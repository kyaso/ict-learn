from __future__ import absolute_import, division, print_function

import tensorflow as tf
import tflearn
import numpy as np
import shutil
from time import strftime
import os
import decoder


#
# Function which returns score based on probability
# 40% < : -
# 50% - 75% : +
# > 75% : +++
#
def confidence_score(p):
	if(p >= 0.75):
		return " +++"
	if(p > 0.5 and p < 0.75):
		return " +"
	if(p < 0.4):
		return " -"

	return " "

#
# Create the result folder
#
def setup_result_folder():
	time_string = strftime("%d-%m-%Y %H:%M:%S")
	result_folder = "./result"+time_string
	os.makedirs(result_folder)
	return result_folder
#
# If correct labels of test images are available: with_labels = True; else False
#
def classify(dnn, images, picture_path_list, with_labels = True):
	result_string = ""	
	result_folder = setup_result_folder()
	# Open text file (if it does not exit, it will be created, else overwritten)
	result_text = open(result_folder+"/result"+result_folder[8:]+".txt", "w")
	result_text.write(result_folder[8:]+"\n")

	# Predict labels of test images
	predictions = dnn.m.predict(images)
	
	if(with_labels == True):	
		wrong = 0 # Counter for wrong predictions
		# These arrays hold tuples: (label, slat, prediction_value, image index)
		wrongs = []
		correct = []
	i = -1
	# Copy test images with predicted labels to result folder
	for prediction, pic_path in zip(predictions, picture_path_list):
		i=i+1	
		label = "" # Predicted label
		prediction_value = 0 # Prediction probability

		if(with_labels == True):
			slat = pic_path[len(pic_path)-5] # Correct label (slat)

		# argmax returns index of maximum value
		if(np.argmax(prediction)) == 0:
			label = 'l'
			prediction_value = prediction[0]
		if(np.argmax(prediction)) == 1:
			label = 'm'
			prediction_value = prediction[1]
		if(np.argmax(prediction)) == 2:
			label = 'r'
			prediction_value = prediction[2]

		if(with_labels == True):
			# Check if prediction was right
			if(slat != label):
				wrong = wrong + 1
				wrongs.append((label, slat, prediction_value, i)) # i = current image number
			else:
				correct.append((label, slat, prediction_value, i))
		
			# Copy test image i with correct and predicted label in file name to result_folder
			shutil.copy(pic_path, result_folder+"/prediction_"+str(i)+"_"+slat+"_"+label+".png")
		else:
			# Copy test image i with predicted label in file name to result folder
			shutil.copy(pic_path, result_folder+"/prediction_"+str(i)+"_"+label+".png")
			# Write details to result text file
			result_text.write(str(i) + " Prediction: " + label + " , Prob: " + str(prediction_value) + confidence_score(prediction_value) + "\n")

		print("Copied ", pic_path, " to " + result_folder)

		# Append predicted label to lmr-string
		result_string = result_string + label

	# If correct labels exist: Write detailed data to result text file
	if(with_labels == True):
		score = ((len(images) - wrong)/len(images)) * 100
		result_text.write("Score: " + str(score) + "%" + " (" + str(len(images)-wrong) + "/" + str(len(images)) + ")\n\n")

		# a[0] = predicted label
		# a[1] = correct label (slat)
		# a[2] = prediction percentage
		# a[3] = image number/index
		result_text.write("=== WRONG ===\n")
		for a in wrongs:
			result_text.write("X " + str(a[3]) + " Prediction: " + a[0] + " , Correct: " + a[1] + " , Prob: " + str(a[2]) + confidence_score(a[2]) + "\n")

		result_text.write("\n=== CORRECT ===\n")

		for a in correct:
			result_text.write("O " + str(a[3]) + " Prediction: " + a[0] + " , Correct: " + a[1] + " , Prob: " + str(a[2]) + confidence_score(a[2]) + "\n")

	# Close text file
	result_text.close()

	print(result_string)
	decoder.decode(result_string)
	

# Classify and decode without copying pictures to a result folder
def classify_decode(dnn, images):
	result_string = ""
	predictions = dnn.m.predict(images) # Predict labels of test images
	i=0
	
	# Copy test images with predicted labels to result folder
	for prediction in predictions:
		i=i+1	
		label = "" # predicted label
		prediction_value = 0

		# argmax returns index of maximum value
		if(np.argmax(prediction)) == 0:
			label = 'l'
			prediction_value = prediction[0]
		if(np.argmax(prediction)) == 1:
			label = 'm'
			prediction_value = prediction[1]
		if(np.argmax(prediction)) == 2:
			label = 'r'
			prediction_value = prediction[2]


		result_string = result_string + label

	print(result_string+"\n")
# Da der Online-Decoder eh besser ist, brauchen wir hier keinen ;)
'''
	for i in range(0,10):	
		print(decoder.decode(result_string[i:]) + "\n")
'''







#
# OLD FUNCTION
#

'''
#
# If correct labels of test images are not available, use this function
#
def classify_without_labels(dnn, images, picture_path_list):
	result_string = ""
	result_folder = setup_result_folder()
	result_text = open(result_folder+"/result"+result_folder[8:]+".txt", "w") # open text file (if it does not exit, it will be created, else overwritten)
	result_text.write(result_folder[8:]+"\n")
	predictions = dnn.m.predict(images) # predict labels of test images
	i=0
	
	# Copy test images with predicted labels to result folder
	for prediction, pic_path in zip(predictions, picture_path_list):
		i=i+1	
		label = "" # predicted label
		prediction_value = 0

		# argmax returns index of maximum value
		if(np.argmax(prediction)) == 0:
			label = 'l'
			prediction_value = prediction[0]
		if(np.argmax(prediction)) == 1:
			label = 'm'
			prediction_value = prediction[1]
		if(np.argmax(prediction)) == 2:
			label = 'r'
			prediction_value = prediction[2]


		# copy test image i with predicted label in file name to result folder
		shutil.copy(pic_path, result_folder+"/prediction_"+str(i)+"_"+label+".png")
		result_text.write(str(i) + " Prediction: " + label + " , Prob: " + str(prediction_value) + confidence_score(prediction_value) + "\n")
		print("Copied ", pic_path, " to result")
		result_string = result_string + label


	result_text.close()
	print(result_string)
'''



