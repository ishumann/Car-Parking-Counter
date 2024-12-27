import cv2
import pickle

box_width = 108
box_height = 47
# cap = cv2.VideoCapture(r".\Image_Video\video.mp4")
# image = cv2.imread(r".\Image_Video\image.png")
try:
    with open('carparkpos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if (x1 < x < (x1 + box_width)) and (y1 < y < (y1 + box_height)):
                del posList[i]
                break

    with open("carparkpos", 'wb') as f:
        pickle.dump(posList, f)
        # pass




while True:
    image = cv2.imread(r".\Image_Video\image.png")
    for pos in posList:
        cv2.rectangle(image, (pos[0], pos[1]), (pos[0] + box_width, pos[1] + box_height), (0, 255, 0), 1)
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouseClick)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
