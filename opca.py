import cv2
import numpy as np


def is_first_condition(src, y, x):
    points = [
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
    ]
    sum = 0
    for i in range(8):
        sum += src[points[i]] / 255
    return 2 <= sum <= 6


def is_second_condition(src, y, x):
    points = [
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
    ]
    sum = 0
    for i in range(8):
        j = ((i + 2) - 2 + 1) % 8 + 2
        sum += abs(src[points[i]] / 255 - src[points[j - 2]] / 255)
    return sum == 2


def is_third_condition(src, y, x):
    points = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y),
        (x + 2, y),
        (x, y + 2),
    ]
    parts = [False] * 6
    for i in range(6):
        if i == 1 or i == 2:
            parts[i] = src[points[i]] / 255 == 1
        else:
            parts[i] = src[points[i]] / 255 == 0
    return not ((parts[1] and parts[3] and parts[4]) or (parts[2] and parts[0] and parts[5]))


def is_last_condition(src, y, x):
    points = [
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
    ]
    count = 0
    for i in range(4):
        parts = [False] * 3
        j = 2 * i + 1
        k = ((2 * (i + 1) + 1) - 2 + 3) % 8 + 2
        m = ((2 * (i + 1) + 1) - 2 + 5) % 8 + 2
        parts[0] = src[points[j]] / 255 == 0
        parts[1] = src[points[k - 2]] / 255 == 1
        parts[2] = src[points[m - 2]] / 255 == 1
        if parts[0] and parts[1] and parts[2]:
            count += 1
    return count == 4


def opca(src):
    res_points = []
    dst = src.copy()
    isEnd = False
    while not isEnd:
        isEnd = True
        matrix = np.ones(dst.shape, dtype=np.uint8)
        for x in range(1, src.shape[0] - 1):
            for y in range(1, src.shape[1] - 1):
                if dst[x, y] / 255 == 1:
                    if (is_first_condition(dst, y, x) and is_second_condition(dst, y, x)
                            and is_third_condition(dst, y, x)):
                        matrix[x, y] = 0
                        isEnd = False
        dst = cv2.multiply(dst, matrix)
    for y in range(1, src.shape[0] - 1):
        for x in range(1, src.shape[1] - 1):
            if dst[y, x] / 255 == 1:
                if is_last_condition(dst, y, x):
                    dst[x, y] = 0
                else:
                    res_points.append((x, y))
    return res_points
