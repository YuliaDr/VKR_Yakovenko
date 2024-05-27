import json

import numpy as np


def write(size, res, name):
    if type(res) is list:
        with open(name, 'w') as fw:
            json.dump((size, res), fw)
    else:
        with open(name, 'wb') as fw:
            np.save(fw, size, allow_pickle=True)
            np.save(fw, res, allow_pickle=True)


def read(name):
    if name.find(".txt") != -1:
        with open(name, 'r') as fr:
            size, res = json.load(fr)
    else:
        with open(name, 'rb') as fr:
            size = np.load(fr, allow_pickle=True)
            res = np.load(fr, allow_pickle=True)
    return size, res
