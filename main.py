#!/usr/bin/env python
import numpy as np
import sys
from matplotlib import pyplot as plt

import cv2
import Image
import ImageDraw

from transformation import run_perspective_transform
# from cut_image import cut_image


# from edgedetection import detect_edge

point_count = 0
src = None

X = []
Y= []

ENTER = 1048586

# par1 = 0 -> Mouse move
# par1 = 1 -> Mouse down
# par1 = 4 -> Mouse up
# par 2 = x-coord
# par3 = y-coord
# par4 = ?
# par5 = userdata
"""
def pictures_layer(src):
    img_size = src.shape[0, 1]
    poly_size = (256, 256)
    poly_offset = (128, 128)
    back = Image.new('RGBA', img_size, (255, 0 , 0))
    poly = Image.new('RGBA', poly_size)
    pdraw = ImageDraw.Draw(poly)
    pdraw.polygon([ (0, 0), (256, 256), (0, 256)], fill=(255,255,255,127), outline= (255,255,255,255))
    back.paste(poly, poly_offset, mask=poly)
    back.show()
"""
"""
def callback_onMouse(par1, par2, par3, par4, par5): #par1 = event, par2 = x, par3 = y
    global point_count
    global src
    if par1 == cv2.EVENT_LBUTTONDOWN:#par1 == 1:
        #point_count += 1
        print("Point{2}: X:{0}; Y:{1}".format(par2, par3, point_count));
        #X.append(par2)
        #Y.append(par3)
	x = par2
	y = par3
	cv2.circle(src, (x, y), 30, (0, 0, 255), 5)
	cv2.imshow("Quelle", src)
        if point_count == 4:
            # cv2.line(src, (x[0], y[0]), (x[1], y[1]), (0, 0, 255), 1);
            # cv2.line(src, (x[1], y[1]), (x[2], y[2]), (0, 0, 255), 1);
            # cv2.line(src, (x[2], y[2]), (x[3], y[3]), (0, 0, 255), 1);
            # cv2.line(src, (x[3], y[3]), (x[0], y[0]), (0, 0, 255), 1);
            run_perspective_transform(X, Y, src)
            cv2.imshow("Quelle", src)
            print src.shape
            pass
        pass
    pass
"""

scaled = False
last_pos = (0, 0)

# Linkklick: Ausschnitt vergroessern
# Nochmal links: Ecke auswaehlen
# Oder: Rechtsklick: zur grossen Ansicht zurueck

# +++BUG+++ Wenn man zu weit aussen klickt, dann
# gehts nicht, weil der Array dann "out-of-range" ist.
# Man muss etwas weiter innen klicken, und so oft probieren
# bis die entsprechende Ecke sichtbar und somit klickbar ist!
def callback_onMouse(event, x, y, flags, param):
	global point_count
	global src
	global scaled
	global last_pos

	scale_width = 300;
	
	if event == cv2.EVENT_LBUTTONDOWN and scaled == False:
		scaled = True
		last_pos = (x, y)
		cropped = src[y-scale_width/2:y+scale_width/2, x-scale_width/2:x+scale_width/2]
		cv2.imshow("Quelle", cropped)
	elif event == cv2.EVENT_LBUTTONDOWN and scaled == True:
		scaled = False
		point_count += 1
		true_x = last_pos[0] + (x - scale_width/2)
		true_y = last_pos[1] + (y - scale_width/2)
		X.append(true_x)
		Y.append(true_y)
		print "Point ", point_count, true_x, true_y
		cv2.imshow("Quelle", src)
	elif event == cv2.EVENT_RBUTTONDOWN and scaled == True:
		scaled = False
		cv2.imshow("Quelle", src)	


	
	if point_count == 4:
	    # cv2.line(src, (x[0], y[0]), (x[1], y[1]), (0, 0, 255), 1);
	    # cv2.line(src, (x[1], y[1]), (x[2], y[2]), (0, 0, 255), 1);
	    # cv2.line(src, (x[2], y[2]), (x[3], y[3]), (0, 0, 255), 1);
	    # cv2.line(src, (x[3], y[3]), (x[0], y[0]), (0, 0, 255), 1);
	    run_perspective_transform(X, Y, src)
	    cv2.imshow("Quelle", src)
	    print src.shape
	    

	
            
        
    

if __name__ == "__main__":
    help_message = "USAGE: perspective_transform.py [<image>]\nSelect 4 Points in following order:\nupper-left, upper-right, bottom-right, bottom-left\nClose with 'Esc'\n"
    try:
        fn = sys.argv[1]
    except:
        print help_message
        exit()

    src = cv2.imread(fn, True)
    #original_src = src

    cv2.namedWindow("Quelle", cv2.WINDOW_NORMAL)
    cv2.imshow("Quelle", src)
    #pictures_layer(src)
    cv2.setMouseCallback("Quelle", callback_onMouse, "Hello World!")

    # cut_image(src)
    c = 0
    while c != ENTER:
        c = cv2.waitKey(0)
        print(c)
        pass
	 
    #recognize.recognize()



