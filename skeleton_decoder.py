import cv2
from draw_skeleton import draw_circles
from file_operations import read

size, circles = read("skeleton_res.txt")

draw_circles(circles, size)

cv2.waitKey(0)
cv2.destroyAllWindows()
