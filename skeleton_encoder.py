import cv2
from opca import opca
from file_operations import write
from skeleton_vectorization import find_circles
from draw_skeleton import draw_skeleton

img = cv2.imread("kartinka_ch_b.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

resize_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
resize_thresh = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)

skeleton = opca(resize_thresh)
circles = find_circles(resize_thresh, skeleton)

write((resize_thresh.shape[0], resize_thresh.shape[1]), circles, "skeleton_res.txt")