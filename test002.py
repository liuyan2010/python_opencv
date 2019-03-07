#!/usr/bin/python
import numpy as np
import cv2

src = cv2.imread("D:/python_project/picture/2.jpg", 0)
cv2.imshow("input image", src)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows();
else:
    cv2.imwrite("hello01.png", src);
    cv2.destroyAllWindows()


