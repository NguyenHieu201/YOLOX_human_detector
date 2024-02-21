import os
import json
import cv2
import random

def draw_bbox(ori_img, bboxes, color=(0, 0, 255)):
    img = ori_img
    for bbox in bboxes:
        # x1, y1, x2, y2 = [int(i) for i in bbox]
        x, y, w, h = bbox
        x1, y1, x2, y2 = int(x), int(y), int(x + w), int(y + h)

        thickness=1
        c1, c2 = (x1, y1), (x2, y2)
        img = cv2.rectangle(img=img, pt1=c1, pt2=c2, color=color, thickness=thickness)
    return img

def visuzlize_dataset(in_path, annotations, out_path):
    annotations = json.load(open(annotations, "r"))
    images = annotations["images"]
    bboxes = annotations["annotations"]

    rand_images = random.choices(images, k=100)
    for image in rand_images:
        image_id = image['id']
        image_filename = image['file_name']
        bbox = [bbox['bbox'] for bbox in bboxes if bbox['image_id'] == image_id]

        img = cv2.imread(os.path.join(in_path, image_filename))
        img = draw_bbox(img, bbox)
        cv2.imwrite(os.path.join(out_path, f"{image_id}.jpg"), img)

if __name__ == "__main__":
    visuzlize_dataset(in_path="/home/hieu/hieunm/ByteTrack/datasets/supermarket_train_20240220/train",
                      annotations="/home/hieu/hieunm/ByteTrack/datasets/supermarket_train_20240220/annotations/train.json",
                      out_path="./visualize_dataset")

