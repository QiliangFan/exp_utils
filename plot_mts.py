import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
import os
from glob import glob
plt.rcParams["figure.dpi"] = 400
plt.style.use("ggplot")


def main(file: str):
    data = np.loadtxt(file, delimiter=",")
    dim = data.shape[1]
    ranges = list(range(8, 15))
    fig, ax = plt.subplots(len(ranges), sharex=True, figsize=(15, 10))

    for i, key in enumerate(ranges):
        MIN, MAX = data[:, key].min(), data[:, key].max()
        ax[i].plot(data[:, key], color="gray")
        ax[i].tick_params(left=False, right=False, labelleft=False,
                    labelbottom=False, bottom=False)
        ax[i].fill_between(list(range(5500, 6500)), MIN - 1e-6, MAX + 1e-6, alpha=0.6, color="cyan")
        ax[i].fill_between(list(range(14200, 16200)), MIN - 1e-6, MAX + 1e-6, alpha=0.6, color="pink")
        ax[i].fill_between(list(range(25500, 26500)), MIN - 1e-6, MAX + 1e-6, alpha=0.6, color="salmon")
    plt.tight_layout(pad=0.2, h_pad=None)
    plt.savefig("MTS.pdf", bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    root = "/home/fanqiliang/data/dataset/MTS/SMD/train"
    name = "machine-1-1.txt"
    file = os.path.join(root, name)
    main(file)
