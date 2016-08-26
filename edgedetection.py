import numpy as np
from matplotlib import pyplot as plt
import cv2

help_message = '''USAGE: custom_edge_detection.py [<image>]'''

def detect_edge(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    hist, bins = np.histogram(img_gray.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    hist_max_index = np.argmax(hist[25:200:1])
    hist_min_index = hist_max_index + np.argmin(hist[hist_max_index:hist_max_index + 50])

    img_gray[np.where(img_gray > hist_min_index)] = 255
    img_gray[np.where(img_gray <= hist_min_index)] = 0

    img_sobel = cv2.Sobel(img_gray, cv2.CV_32F, 1, 0)

    img_edge = np.zeros(img_gray.shape, dtype=np.uint8)
    img_edge[np.where(img_sobel > 1000)] = 255
    img_edge[np.where(img_sobel < -1000)] = 255

    cv2.imwrite("img_edge.png", img_edge)

    plt.figure()
    plt.imshow(img_sobel, cmap="gray")

    plt.figure()
    plt.imshow(img_edge, cmap="gray")

    plt.figure()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

    cv2.waitKey(0)

    cv2.destroyAllWindows()
    plt.close("all")




