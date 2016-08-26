from __future__ import absolute_import, division, print_function


import tensorflow as tf
import tflearn

input = tflearn.input_data(shape=[None, 50, 25])
hidden = tflearn.fully_connected(input, 512, activation='tanh')
output = tflearn.fully_connected(hidden, 3, activation='softmax')
regression = tflearn.regression(output, optimizer='sgd', 
				learning_rate=0.0001, 
				loss='categorical_crossentropy')

# with offset (Pfad anpassen!)
#m = tflearn.DNN(regression, tensorboard_dir='/home/kyaso/bildererkennen/bildererkennen_final/dnn1_logs')

# no offset (Pfad anpassen!)
#m = tflearn.DNN(regression, tensorboard_dir='/home/kyaso/bildererkennen/bildererkennen_final/dnn1_offset_logs')

#m = tflearn.DNN(regression)
m = tflearn.DNN(regression)
