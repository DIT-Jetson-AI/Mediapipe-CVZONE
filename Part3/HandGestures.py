import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
import cvzone

cap = cv2.VideoCapture(1)
detectorHand = HandDetector(maxHands=1)
detectorFace = FaceDetector()
gesture = ""

while True:
    _, img = cap.read()
    img = detectorHand.findHands(img)
    lmList, bboxInfo = detectorHand.findPosition(img)

    # Face 보이지 않게함 : False
    img, bboxs = detectorFace.findFaces(img, draw=False)

    if bboxs:
        x, y, w, h = bboxs[0]["bbox"]
        bboxRegion = x - 175 - 25, y - 75, 175, h + 75
        cvzone.cornerRect(img, bboxRegion, rt=0, t=10, colorC=(0, 0, 255))

    if lmList and detectorHand.handType() == "Right":

        handCenter = bboxInfo["center"]
        #       x < cx < x+w
        inside = bboxRegion[0] < handCenter[0] < bboxRegion[0] + bboxRegion[2] and \
                 bboxRegion[1] < handCenter[1] < bboxRegion[1] + bboxRegion[3]

        if inside:
            cvzone.cornerRect(img, bboxRegion, rt=0, t=10, colorC=(0, 255, 0))

            fingers = detectorHand.fingersUp()
            # print(fingers)

            if fingers == [0, 1, 0, 0, 0]:
                gesture = "Light1 ON"
            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "Light2 ON"
            elif fingers == [0, 0, 1, 1, 1]:
                gesture = "Light3 ON"
            elif fingers == [0, 0, 0, 0, 0]:
                gesture = "Light OFF"
            else:
                gesture = ""

            # elif fingers == [1, 1, 0, 0, 1]:
            #     gesture = "SpiderMan"
            # elif fingers == [0, 1, 1, 0, 0]:
            #     gesture = " Victory"
            # elif fingers == [0, 0, 0, 0, 1]:
            #     gesture = "  Pinky"
            # elif fingers == [1, 0, 0, 0, 0]:
            #     gesture = "  Thumb"

            # if fingers == [1, 1, 1, 1, 1]:
            #     gesture = "  Open"
            # elif fingers == [0, 1, 0, 0, 0]:
            #     gesture = "  Index"
            # elif fingers == [0, 0, 0, 0, 0]:
            #     gesture = "  Fist"
            # elif fingers == [0, 0, 1, 0, 0]:
            #     gesture = "  Middle"
            # elif fingers == [1, 1, 0, 0, 1]:
            #     gesture = "SpiderMan"
            # elif fingers == [0, 1, 1, 0, 0]:
            #     gesture = " Victory"
            # elif fingers == [0, 0, 0, 0, 1]:
            #     gesture = "  Pinky"
            # elif fingers == [1, 0, 0, 0, 0]:
            #     gesture = "  Thumb"

            if gesture != "":
                cv2.rectangle(img, (bboxRegion[0], bboxRegion[1] + bboxRegion[3] + 10),
                              (bboxRegion[0] + bboxRegion[2], bboxRegion[1] + bboxRegion[3] + 60),
                              (0, 255, 0),cv2.FILLED)

                cv2.putText(img, f'{gesture}',
                            (bboxRegion[0] + 10, bboxRegion[1] + bboxRegion[3] + 50),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from cvzone.FaceDetectionModule import FaceDetector
# import cvzone
#
# cap = cv2.VideoCapture(1)
# detectorHand = HandDetector(maxHands=1)
# detectorFace = FaceDetector()
# gesture = ""
#
# while True:
#     _, img = cap.read()
#     img = detectorHand.findHands(img)
#     lmList, bboxInfo = detectorHand.findPosition(img)
#     # img, bboxs = detectorFace.findFaces(img, draw=True)
#     # bboxs = detectorFace.findFaces(img, draw=True)
#
#     if bboxs:
#         x, y, w, h = bboxs[0]["bbox"]
#         bboxRegion = x - 175 - 25, y - 75, 175, h + 75
#         cvzone.cornerRect(img, bboxRegion, rt=0, t=10, colorC=(0, 0, 255))
#
#         if lmList and detectorHand.handType() == "Right":
#
#             handCenter = bboxInfo["center"]
#             #       x < cx < x+w
#             inside = bboxRegion[0] < handCenter[0] < bboxRegion[0] + bboxRegion[2] and \
#                      bboxRegion[1] < handCenter[1] < bboxRegion[1] + bboxRegion[3]
#
#             if inside:
#                 cvzone.cornerRect(img, bboxRegion, rt=0, t=10, colorC=(0, 255, 0))
#
#                 fingers = detectorHand.fingersUp()
#                 # print(fingers)
#
#                 if fingers == [1, 1, 1, 1, 1]:
#                     gesture = "  Open"
#                 elif fingers == [0, 1, 0, 0, 0]:
#                     gesture = "  Index"
#                 elif fingers == [0, 0, 0, 0, 0]:
#                     gesture = "  Fist"
#                 elif fingers == [0, 0, 1, 0, 0]:
#                     gesture = "  Middle"
#                 elif fingers == [1, 1, 0, 0, 1]:
#                     gesture = "SpiderMan"
#                 elif fingers == [0, 1, 1, 0, 0]:
#                     gesture = " Victory"
#                 elif fingers == [0, 0, 0, 0, 1]:
#                     gesture = "  Pinky"
#                 elif fingers == [1, 0, 0, 0, 0]:
#                     gesture = "  Thumb"
#
#                 cv2.rectangle(img, (bboxRegion[0], bboxRegion[1] + bboxRegion[3] + 10),
#                               (bboxRegion[0] + bboxRegion[2], bboxRegion[1] + bboxRegion[3] + 60),
#                               (0, 255, 0),cv2.FILLED)
#
#                 cv2.putText(img, f'{gesture}',
#                             (bboxRegion[0] + 10, bboxRegion[1] + bboxRegion[3] + 50),
#                             cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
#
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
#
