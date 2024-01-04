import os
import cv2
import json
import numpy as np

from tqdm import tqdm

def draw_bbox(ori_img, bboxes, scores, color=(0, 0, 255)):
    img = ori_img
    for bbox, score in zip(bboxes, scores):
        # x1, y1, x2, y2 = [int(i) for i in bbox]
        x, y, w, h = bbox
        x1, y1, x2, y2 = int(x), int(y), int(x + w), int(y + h)

        thickness=1
        c1, c2 = (x1, y1), (x2, y2)
        img = cv2.rectangle(img=img, pt1=c1, pt2=c2, color=color, thickness=thickness)

        label = f"{score:.2f}"
        y = x1 - 15 if y1 - 15 > 15 else y1 + 15
        img = cv2.putText(img, label, (x1, y1+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) 
    return img

def draw(pred="./temp/poly_7.json", image_id=90, is_val=False):
    print("Running file: " + pred)
    filename = os.path.join("datasets/mlti_cam/many_people_cut1m/ch03/train/cam/img1", f"{image_id:06d}.jpg")
    img = cv2.imread(filename)
    outdir = f"./output/visualize/{image_id}"
    outfile = pred.split("/")[-2] + pred.split("/")[-1].replace(".json", ".jpg")
    outfile = os.path.join(outdir, outfile)

    pred = json.load(open(pred, "r"))
    if is_val:
        pred = pred["annotations"]
    bboxes = [p["bbox"] for p in pred if p["image_id"] == image_id]
    if is_val:
        scores = [1 for bbox in bboxes]
    else:
        scores = [p["score"] for p in pred if p["image_id"] == image_id]

    img = draw_bbox(img, bboxes, scores, (0, 0, 255)) 

    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    cv2.imwrite(outfile, img)
    print(f"Detected Boxes: {len(bboxes)}")

    if is_val:
        right, left = 0, 0
        for bbox in bboxes:
            if bbox[0] > 539:
                right += 1
            else:
                left += 1
        print(f"Left box: {left} - Right box: {right}")

def draw_seq(in_path="datasets/mlti_cam/many_people_cut1m/ch03/train/cam/img1", pred=""):
    pred = json.load(open(pred, "r"))
    outdir = f"./output/det"
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    for i in tqdm(range(1, 1801)):
        filename = os.path.join(in_path, f"{i:06d}.jpg")
        img = cv2.imread(filename)
        outfile = f"{i:06d}.jpg"
        outfile = os.path.join(outdir, outfile)

        bboxes = [p["bbox"] for p in pred if p["image_id"] == i]
        scores = [p["score"] for p in pred if p["image_id"] == i]

        img = draw_bbox(img, bboxes, scores, (0, 0, 255)) 
        cv2.imwrite(outfile, img)
            


# image_id = 1800
draw_seq(in_path="./datasets/supermarket_dataset/train/", 
         pred="./output/detection/ch03_nms70_conf0/yolox_2023_10_26_79.json")
# draw("./output/detection/ch03_nms85_conf1/bytetrack_l_mot17.json", image_id)
# for image_id in range(10, 1810, 10):
    # draw("./output/detection/ch03_nms85_conf1/bytetrack_l_mot17.json", image_id)
    # draw("./output/detection/ch03_540_nms85_conf1/bytetrack_l_mot17.json", image_id)
    # draw("./datasets/mlti_cam/many_people_cut1m/ch02/annotations/train.json", image_id, True)
    # draw("epoch200_w40/ch07_nms85_conf1/bytetrack_l_mot17.json", image_id)
# draw("./epoch_80_w_10/train/pretrained_nms85_conf1.json", image_id)

# draw("./epoch_30/poly_nms7_conf5.json", image_id)
# draw("./epoch_30/poly_nms4_conf1.json", image_id)
# draw("./epoch_30/poly_nms4_conf5.json", image_id)
# draw("./epoch_30/test.json", image_id)
# draw("./epoch_30/nms7_conf1.json", image_id)
# draw("./epoch_30/nms85_conf15.json", image_id)
# draw("./epoch_30/test.json", image_id)
# draw("./epoch_30/left_nms9_conf2.json", image_id)
# draw("./epoch_30/right_nms85_conf2.json", image_id)
