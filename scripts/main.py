import cv2
import numpy as np

import pickle


box_width = 108
box_height = 47

with open('carparkpos', 'rb') as f:
    posList = pickle.load(f)
    
cap = cv2.VideoCapture("./Image_Video/video.mp4")    
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    ret, frame = cap.read()
    
    if ret:
        # Convert our frame to gray scale
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Add Gaussian Blur
        blur = cv2.GaussianBlur(gray_scale, (3,3), 1)
        
        # Applying threshold on each of the frame of the video
        
        frame_threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
        
        
        # To remove the nise dots ws will apply median blur
        
        median_blur = cv2.medianBlur(frame_threshold, 5)
        
        
        
        
        
        
        
        cv2.imshow("video", frame_threshold)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break
    
cap.release()


    