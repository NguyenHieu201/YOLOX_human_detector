ckpt="./pretrained/bytetrack_l_mot17.pth.tar"
# ckpt="./pretrained/yolox_l_w40_epoch200.pth"
# ckpt="./pretrained/yolox_2023_10_26_79.tar"
# ckpt="./pretrained/freeze_backbone.tar"
# ckpt="./pretrained/freeze_backbone_epoch20.tar"
# ckpt="./pretrained/freeze_backbone_bn.tar"

# python3 tools/demo_track.py video -f "./custom_exp/ch02.py" -c $ckpt --fp16 --fuse --save_result --path "./datasets/mlti_cam/many_people_cut1m/ch02.mp4" \
#         --track_thresh 0.75 --track_buffer 30

# python3 tools/demo_track.py video -f "./custom_exp/ch03.py" -c $ckpt --fp16 --fuse --save_result --path "./datasets/mlti_cam/many_people_cut1m/ch03.mp4" \
#         --track_thresh 0.75 --track_buffer 30     

python3 tools/custom_demo_track.py video -f "./custom_exp/ch03.py" -c $ckpt --fp16 --save_result --path "./datasets/mlti_cam/many_people_cut1m/ch03.mp4" \
        --track_thresh 0.75 --track_buffer 30 --device gpu

# python3 tools/demo_track.py image -f $exp -c $ckpt --fp16 --fuse --save_result --path $input \
#         --track_thresh 0.75 --track_buffer 20

# scp -r hoangnh@192.168.1.54:/home/hoangnh/multicams_human_tracking/data/gt/many_people_cut1m /home/hieu/hieunm/ByteTrack/datasets/mlti_cam
# scp -r hoangnh@192.168.1.54:/home/hoangnh/multicams_human_tracking/videos/input/many_people_cut1m /home/hieu/hieunm/ByteTrack/datasets/mlti_cam