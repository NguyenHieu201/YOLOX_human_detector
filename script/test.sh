exp="./custom_exp/ch03.py"
ckpt="./pretrained/bytetrack_l_mot17.pth.tar"
path="/home/hieu/Downloads/crop.jpg"
conf=0.1
nms=0.85

python tools/demo.py image -f $exp -c $ckpt --path $path --conf $conf --nms $nms \
                           --save_result --device gpu --fp16

# python tools/demo.py video -f $exp -c $ckpt --path "./datasets/mlti_cam/many_people_cut1m/ch03.mp4" --conf $conf --nms $nms \
#                            --save_result --device gpu