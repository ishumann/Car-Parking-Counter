import cv2
import pickle
import os
from carParkingCounter.utils.common import load_pickle, save_pickle
from carParkingCounter.entity import PosFinderConfig
from pathlib import Path
from box import ConfigBox

# box_width = 108
# box_height = 47
# cap = cv2.VideoCapture(r".\Image_Video\video.mp4")
# image = cv2.imread(r".\Image_Video\image.png")
class PosFinder:
    def __init__(self, config: PosFinderConfig):
        self.config = config
        try:
            self.posList =  load_pickle(Path(self.config.pickle_dir))
        except:
            self.posList = []
        # try:
        #     with open('carparkpos', 'rb') as f:
        #         posList = pickle.load(f)
        # except:
        #     posList = []

    def mouseClick(self, events, x, y, flags, params):
        if events == cv2.EVENT_LBUTTONDOWN:
            self.posList.append((x, y))

        if events == cv2.EVENT_RBUTTONDOWN:
            for i, pos in enumerate(self.posList):
                x1, y1 = pos
                if (x1 < x < (x1 + self.config.box_width)) and (y1 < y < (y1 + self.config.box_height)):
                    del self.posList[i]
                    break

        save_pickle(Path(self.config.pickle_dir), self.posList)
        # with open("carparkpos", 'wb') as f:
        #     pickle.dump(posList, f)
        #     # pass
