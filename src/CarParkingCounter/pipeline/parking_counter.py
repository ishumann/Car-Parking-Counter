from carParkingCounter import logger
from carParkingCounter.config.configuration import ConfigurationManager
from carParkingCounter.components.parking_counter import  ParkingCounter
import cv2
from box import ConfigBox
from pathlib import Path
import numpy as np


class ParkingCounterPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        parking_counter_config = config.get_parking_counter_config()
        parking_counter = ParkingCounter(config=parking_counter_config)

        cap = cv2.VideoCapture(Path(parking_counter_config.video_dir))
        while True:
            #For Video loop
            # if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            #     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

            ret, frame = cap.read()

            if ret:
                # Convert our frame to gray scale
                gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Add Gaussian Blur
                blur = cv2.GaussianBlur(gray_scale, (3, 3), 1)

                # Applying threshold on each of the frame of the video

                frame_threshold = cv2.adaptiveThreshold(
                    blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
                )

                # To remove the noise dots ws will apply median blur

                median_blur = cv2.medianBlur(frame_threshold, 5)

                kernel = np.ones((3, 3), np.uint8)
                frame_dilate = cv2.dilate(median_blur, kernel, iterations=1)

                parking_counter.checkparkingspace(frame_dilate, frame)

                cv2.imshow("video", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        cap.release()
