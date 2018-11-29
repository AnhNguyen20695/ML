import numpy as np
#########
# Return the total number of white pixels in a thresh image
#########

def CountWhitePixel(img):
    return img[img == 255].sum()