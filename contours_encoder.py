import cv2
from file_operations import write
from preprocessing import preprocess

img = cv2.imread("kartinka_ch_b.jpg")

preprocessed_img = preprocess(img)

contours, hierarchy = cv2.findContours(preprocessed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

write((preprocessed_img.shape[0], preprocessed_img.shape[1]), contours, "contours_res.npy")
