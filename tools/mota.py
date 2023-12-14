from loguru import logger

import torch
import torch.backends.cudnn as cudnn
from torch.nn.parallel import DistributedDataParallel as DDP

from yolox.core import launch
from yolox.exp import get_exp
from yolox.utils import configure_nccl, fuse_model, get_local_rank, get_model_info, setup_logger
from yolox.evaluators import MOTEvaluator

import argparse
import os
import random
import warnings
import glob
import motmetrics as mm
from collections import OrderedDict
from pathlib import Path



def compare_dataframes(gts, ts):
    accs = []
    names = []
    for k, tsacc in ts.items():
        if k in gts:            
            logger.info('Comparing {}...'.format(k))
            accs.append(mm.utils.compare_to_groundtruth(gts[k], tsacc, 'iou', distth=0.5))
            names.append(k)
        else:
            logger.warning('No ground truth for {}, skipping.'.format(k))

    return accs, names


# evaluate MOTA
# results_folder = 'YOLOX_outputs/yolox_x_ablation/track_results'
mm.lap.default_solver = 'lap'

# gt_type = '_val_half'
# #gt_type = ''
# print('gt_type', gt_type)
# gtfiles = glob.glob(
#     os.path.join('datasets/mot/train', '*/gt/gt{}.txt'.format(gt_type)))
# print('gt_files', gtfiles)
# tsfiles = [f for f in glob.glob(os.path.join(results_folder, '*.txt')) if not os.path.basename(f).startswith('eval')]

# gtfiles = ["datasets/mlti_cam/many_people_cut1m/ch02/train/cam/gt/gt.txt"]
cam = "ch03"
# video = ["pretrained", "200epochs", "80epochs", "backbone10", "backbone20", "bn10"]
video = ["80epochs"]
# video = list(range(5, 105, 5))
gtfiles = [f"./datasets/mlti_cam/many_people_cut1m/{cam}/train/cam/gt/gt.txt"] * len(video)
# tsfiles = [f"epoch_{i}_ckpt.txt" for i in video]
tsfiles = ["yolox_2023_10_26_79.txt"]
# tsfiles = ["bytetrack_l_mot17.txt", "yolox_l_w40_epoch200.txt",
#                         "yolox_2023_10_26_79.txt", "freeze_backbone.txt",
#                         "freeze_backbone_epoch20.txt", "freeze_backbone_bn.txt"]
# tsfiles = [os.path.join(f"YOLOX_outputs/{cam}/track_vis", tsfile) for tsfile in tsfiles]
tsfiles = ["temp/track.txt"]



logger.info('Found {} groundtruths and {} test files.'.format(len(gtfiles), len(tsfiles)))
logger.info('Available LAP solvers {}'.format(mm.lap.available_solvers))
logger.info('Default LAP solver \'{}\''.format(mm.lap.default_solver))
logger.info('Loading files.')

# gt = [Path(f).parts[-1] for f in gtfiles]
# print(Path(gtfiles[0]).parts[-1])

# assert False

gt = OrderedDict([(v, mm.io.loadtxt(f, fmt='mot15-2D', min_confidence=1)) for v, f in zip(video, gtfiles)])
ts = OrderedDict([(v, mm.io.loadtxt(f, fmt="mot15-2D", min_confidence=-1.0)) for v, f in zip(video, tsfiles)])
# ts = OrderedDict([(os.path.splitext(Path(f).parts[-1])[0], mm.io.loadtxt(f, fmt='mot15-2D', min_confidence=-1.0)) for f in tsfiles])    

mh = mm.metrics.create()    
accs, names = compare_dataframes(gt, ts)

logger.info('Running metrics')
metrics = ['recall', 'precision', 'num_unique_objects', 'mostly_tracked',
            'partially_tracked', 'mostly_lost', 'num_false_positives', 'num_misses',
            'num_switches', 'num_fragmentations', 'mota', 'motp', 'num_objects']
summary = mh.compute_many(accs, names=names, metrics=metrics, generate_overall=True)
# summary = mh.compute_many(accs, names=names, metrics=mm.metrics.motchallenge_metrics, generate_overall=True)
# print(mm.io.render_summary(
#   summary, formatters=mh.formatters, 
#   namemap=mm.io.motchallenge_metric_names))
div_dict = {
    'num_objects': ['num_false_positives', 'num_misses', 'num_switches', 'num_fragmentations'],
    'num_unique_objects': ['mostly_tracked', 'partially_tracked', 'mostly_lost']}
for divisor in div_dict:
    for divided in div_dict[divisor]:
        summary[divided] = (summary[divided] / summary[divisor])
fmt = mh.formatters
change_fmt_list = ['num_false_positives', 'num_misses', 'num_switches', 'num_fragmentations', 'mostly_tracked',
                    'partially_tracked', 'mostly_lost']
for k in change_fmt_list:
    fmt[k] = fmt['mota']
print(mm.io.render_summary(summary, formatters=fmt, namemap=mm.io.motchallenge_metric_names))

metrics = mm.metrics.motchallenge_metrics + ['num_objects']
summary = mh.compute_many(accs, names=names, metrics=metrics, generate_overall=True)
print(mm.io.render_summary(summary, formatters=mh.formatters, namemap=mm.io.motchallenge_metric_names))
logger.info('Completed')
