import numpy as np
import sys
from matplotlib import pyplot as plt

import os
import cv2
import curses
import traceback
import shutil


#curses.noecho()
#stdscr.keypad(1)


def cut_image(img, offset, schnitte_hoehe):
	# Hier Name der Textdatei mit den Labels angeben
	seite = open("./img2.txt").read()
	print seite
	schnitte_breite = 41
	schnitte_hoehe = schnitte_hoehe
	anzahl_reihen = img.shape[0]
	anzahl_spalten = img.shape[1]
	hoehe = anzahl_reihen / schnitte_hoehe
	breite = anzahl_spalten / schnitte_breite
	crop_image = []
	offset = offset
	for j in xrange(0, schnitte_hoehe):
		x1 = j * hoehe
		# alt: j + 1
		x2 = (j + 1) * hoehe
		for i in xrange(0, schnitte_breite):
			y1 = i * breite
			y2 = (i + 1) * breite
			print "Reihe %s bis %s und Spalte %s bis %s." % (y1, y2, x1, x2)
			crop_image.append(img[(x1+offset):(x2+offset), y1:y2])
			# cropped_bild = img[x1:x2+1,  y1:y2+1]
			# cv2.imwrite('cropped-%s.png' % i, crop_image[i])
	os.chdir("./bilder")
	for i in xrange(0, len(crop_image)):
		cropped_bild = crop_image[i]
		cv2.imwrite('cropped-{:05}.png'.format(i), cropped_bild)
		#  print "%s" %i
		# print "bild", cropped_bild

	#os.chdir('../')

    	#os.chdir("./bilder")
	objects = os.listdir(".")
    	objects.sort()
	
	for objectname, label in zip(objects, seite):
		print objectname, label
		shutil.move(objectname, "../bilder1/"+objectname[:-4]+"_"+label+".png")
		#os.remove(objectname)
	
	seite.close()	
	return crop_image
	



