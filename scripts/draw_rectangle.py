
import cv2

# cap = cv2.VideoCapture(r".\Image_Video\video.mp4")
image = cv2.imread(r".\Image_Video\image.png")


while True:
    cv2.rectangle(image, (33, 89), (156, 146), (0, 255, 0), 1)
    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

