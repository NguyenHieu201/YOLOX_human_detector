import os
import numpy as np
import cv2
import json

DATA_PATH = '/home/hieu/hieunm/ByteTrack/datasets/evaluation/tmp/'
OUT_PATH = '/home/hieu/hieunm/ByteTrack/datasets/evaluation/tmp_out'
REQUIRE_IMAGES = False

if __name__ == "__main__":
    os.makedirs(OUT_PATH, exist_ok=True)
    seqs = os.listdir(DATA_PATH)
    out_path = os.path.join(OUT_PATH, "data.json")
    out = {'images': [], 'annotations': [], 'videos': [],
            'categories': [{'id': 1, 'name': 'pedestrian'}]}
    image_cnt = 0
    ann_cnt = 0
    video_cnt = 0
    for seq in seqs:
        video_cnt += 1
        image_folder = os.path.join(DATA_PATH, seq, "img1")
        gt_file = os.path.join(DATA_PATH, seq, "gt", "gt.txt")
        gt = np.loadtxt(gt_file, delimiter=",", dtype=np.float32)
        images = os.listdir(image_folder)
        images = [image for image in images if ".jpg" in image]
        out['videos'].append({'id': video_cnt, 'file_name': seq})

        print(f"{seq}: Load {len(images)} images")

        for image in images:
            image_cnt += 1
            frame_idx = int(image.removesuffix(".jpg"))
            if REQUIRE_IMAGES:
                img = cv2.imread(os.path.join(image_folder, image))
                height, width = img.shape[:2]
            else:
                height, width = 1080, 1920
            # bboxes = gt[gt[:, 0] == frame_idx]
            bboxes = gt[np.where(gt[:, 0] == frame_idx)]

            image_info = {
                'file_name': f"{seq}/img1/{image}",
                'id': image_cnt,
                'frame_id': frame_idx,
                'prev_image_id': -1,
                'next_image_id': -1,
                'video_id': video_cnt,
                'height': height, 'width': width
            }
            out['images'].append(image_info)

            for bbox in bboxes:
                ann_cnt += 1
                ann = {
                    'id': ann_cnt,
                    'image_id': image_cnt,
                    'category_id': 1,
                    'track_id': int(bbox[1]),
                    'bbox': bbox[2:6].tolist(),
                    'conf': 1.0,
                    'iscrowd': 0,
                    'area': float(bbox[4] * bbox[5])
                }
                out['annotations'].append(ann)

    json.dump(out, open(out_path, "w"), indent=4)

