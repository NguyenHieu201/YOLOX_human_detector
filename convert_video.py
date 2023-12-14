import os
import os.path as osp
import shutil

import cv2

def main(video_path, skip_frame=1):
    cap = cv2.VideoCapture(video_path)
    print(cap.get(cv2.CAP_PROP_FPS))
    i = 0

    # video_path = "datasets/mlti_cam/many_people_cut1m/ch02.mp4"

    out_dir = "/".join(video_path.split("/")[:-1])
    out_name = video_path.split("/")[-1].replace(".mp4", "")

    for name in ["train/cam/gt", "train/cam/img1"]:
        try:
            os.makedirs(osp.join(out_dir, out_name, name))
        except FileExistsError:
            continue
    shutil.copy(osp.join(out_dir, f"{out_name}.txt"), 
                osp.join(out_dir, out_name, "train/cam/gt/gt.txt"))
    out_dir = osp.join(out_dir, out_name, "train/cam/img1")
    

    while True:
        i += 1
        ret, frame = cap.read()
        if not ret:
            break
        if (i % skip_frame) == 0:
            out_file = osp.join(out_dir, f"{i:06d}.jpg")
            cv2.imwrite(out_file, frame)
    print(f"{i} frame")

main("./datasets/mlti_cam/many_people_cut1m/ch02.mp4")
main("./datasets/mlti_cam/many_people_cut1m/ch03.mp4")
main("./datasets/mlti_cam/many_people_cut1m/ch04.mp4")
main("./datasets/mlti_cam/many_people_cut1m/ch06.mp4")
main("./datasets/mlti_cam/many_people_cut1m/ch07.mp4")
main("./datasets/mlti_cam/many_people_cut1m/ch08.mp4")

