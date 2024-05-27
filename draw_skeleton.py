import cv2
import numpy as np


def draw_skeleton(skeleton, size):
    img = np.uint8(np.zeros((size[0], size[1])))

    for (x, y) in skeleton:
        img[y, x] = 255

    cv2.imshow("Skeleton", img)
    return img


def draw_circles(circles, size):
    img = np.uint8(np.zeros((size[0], size[1])))

    for (x, y, r) in circles:
        cv2.circle(img, (y, x), r, (255, 255, 255), 1)
    cv2.imshow("With circles", img)
