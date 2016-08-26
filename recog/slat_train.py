from __future__ import absolute_import, division, print_function


#import tensorflow as tf
#import tflearn
import cv2
import glob
import dnn1_bw as net
import classify

X = []
Y = []

#
# Function for loading images and creating label-vector Y based on image names
# color = Load image as color or grayscale. 0 : grayscale, default: 1 (color)
#
def load_images(X, path, color = 1):
	global Y
	pictures = sorted(glob.glob(path+"/*.png")) # this is a list of all png files
	for pic in pictures:
		X.append(cv2.imread(pic, color))
		slat = pic[len(pic)-5]
		if slat == "l":
			Y.append([1,0,0])
		if slat == "m":
			Y.append([0,1,0])
		if slat == "r":
			Y.append([0,0,1])

	return pictures



	
#
# Load cropped images and correct output values
#
'''
load_images(X, "./NO_OFFSET/cropped0")

load_images(X, "./NO_OFFSET/cropped1")

load_images(X, "./NO_OFFSET/cropped2")

load_images(X, "./NO_OFFSET/cropped3")

load_images(X, "./NO_OFFSET/cropped4")

load_images(X, "./NO_OFFSET/cropped_img2")

load_images(X, "./NO_OFFSET/cropped_img2_bw")

load_images(X, "./NO_OFFSET/cropped_dsc0202")

load_images(X, "./NO_OFFSET/cropped_dsc0248")

load_images(X, "./NO_OFFSET/cropped_dsc0249")
'''
'''
load_images(X, "./NO_OFFSET/cropped0")

load_images(X, "./NO_OFFSET/cropped1")

load_images(X, "./NO_OFFSET/cropped2")

load_images(X, "./NO_OFFSET/cropped3")

load_images(X, "./NO_OFFSET/cropped4")

load_images(X, "./NO_OFFSET/cropped_img2")

load_images(X, "./NO_OFFSET/cropped_img2_bw")

load_images(X, "./NO_OFFSET/cropped_dsc0202")
'''

# OFFSET
'''
load_images(X, "./OFFSET/img1_1")
load_images(X, "./OFFSET/img1_2")
load_images(X, "./OFFSET/img1_3")

load_images(X, "./OFFSET/img2_1")
load_images(X, "./OFFSET/img2_2")
load_images(X, "./OFFSET/img2_3")
load_images(X, "./OFFSET/img2_4")
'''
# OFFSET + BW

#load_images(X, "./OFFSET/img1_1", 0)
#load_images(X, "./OFFSET/img1_2", 0)
#load_images(X, "./OFFSET/img1_3", 0)

load_images(X, "./OFFSET/img2_1", 0)
#load_images(X, "./OFFSET/img2_2", 0)
#load_images(X, "./OFFSET/img2_3", 0)

#load_images(X, "./OFFSET/img2_4", 0)
#load_images(X, "./OFFSET/img2_5", 0)
#load_images(X, "./OFFSET/img4_1", 0)
#load_images(X, "./OFFSET/img4_2", 0)




# NO OFFSET
'''
load_images(X, "./NO_OFFSET/img1_1")
load_images(X, "./NO_OFFSET/img1_2")
load_images(X, "./NO_OFFSET/img1_3")

load_images(X, "./NO_OFFSET/img2_1")
load_images(X, "./NO_OFFSET/img2_2")
load_images(X, "./NO_OFFSET/img2_3")
load_images(X, "./NO_OFFSET/img2_4")
'''
"""
#file = open("lmr.txt", "r")
#lmr = file.read()
#for c in lmr:
#	if c == "l":
#		Y.append([1,0,0])
#	if c == "m":
#		Y.append([0,1,0])
#	if c == "r":
#		Y.append([0,0,1])

#file.close()
"""
	
print (len(X))
print (len(Y))

# Load existing model
net.m.load("dnn1_offset_bw.tfl")

#
# TRAINING
#
net.m.fit(X, Y, validation_set=0.2, n_epoch=50, snapshot_epoch=False, show_metric=True)

# Save model
net.m.save("dnn1_offset_bw.tfl")

#
# TESTING
#
'''
test = []
picture_path_list = load_images(test, "./NO_OFFSET/img1_1")
#picture_path_list = load_images(test, "./NO_OFFSET/cropped_img2")

# Falls Testbilder korrekte label enthalten: Vierter Parameter = True; sonst False (Achtung: es wird wirklich "False", bzw. "True" geschrieben)
classify.classify(net, test, picture_path_list, True)
'''
