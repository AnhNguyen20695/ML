import numpy as np
import cv2 as cv

def adjust_img(img):
    w = img.shape[1]
    h = img.shape[0]
    pad = np.zeros((h+14,w+14))
    pad += 255
    pad[7:h+7, 7:w+7] = img
    cv.imwrite('adjusted_img.jpg', pad)