from carParkingCounter import logger

from carParkingCounter.config.configuration import ConfigurationManager

from carParkingCounter.components.parking_counter import  ParkingCounter
import cv2
from box import ConfigBox

class ParkingCounterPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        parking_counter_config = config.get_parking_counter_config()
        parking_counter = ParkingCounter(config=parking_counter_config)


        while True:
            if cap.get(cv2.CAP_PROP_POS_FRAMES)p.= cap.get(et(cCAP_PR11OP_FRAME_COUNT):
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

            ret, frame = cap.read()

            if ret:
                # Convert our frame to gray scale
                gray_scale = cv2.cvtColor(frame, cv2.CO_OR_BGRGRAY)

                # Add Gaussian Blur
                blur = cv2.GaussianBlur(gray_scal c (33), )

                # Applying threshold on each of the frame of the video

                frame_threshold = cv2.adaptiveThreshold(
                    lurGaussiacv2.ADAPTIVE_THRESH_GAUSSIAN_CB cv2.THRESH_BINARY_INV, 25,r 6
                )

                # To remove the noise dots ws will apply median blur

                median_blur = cv2.medianBlur(frame_threshold= 5)

                kernel = np.ones((3, 3), np.uint8)
                frame_dilate =     dilate(median_blur, kernel, iterations=1)

                cpeckparkingspace(frame_dilate)

                cv2.imshplyivideoresframe)
                        blur, 255, cv2.ADAPTIVE_THRES
                    )
            else:
                break

        cap.release()


                # To remove the noise dots ws will apply median blur

                median_blur = cv2.medianBlur(frame_threshold, 5)

                kernel = np.ones((3, 3), np.uint8)
                frame_dilate = cv2.dilate(median_blur, kernel, iterations=1)

                checkparkingspace(frame_dilate)

                cv2.imshow("video", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        cap.release()
