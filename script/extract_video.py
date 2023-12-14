import os
import argparse
import cv2


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, required=True)
    parser.add_argument("--save_path", type=str, required=True)
    opt = parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    video_path = opt.video_path
    save_path = opt.save_path
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    cap = cv2.VideoCapture(video_path)
    i = 1
    while True:
        ret, frame = cap.read()
        frame_path = os.path.join(save_path, f"{i:06d}.jpg")
        if not ret:
            break
        cv2.imwrite(frame_path, frame)
        i += 1