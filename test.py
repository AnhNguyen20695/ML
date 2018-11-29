import cv2 as cv
import os
from predict_img import predict_img
from FindRectangle import FindRectangle
from FindContoursRect import FindContoursRect
from BestBoundingRect import BestBoundingRect
from adjust_img import adjust_img
import numpy as np

def step2(image):
    return FindRectangle(image)

def step3(image, rect):
    xs,ys,ws,hs = rect
    image = image[ys:ys+hs, xs:xs+ws]
    adjust_img(image)
    image = cv.imread("adjusted_img.jpg", 0)
    image = cv.resize(image, (28,28))
    cl, pr = predict_img(image, iwhite_background=True)
    return cl, pr

if __name__ == '__main__':
    img_path = "sample/cut_boxes/Doc0001/ex4.png"
    img = cv.imread(img_path, 0)
    rects = step2(img)
    print(len(rects))
    for rect in rects:
        x,y,w,h = rect
        cropped_img = img[y+3:y+h-3, x+3:x+w-3]
        rect_s = FindContoursRect(cropped_img)
        result_cl, result_pr = step3(cropped_img, rect_s)
        # if (result_pr >= 0.4):
        cv.imwrite("sample/Doc00xx_new/{}-{}%.jpg".format(
            result_cl, round(result_pr*100, 4)), cropped_img)
    os.remove("adjusted_img.jpg")