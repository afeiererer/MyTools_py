import cv2
import numpy as np
import SimpleITK as sitk
from helper import *
#
# img = cv2.imread("hammer.jpg", 0)
# cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
# cv2.imshow("canny", cv2.imread("canny.jpg"))
# cv2.waitKey()
# cv2.destroyAllWindows()



cv2.namedWindow('win',flags=cv2.WINDOW_NORMAL|cv2.WINDOW_FREERATIO)

global v1
global v2
global img


def find(x):
    global v1,v2,img
    global  img
    v1 = cv2.getTrackbarPos('low', 'win')
    v2 = cv2.getTrackbarPos('up', 'win')

    cv2.imshow("win", img)

if __name__ == '__main__':
    global img
    cv2.createTrackbar('low', 'win', 0, 3000, find)
    cv2.createTrackbar('up', 'win', 0,5000, find)

    filePath=r"G:\zigong\data\LIQIANRU\data\roi_3D_l.mhd"
    img = sitk.GetArrayFromImage(sitk.ReadImage(filePath))[5]


    find(0)

    cv2.waitKey(0)