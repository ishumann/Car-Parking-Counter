import cv2
import numpy as np

import pickle


box_width = 108
box_height = 47

with open('carparkpos', 'rb') as f:
    posList = pickle.load(f)

cap = cv2.VideoCapture("./Image_Video/video.mp4")    

def checkparkingspace(preprocessed_frame):
    if len(posList)!= 0:
    
        for pos in posList:
            x, y = pos

            cropped_frame = preprocessed_frame[y:y+box_height, x:x+box_width]
            # cv2.imshow(str(x+y), cropped_frame
            count = cv2.countNonZero(cropped_frame)
            cv2.rectangle(frame,(pos[0], pos[1]), (pos[0]+box_width, pos[1]+box_height), (255,100, 100), 2)
            cv2.putText(frame, str(count), (pos[0], pos[1]+5), 0, 0.5, [255,255,255], thickness=1, lineType =cv2.LINE_AA)


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

        # To remove the noise dots ws will apply median blur

        median_blur = cv2.medianBlur(frame_threshold, 5)

        kernel = np.ones((3,3), np.uint8)
        frame_dilate = cv2.dilate(median_blur, kernel, iterations=1)

        checkparkingspace(frame_dilate)

        cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break

cap.release()