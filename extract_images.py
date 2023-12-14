import os
from pathlib import Path
import cv2

video_path = "./datasets/supermarket_ds/20231129_184822/204_20231129_184822.mp4"
frame_range = list(range(1, 151)) + list(range(1600, 1651))
output_path = "./datasets/supermarket_dataset/"

if __name__ == "__main__":
    cap = cv2.VideoCapture(video_path)
    video_path = Path(video_path)
    video_name = video_path.name
    output_folder = video_name.replace(".mp4", "")

    output_path = os.path.join(output_path, output_folder, "img1")
    os.makedirs(output_path, exist_ok=True)
    idx = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if idx in frame_range:
            filename = os.path.join(output_path, f"{idx:06d}.jpg")
            cv2.imwrite(filename, frame)
        idx += 1

