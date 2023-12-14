#!/bin/bash

video="./datasets/mlti_cam/many_people_cut1m/ch07.mp4"
exp="./custom_exp/ch07.py"
# Declare an array of string with type
# declare -a StringArray=("./pretrained/bytetrack_l_mot17.pth.tar" "./pretrained/yolox_l_w40_epoch200.pth" \
#                         "./pretrained/yolox_2023_10_26_79.tar" "./pretrained/freeze_backbone.tar" \
#                         "./pretrained/freeze_backbone_epoch20.tar" "./pretrained/freeze_backbone_bn.tar" \
#                         "./pretrained/whoknow.tar")
declare -a StringArray=("./pretrained/whoknow.tar")

# Iterate the string array using for loop
for ckpt in ${StringArray[@]}; do
    python3 tools/demo_track.py video -f $exp -c $ckpt --fp16 --fuse --save_result \
            --path $video \
            --track_thresh 0.75 --track_buffer 30     
done