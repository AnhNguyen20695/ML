import cv2
import numpy as np

##########
# Return a list of non-overlapped rectangle boxes on the image
##########
def FindRectangle(img):
        ret, thresh = cv2. threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        _, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = (sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True))[1:]
        no_overlap_rects = []
        for cnt in contours:
                approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
                if (len(approx) >= 4):
                        rect = cv2.boundingRect(cnt)
                        x,y,w,h = rect
                        if (len(no_overlap_rects) == 0):
                                no_overlap_rects.append(rect)
                        else:
                                for i in range(len(no_overlap_rects)):
                                        xn, yn, wn, hn = no_overlap_rects[i]
                                        overlapped_in = ((x + w >= xn + wn) and (x <= xn) and (y <= yn) and (y + h >= yn))
                                        overlapped_out = ((xn + wn >= x + w) and (xn <= x) and (yn <= y) and (yn + hn >= y + h))
                                        if (overlapped_in):
                                                no_overlap_rects[i] = rect
                                                break
                                        elif (overlapped_out):
                                                break
                                        else:
                                                if (i == len(no_overlap_rects)-1):
                                                        no_overlap_rects.append(rect)
        return no_overlap_rects