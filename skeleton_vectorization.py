import numpy as np
import math


def remove_redundant_points(coords, n):
    filtered_coords = []
    for i in range(len(coords)):
        is_redundant = False
        for j in range(len(filtered_coords)):
            distance = math.sqrt((coords[i][0] - filtered_coords[j][0])**2 + (coords[i][1] - filtered_coords[j][1])**2)
            if distance < n:
                is_redundant = True
                break
        if not is_redundant:
            filtered_coords.append(coords[i])
    return filtered_coords


def find_circles(img, skeleton):
    circles = []
    filtered_skeleton = remove_redundant_points(skeleton, 3)
    for y, x in filtered_skeleton:
        for r in range(13, -1, -1):
            if x-r >= 0 and y-r >= 0 and x+r <= img.shape[0] and y-r <= img.shape[1] and np.min(img[x-r:x+r+1, y-r:y+r+1]) == 255:
                circles.append((x, y, r))
                break
    return circles
