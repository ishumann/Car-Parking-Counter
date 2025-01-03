import cv2
import pickle
import os
from carParkingCounter.utils.common import load_pickle
from carParkingCounter.entity import ParkingCounterConfig
from pathlib import Path
from box import ConfigBox
import numpy as np
# box_width = 108
# box_height = 47


class ParkingCounter:
    def __init__(self, config: ParkingCounterConfig):
        self.config = config
        try:
            self.posList = load_pickle(Path(self.config.pickle_dir))
        except:
            self.posList = []

        # with open('carparkpos', 'rb') as f:
        #     posList = pickle.load(f)

    def checkparkingspace(self, preprocessed_frame, frame):
        counter=0
        if len(self.posList) != 0:

            for pos in self.posList:
                x, y = pos

                cropped_frame = preprocessed_frame[
                    y : y + self.config.box_height, x : x + self.config.box_width
                ]
                # cv2.imshow(str(x+y), cropped_frame
                count = cv2.countNonZero(cropped_frame)

                if count < 900:
                    counter+=1
                    color =(100, 255,100)
                else:
                    color = (100, 100, 255)

                cv2.rectangle(
                    frame,
                    (pos[0], pos[1]),
                    (pos[0] + self.config.box_width, pos[1] + self.config.box_height),
                    color,
                    2,
                )
                cv2.putText(frame, str(count), (pos[0], pos[1]+5), 0, 0.5, [255,255,255], thickness=1, lineType =cv2.LINE_AA)
                cv2.rectangle(frame, (51,15), (51+self.config.box_width+100, 15+self.config.box_height), (255,0,255), cv2.FILLED)
                cv2.putText(
                    frame,
                    f"Free: {counter}/{len(self.posList)}",
                    (52, 10 + self.config.box_height),
                    0,
                    1,
                    [255, 255, 255],
                    thickness=1,
                    lineType=cv2.LINE_AA,
                )

    def save_video_out(self, cap):
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        fourcc = cv2.VideoWriter_fourcc(*"hvc1")  # Codec for .mp4 files
        out = cv2.VideoWriter(Path(self.config.video_write_dir), fourcc, fps, (frame_width, frame_height))
        return out

    def countemptyspace(self):
        cap = cv2.VideoCapture(Path(self.config.video_dir))
        out = self.save_video_out(cap)
        while True:
            # For Video loop
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
                    blur,
                    255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY_INV,
                    25,
                    16,
                )

                # To remove the noise dots ws will apply median blur

                median_blur = cv2.medianBlur(frame_threshold, 5)

                kernel = np.ones((3, 3), np.uint8)
                frame_dilate = cv2.dilate(median_blur, kernel, iterations=1)

                self.checkparkingspace(frame_dilate, frame)

                cv2.imshow("video", frame)
                # Write the processed frame to the output video
                processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                out.write(cv2.cvtColor(processed_frame, cv2.COLOR_GRAY2BGR))
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
