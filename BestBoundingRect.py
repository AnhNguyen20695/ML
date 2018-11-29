import numpy as np
import cv2 as cv
from CountWhitePixel import CountWhitePixel
#########
# Returns the best fit bounding rect from a list of rects
#########
def BestBoundingRect(img, rects):
        BestRect = rects[0]
        ret, thresh = cv.threshold(img, 0, 255,cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
        for rect in rects:
                x,y,w,h = rect
                rect_white_ratio = CountWhitePixel(thresh[y:y+h, x:x+w]) / (w*h)
                BestRect_white_ratio = (CountWhitePixel(thresh[BestRect[1]:BestRect[1] + BestRect[3],
                        BestRect[0]:BestRect[0]+BestRect[2]])) / (BestRect[2]*BestRect[3])
                if (rect_white_ratio >= BestRect_white_ratio):
                        BestRect = rect
        return BestRect