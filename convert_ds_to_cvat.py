import pandas as pd
itm_data_path = "/home/hieu/hieunm/multicam/multicams_human_tracking/data/supermarket_pmodel_20231220_185141/input/208.txt"
df = pd.read_csv(itm_data_path, header=None)
df[2] = df[2]
df[3] = df[3]
df[4] = df[4]
df[5] = df[5]
df[7] = 1
df[8] = 1
df[9] = 1.0
df.to_csv("./generate_labels/gt/gt.txt", index=False, header=False)