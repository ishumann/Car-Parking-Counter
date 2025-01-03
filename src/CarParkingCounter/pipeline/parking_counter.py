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
        parking_counter.countemptyspace()
        