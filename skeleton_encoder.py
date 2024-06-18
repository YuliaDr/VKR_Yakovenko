import cv2
from preprocessing import preprocess
from opca import opca
from file_operations import write
from skeleton_vectorization import find_circles

img = cv2.imread("kartinka_ch_b.jpg")

preprocessed_img = preprocess(img)

skeleton = opca(preprocessed_img)
circles = find_circles(preprocessed_img, skeleton)

write((preprocessed_img.shape[0], preprocessed_img.shape[1]), circles, "skeleton_res.txt")
