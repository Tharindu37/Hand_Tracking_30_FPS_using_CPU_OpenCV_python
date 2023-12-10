import cv2

# load image
# img = cv2.imread("126315265.png")
# cv2.imshow("Programming-Stack", img)
# cv2.waitKey(0)

# load video
# video = cv2.VideoCapture("AS2020913.mp4")
# while True:
#     success, img = video.read()
#     cv2.imshow("Bus Trackig System", img)
#     if cv2.waitKey(1) & 0xFF == ord('s'):
#         break

# open camera
video = cv2.VideoCapture(0)
while True:
    success, img = video.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
