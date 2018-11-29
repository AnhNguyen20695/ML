from CNN_Model.mnist_classifier1 import mnist_classifier
import tensorflow as tf
import numpy as np
import cv2 as cv

#########
# Function to predict a single number
# Input image should be in grayscale
#########
def predict_img(im, iwhite_background):
    if iwhite_background:
        imarr = np.asarray(255-im, dtype=np.float32)
    else:
        imarr = np.asarray(im, dtype=np.float32)

    imarr = imarr / 255.0
    pred_data_fn = tf.estimator.inputs.numpy_input_fn(
        x = {"x": imarr}, shuffle=False)
    result = next(mnist_classifier.predict(
                    input_fn= pred_data_fn
                ))
    result_class = result['classes']
    result_prob = result['probabilities']
    if (result_prob[result_class] >= 0.4):
        print("There is a {}% chance that the image displays number {}".format(
                str(round(result_prob[result_class] * 100, 2)), 
                str(result_class))
        ) 
    else:
        print("This may not be a number")
    return result_class, result_prob[result_class]
    # print(result_prob)
    # cv.imshow('{}'.format(result['classes']), imarr)
    # else:
        # print("Input is not a digit.")
        # cv.imshow('{}'.format(result['classes']), imarr)
#########