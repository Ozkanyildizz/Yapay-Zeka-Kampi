
# Read images-videos-webcam

import cv2


# Fotoğraf yükleme
"""
img=cv2.imread('Resources/lena.png')

cv2.imshow( 'output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

# video yükleme
"""
cap = cv2.VideoCapture("resources/video.mp4")
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # stop if pres a button
        break"""

# wabcam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100) # brightness
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # stop if pres a button
        break