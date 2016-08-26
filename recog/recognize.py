from __future__ import absolute_import, division, print_function


import cv2
import glob
import dnn1_bw as net
import classify

X = []

#
# Function for loading images and creating label-vector Y based on image names
#
def load_images(X, path, color = 1):
	pictures = sorted(glob.glob(path+"/*.png")) # this is a list of all png files
	for pic in pictures:
		img = cv2.imread(pic, color)
		if(color == 1):
			if img.shape == (50,25, 3):
				X.append(img)
			else:
				break
		elif(color == 0):
			if img.shape == (50,25):
				X.append(img)
			else:
				break
	'''
		slat = pic[len(pic)-5]
		if slat == "l":
			Y.append([1,0,0])
		if slat == "m":
			Y.append([0,1,0])
		if slat == "r":
			Y.append([0,0,1])
	'''

	print(len(X))
	return pictures




# Load model
net.m.load('dnn1_offset_bw.tfl')

#
# TESTING
#
test = []
picture_path_list = load_images(test, "../bilder1", 0) # The test folder; 0 = black & white

# Falls Testbilder korrekte label enthalten: Vierter Parameter = True; sonst False (Achtung: es wird wirklich "False", bzw. "True" geschrieben)
classify.classify(net, test, picture_path_list, True)
