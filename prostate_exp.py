import os
from collections import OrderedDict
from glob import glob
import pandas as pd
import numpy as np

data_root = "/home/fanqiliang/data/nutstore/工作内容/写作/prostate_seg_1/实验结果/exp2"
output_file = "exp.xlsx"

def main():
    versions = glob(os.path.join(data_root, "**", "version_*"), recursive=True)
    versions.sort()

    fold = []
    dice = []
    precision = []
    recall = []
    hd = []
    abd = []
    ravd = []

    base_dice = []
    base_hd = []
    base_abd = []
    base_ravd = []

    mid_dice = []
    mid_hd = []
    mid_abd = []
    mid_ravd = []

    apex_dice = []
    apex_hd = []
    apex_abd = []
    apex_ravd = []

    for idx, v in enumerate(versions):
        file = os.path.join(v, "metrics.csv")
        dt = pd.read_csv(file)
        for _, row in dt.tail(1).iterrows():
            fold.append(idx)
            dice.append(row["dice"])
            precision.append(row["precision"])
            recall.append(row["recall"])
            hd.append(row["hd"])
            abd.append(row["abd"])
            ravd.append(row["ravd"])

            base_dice.append(row["base_dice"])
            base_hd.append(row["base_hd"])
            base_abd.append(row["base_abd"])
            base_ravd.append(row["base_ravd"])

            mid_dice.append(row["mid_dice"])
            mid_hd.append(row["mid_hd"])
            mid_abd.append(row["mid_abd"])
            mid_ravd.append(row["mid_ravd"])

            apex_dice.append(row["apex_dice"])
            apex_hd.append(row["apex_hd"])
            apex_abd.append(row["apex_abd"])
            apex_ravd.append(row["apex_ravd"])
    result_dt = pd.DataFrame(OrderedDict({
        "fold": fold,
        "dice": dice,
        "precision": precision,
        "recall": recall,
        "hd": hd,
        "abd": abd,
        "ravd": ravd,
        "base_dice": base_dice,
        "base_hd": base_hd,
        "base_abd": base_abd,
        "base_ravd": base_ravd,
        "mid_dice": mid_dice,
        "mid_hd": mid_hd,
        "mid_abd": mid_abd,
        "mid_ravd": mid_ravd,
        "apex_dice": apex_dice,
        "apex_hd": apex_hd,
        "apex_abd": apex_hd,
        "apex_ravd": apex_ravd
    }))
    result_dt.to_excel(f"{os.path.join(data_root, output_file)}", index=False)


if __name__ == "__main__":
    main()