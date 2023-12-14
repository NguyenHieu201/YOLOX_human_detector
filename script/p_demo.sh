input="./datasets/mlti_cam/many_people_cut1m/ch03.mp4"
exp="./custom_exp/ch03.py"

# ckpt="./pretrained/bytetrack_l_mot17.pth.tar"
# ckpt="./pretrained/yolox_l_w40_epoch200.pth"
# ckpt="./pretrained/yolox_2023_10_26_79.tar"
# ckpt="./pretrained/freeze_backbone.tar"
# ckpt="./pretrained/freeze_backbone_epoch20.tar"
# ckpt="./pretrained/freeze_backbone_bn.tar"


# python3 tools/demo_track.py video -f $exp -c "./pretrained/bytetrack_l_mot17.pth.tar" --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.5 --track_buffer 20

# python3 tools/demo_track.py video -f $exp -c "./pretrained/yolox_l_w40_epoch200.pth" --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.5 --track_buffer 20

# python3 tools/demo_track.py video -f $exp -c "./pretrained/yolox_2023_10_26_79.tar" --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.5 --track_buffer 20

# python3 tools/demo_track.py video -f $exp -c "./pretrained/freeze_backbone.tar" --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.5 --track_buffer 20

# python3 tools/demo_track.py video -f $exp -c "./pretrained/freeze_backbone_epoch20.tar" --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.5 --track_buffer 20

# python3 tools/demo_track.py video -f $exp -c "./pretrained/freeze_backbone_bn.tar" --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.5 --track_buffer 20                     