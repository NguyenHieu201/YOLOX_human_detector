exp_file="./custom_exp/pretrained.py"
ckpt="./pretrained/yolox_x.pth"
python3 tools/train.py -f $exp_file -d 1 -b 2 --fp16 -o -c $ckpt