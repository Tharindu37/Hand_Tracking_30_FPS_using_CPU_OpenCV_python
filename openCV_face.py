import cv2

# load Cascade file
face = cv2.CascadeClassifier(
    "haar-cascade-files-master\haarcascade_frontalface_default.xml")

# load Image
img = cv2.imread("audience-citizen_0.jpg")

# convert to black & white
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face
detect = face.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in detect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# show image
cv2.imshow("image", img)
cv2.waitKey(0)
