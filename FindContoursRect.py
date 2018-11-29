import cv2 as cv

#########
# Find the contour with the second largest area.
# Since contour with the largest area is the whole image
#########

def FindContoursRect(im):
    ret, thresh = cv.threshold(im, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    _, cnts, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cSorted = sorted(cnts, key=lambda x: cv.contourArea(x), reverse=True)
    if (len(cSorted) == 1):
        return cv.boundingRect(cSorted[0])
    else:
        return cv.boundingRect(cSorted[1])