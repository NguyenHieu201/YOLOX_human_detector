#!/bin/bash
input="./datasets/mlti_cam/many_people_cut1m/ch03.mp4"
exp="./custom_exp/ch03.py"

for value in {5..100..5}
do
    ckpt="/home/hieu/hieunm/kaggle/ver2/ByteTrack/YOLOX_outputs/custom_exp_201/epoch_"$value"_ckpt.pth.tar"
    python3 tools/demo_track.py video -f $exp -c "$ckpt" \
        --fp16 --fuse --save_result --path $input \
        --track_thresh 0.75 --track_buffer 10
done                                        

