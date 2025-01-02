from carParkingCounter import logger
from carParkingCounter.config.configuration import ConfigurationManager
from carParkingCounter.components.posfinder import PosFinder
import cv2
from box import ConfigBox

class PosFinderPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        posfinder_config = config.get_posfinder_config()
        posfinder = PosFinder(config=posfinder_config)
        # PosFinder.mouseClick()

        while True:
            image = cv2.imread(posfinder.config.image_dir)
            for pos in posfinder.posList:
                cv2.rectangle(
                    image,
                    (pos[0], pos[1]),
                    (
                        pos[0] + posfinder_config.box_width,
                        pos[1] + posfinder_config.box_height,
                    ),
                    (0, 255, 0),
                    1,
                )
            cv2.imshow("Image", image)
            cv2.setMouseCallback("Image", posfinder.mouseClick)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
