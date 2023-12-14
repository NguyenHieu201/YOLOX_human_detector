import os
import json

annotation_path = "./datasets/supermarket_dataset/annotations/train.json"
dataset_path = "./datasets/supermarket_dataset/train/"
train_path = "./train.json"
val_path = "./val.json"
train_ratio = 0.8
seqs = ["201_20231129_184822", "202_20231129_184822", "203_20231129_184822", "204_20231129_184822",
        "201_20231204_120908", "202_20231204_120908", "203_20231204_120908", "204_20231204_120908",
        "201_20231207_095105", "202_20231207_095105", "203_20231207_095105", "204_20231207_095105"]

vals = [list(range(1, 31)) + list(range(1600, 1611)), list(range(1, 31)) + list(range(1600, 1611)), list(range(1, 31)) + list(range(1600, 1611)), list(range(1, 31)) + list(range(1600, 1611)),
        list(range(400, 421)) + list(range(900, 921)), list(range(400, 421)) + list(range(900, 921)), list(range(400, 421)) + list(range(900, 921)), list(range(400, 421)) + list(range(900, 921)),
        list(range(1, 31)) + list(range(1600, 1611)), list(range(1, 31)) + list(range(1600, 1611)), list(range(1, 31)) + list(range(1600, 1611)), list(range(1, 31)) + list(range(1600, 1611))]

def split_by_name(annotations, filenames):
    datas = {"images": [], "annotations": [], "videos": [], "categories": []}
    datas['videos'] = annotations['videos']
    datas['categories'] = annotations['categories']
    image_ids = []
    for image in annotations['images']:
        if image['file_name'] in filenames:
            datas['images'].append(image)
            image_ids.append(image['id'])

    for annotation in annotations['annotations']:
        if annotation['image_id'] in image_ids:
            datas['annotations'].append(annotation)
    return datas


if __name__ == "__main__":
    anns = json.load(open(annotation_path, "r"))
    train_files = []
    val_files = []
    for val, seq in zip(vals, seqs):
        video_path = os.path.join(dataset_path, seq, "img1")
        filenames = os.listdir(video_path)
        frame_ids = [int(filename.removesuffix(".jpg")) for filename in filenames]
        train = set(frame_ids) - set(val)
        train = list(train)

        for idx in train:
            train_files.append(os.path.join(seq, "img1", f"{idx:06d}.jpg"))
        for idx in val:
            val_files.append(os.path.join(seq, "img1", f"{idx:06d}.jpg"))

    train_annotaions = split_by_name(anns, train_files)
    val_annotaions = split_by_name(anns, val_files)

    json.dump(train_annotaions, open(train_path, "w"))
    json.dump(val_annotaions, open(val_path, "w"))
        


        
