# exp_file="./custom_exp/mlti_cam.py"
# ckpt="./pretrained/bytetrack_l_mot17.pth.tar"
# ckpt="./pretrained/yolox_l_w40_epoch200.pth"
# ckpt="./pretrained/freeze_backbone.tar"
# ckpt="./pretrained/freeze_backbone_epoch20.tar"
# ckpt="./pretrained/freeze_backbone_bn.tar"
save_dir="./output/detection"
exp="./custom_exp/supermarket.py"
conf=0.1

ckpt="./pretrained/spm_retrain.tar"
echo $ckpt
python3 detection_evaluation.py -f $exp -d 1 -b 2 --fp16 -o -c $ckpt --save_dir $save_dir

ckpt="./pretrained/yolox_2023_10_26_79.tar"
echo $ckpt
python3 detection_evaluation.py -f $exp -d 1 -b 2 --fp16 -o -c $ckpt --save_dir $save_dir

ckpt="./pretrained/epoch15.tar"
echo $ckpt
python3 detection_evaluation.py -f $exp -d 1 -b 2 --fp16 -o -c $ckpt --save_dir $save_dir

ckpt="./pretrained/bytetrack_l_mot17.pth.tar"
echo $ckpt
python3 detection_evaluation.py -f $exp -d 1 -b 2 --fp16 -o -c $ckpt --save_dir $save_dir