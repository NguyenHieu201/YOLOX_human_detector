exp="./custom_exp/ch03.py"
ckpt="./pretrained/yolox_2023_10_26_79.tar"
# path="./datasets/mlti_cam/many_people_cut1m/ch03/train/cam/img1/001637.jpg"
path="./datasets/supermarket/201_30s/"
conf=0.1
nms=0.45

python tools/demo.py image -f $exp -c $ckpt --path $path --conf $conf --nms $nms \
                           --save_result --device gpu --fp16