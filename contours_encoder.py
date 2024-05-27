import cv2
from file_operations import write

img = cv2.imread("kartinka_ch_b.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

resize_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
resize_thresh = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)

contours, hierarchy = cv2.findContours(resize_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

write((resize_thresh.shape[0], resize_thresh.shape[1]), contours, "contours_res.npy")
