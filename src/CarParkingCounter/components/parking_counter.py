import cv2
import pickle
import os
from carParkingCounter.utils.common import load_pickle
from carParkingCounter.entity import PosFinderConfig
from pathlib import Path
from box import ConfigBox

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

    cap = cv2.VideoCapture("./Image_Video/video.mp4")    

    def checkparkingspace(self, preprocessed_frame):
        counter=0
        if len(posList)!= 0:

            for pos in posList:
                x, y = pos

                cropped_frame = preprocessed_frame[y:y+box_height, x:x+box_width]
                # cv2.imshow(str(x+y), cropped_frame
                count = cv2.countNonZero(cropped_frame)

                if count < 900:
                    counter+=1
                    color =(100, 255,100)
                else:
                    color = (100, 100, 255)

                cv2.rectangle(frame,(pos[0], pos[1]), (pos[0]+box_width, pos[1]+box_height), color, 2)
                cv2.putText(frame, str(count), (pos[0], pos[1]+5), 0, 0.5, [255,255,255], thickness=1, lineType =cv2.LINE_AA)
                cv2.rectangle(frame, (51,15), (51+box_width+100, 15+box_height), (255,0,255), cv2.FILLED)
                cv2.putText(
                    frame,
                    f"Free: {counter}/{len(posList)}",
                    (52, 10 + box_height),
                    0,1,
                    [255, 255, 255],
                    thickness=1,
                    lineType=cv2.LINE_AA,
                )
