#!/usr/bin/env python

import sys
import cv2
import numpy as np
import cut_image as ct

point_count = 0
x = input("Hoehe Patches?")
y = input ("Breite Patches?")
schnitte_hoehe = input("Wie viele Reihen?")
x1 = x * schnitte_hoehe
y1 = y * 41
offset = raw_input("offset?(j/n)")
if offset == 'j':
    a = input("Wie viel Offset? (2 = Mitte)")
    offset1 = x1 / (a*schnitte_hoehe)
elif offset == 'n':
    offset1 = 0
else:
    offset1 = 0
def run_perspective_transform(x,y, src):
    src_quad = np.array([(x[0], y[0]), (x[1], y[1]), (x[2], y[2]), (x[3], y[3])], np.float32)
    dst_quad = np.array([(0.0, 0.0), (y1, 0.0), (y1, x1), (0.0, x1)], np.float32)
    transf_matr = cv2.getPerspectiveTransform(src_quad, dst_quad)  # src, dst,
    transf_img = cv2.warpPerspective(src, transf_matr, (y1, x1))
    print  transf_matr

    cv2.imwrite('pers_t.jpg', transf_img)

    cv2.namedWindow("Transformiert", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Transformiert", transf_img)

    #grau = cv2.cvtColor(transf_img, cv2.COLOR_BGR2GRAY)
    #cannyImg = cv2.Canny(grau, 50, 150, 3)

    #cv2.namedWindow("Canny", cv2.WINDOW_AUTOSIZE)
    #cv2.imshow("Canny", cannyImg)

    ct.cut_image(transf_img, offset1, schnitte_hoehe)
