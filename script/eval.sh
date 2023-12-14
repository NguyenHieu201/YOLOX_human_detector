# exp_file="./custom_exp/mlti_cam.py"
# ckpt="./pretrained/bytetrack_l_mot17.pth.tar"
# ckpt="./pretrained/yolox_l_w40_epoch200.pth"
# ckpt="./pretrained/freeze_backbone.tar"
# ckpt="./pretrained/freeze_backbone_epoch20.tar"
# ckpt="./pretrained/freeze_backbone_bn.tar"
ckpt="./pretrained/yolox_2023_10_26_79.tar"
save_dir="./output/detection"
conf=0.1

# udon cam 201
# python3 detection_evaluation.py -f "./custom_exp/pretrained.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir

# echo 2
# python3 detection_evaluation.py -f "./custom_exp/ch02.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir &
echo 3
python3 detection_evaluation.py -f "./custom_exp/ch03.py" -d 1 -b 2 --fp16 -o -c $ckpt --save_dir $save_dir

# echo 3 540
# python3 detection_evaluation.py -f "./custom_exp/ch03_540.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir
# echo 4
# python3 detection_evaluation.py -f "./custom_exp/ch04.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir
# echo 6
# python3 detection_evaluation.py -f "./custom_exp/ch06.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir
# echo 7
# python3 detection_evaluation.py -f "./custom_exp/ch07.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir
# echo 8
# python3 detection_evaluation.py -f "./custom_exp/ch08.py" -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.85 --save_dir $save_dir




# python3 detection_evaluation.py -f $exp_file -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.5 --save_dir $save_dir
# python3 detection_evaluation.py -f $exp_file -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.6 --save_dir $save_dir
# python3 detection_evaluation.py -f $exp_file -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.7 --save_dir $save_dir
# python3 detection_evaluation.py -f $exp_file -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.8 --save_dir $save_dir
# python3 detection_evaluation.py -f $exp_file -d 1 -b 2 --fp16 -o -c $ckpt --conf $conf --nms 0.9 --save_dir $save_dir