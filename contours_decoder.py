import cv2
import numpy as np
from file_operations import read

size, contours = read("contours_res.npy")

img_contours = np.uint8(np.zeros((size[0], size[1])))
cv2.drawContours(img_contours, contours, -1, (255, 255, 255), 1)

cv2.imshow("Contours", img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
