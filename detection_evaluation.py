import os
from loguru import logger

import torch
import torch.backends.cudnn as cudnn
import numpy as np

from yolox.core import Trainer, launch
from yolox.exp import get_exp

import argparse
import random
import warnings

from yolox.utils.dist import synchronize


def make_parser():
    parser = argparse.ArgumentParser("YOLOX train parser")
    parser.add_argument("-expn", "--experiment-name", type=str, default=None)
    parser.add_argument("-n", "--name", type=str, default=None, help="model name")

    # distributed
    parser.add_argument(
        "--dist-backend", default="nccl", type=str, help="distributed backend"
    )
    parser.add_argument(
        "--dist-url",
        default=None,
        type=str,
        help="url used to set up distributed training",
    )
    parser.add_argument("-b", "--batch-size", type=int, default=64, help="batch size")
    parser.add_argument(
        "-d", "--devices", default=None, type=int, help="device for training"
    )
    parser.add_argument(
        "--local_rank", default=0, type=int, help="local rank for dist training"
    )
    parser.add_argument(
        "-f",
        "--exp_file",
        default=None,
        type=str,
        help="plz input your expriment description file",
    )
    parser.add_argument(
        "--resume", default=False, action="store_true", help="resume training"
    )
    parser.add_argument("-c", "--ckpt", default=None, type=str, help="checkpoint file")
    parser.add_argument(
        "-e",
        "--start_epoch",
        default=None,
        type=int,
        help="resume training start epoch",
    )
    parser.add_argument(
        "--num_machines", default=1, type=int, help="num of node for training"
    )
    parser.add_argument(
        "--machine_rank", default=0, type=int, help="node rank for multi-node training"
    )
    parser.add_argument(
        "--fp16",
        dest="fp16",
        default=True,
        action="store_true",
        help="Adopting mix precision training.",
    )
    parser.add_argument(
        "-o",
        "--occupy",
        dest="occupy",
        default=False,
        action="store_true",
        help="occupy GPU memory first for training.",
    )
    parser.add_argument(
        "opts",
        help="Modify config options using the command-line",
        default=None,
        nargs=argparse.REMAINDER,
    )

    parser.add_argument("--nms", default=None)
    parser.add_argument("--conf", default=None)
    parser.add_argument("--save_dir", default="./temp")
    return parser


@logger.catch
def main(exp, args):
    if exp.seed is not None:
        random.seed(exp.seed)
        torch.manual_seed(exp.seed)
        cudnn.deterministic = True
        warnings.warn(
            "You have chosen to seed training. This will turn on the CUDNN deterministic setting, "
            "which can slow down your training considerably! You may see unexpected behavior "
            "when restarting from checkpoints."
        )

    # set environment variables for distributed training
    # cudnn.benchmark = True
    cudnn.benchmark = False

    # log_writer = open("./epoch_30/right_conf.txt", "a")
    trainer = Trainer(exp, args)
    trainer.before_train()
    summary = trainer.evaluate()
    # log_writer.write(f"nms: {exp.nmsthre}  conf: {exp.test_conf}\n")
    # log_writer.write(f"{summary}\n")
    # log_writer.close()

    print(summary + "\n")


if __name__ == "__main__":
    args = make_parser().parse_args()
    exp = get_exp(args.exp_file, args.name)
    exp.merge(args.opts)

    if not args.experiment_name:
        args.experiment_name = exp.exp_name

    num_gpu = torch.cuda.device_count() if args.devices is None else args.devices
    print(num_gpu)
    assert num_gpu <= torch.cuda.device_count()

    if args.conf is not None:
        exp.test_conf = float(args.conf)

    if args.nms is not None:
        exp.nmsthre = float(args.nms)

    ckpt = args.ckpt
    ckpt = ckpt.split("/")[-1].split(".")[0]
    save_path = os.path.join(args.save_dir, f"{exp.exp_name}_nms{int(exp.nmsthre*100)}_conf{int(exp.test_conf*10)}")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    save_path = os.path.join(save_path, f"{ckpt}.json")
    # save_path = os.path.join(args.save_dir, f"{exp.exp_name}_nms{int(exp.nmsthre*100)}_conf{int(exp.test_conf*10)}.json")
    exp.set_save_path(save_path)
    print(save_path)

    launch(
        main,
        num_gpu,
        args.num_machines,
        args.machine_rank,
        backend=args.dist_backend,
        dist_url=args.dist_url,
        args=(exp, args),
    )