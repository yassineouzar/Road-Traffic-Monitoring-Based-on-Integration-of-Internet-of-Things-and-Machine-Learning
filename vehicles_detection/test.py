#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports
import numpy as np
import os
#import six.moves.urllib as urllib
import sys
#import tarfile
import tensorflow as tf
#import zipfile
import cv2
import numpy as np
#import csv
import time

from matplotlib import pyplot as plt



# This is needed since the working directory is the object_detection folder.
sys.path.append('..')

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'ssdlite_mobilenet_v2_coco_2018_05_09'

# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'data','mscoco_label_map.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 90

# input video
cap = cv2.VideoCapture('a.mp4')
#cap = cv2.VideoCapture('surveillance.m4v')

# Variables
total_passed_vehicle = 0  # using it to count vehicles

## Load the label map.

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Initialize frame rate calculation
frame_rate_calc = 250
freq = cv2.getTickFrequency()
font = cv2.FONT_HERSHEY_SIMPLEX
im_width = 640
im_height = 480
def load_image_into_numpy_array(image):
    return np.array(image.getdata()).reshape((im_height, im_width,
                3))

def object_detection_function():
    total_passed_vehicle=0
    

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:

            # Definite input and output Tensors for detection_graph
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

            # Each box represents a part of the image where a particular object was detected.
            detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
            detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            # for all the frames that are extracted from input video
            while(cap.isOpened()):

                (ret, frame) = cap.read()

                if not ret:
                    #print ('end of the video file...')
                    break
                input_frame = frame
                vehicle_detected=0
                

                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(input_frame, axis=0)

                # Actual detection.
                (boxes, scores, classes, num) = \
                    sess.run([detection_boxes, detection_scores,
                            detection_classes, num_detections],
                            feed_dict={image_tensor: image_np_expanded})
                vehicle_detected = num
		#print(vehicle_detected)
                total_passed_vehicle=vehicle_detected




                             
        # Draw the results of the detection (aka 'visulaize the results')
                vis_util.visualize_boxes_and_labels_on_image_array(
                    cap.get(1),
                    frame,                
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=8,
                    min_score_thresh=0.40)

                    
                # insert information text to video frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(
                    input_frame,
                    'Vehicles Detectes: ' + str(vehicle_detected),
                    (10, 35),
                    font,
                    0.8,
                    (0xFF, 0, 0),
                    2,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    )

                # when the vehicle passed over line and counted, make the color of ROI line green
                # if counter == 1:
                    # cv2.line(input_frame, (0, 200), (640, 200), (0, 0xFF, 0), 5)
                # else:
                    # cv2.line(input_frame, (0, 200), (640, 200), (0, 0, 0xFF), 5)

                # insert information text to video frame

                # cv2.putText(
                    # input_frame,
                    # 'Over Line',
                    # (545, 190),
                    # font,
                    # 0.6,
                    # (0, 0, 0xFF),
                    # 2,
                    # cv2.LINE_AA,
                    # )
                
                cv2.imshow('vehicle detection', input_frame)


                total_passed_vehicle=vehicle_detected+total_passed_vehicle
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.imshow('vehicle detection', input_frame)
                    break
                total_passed_vehicle=vehicle_detected+total_passed_vehicle
                
            cap.release
            
            cv2.destroyAllWindows()
            print(str(total_passed_vehicle))

object_detection_function()
