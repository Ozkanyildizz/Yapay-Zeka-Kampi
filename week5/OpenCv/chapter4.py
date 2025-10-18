
# Shapes and Texts

import  cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

# coloring
"""
img[:] = 255,0,0
img[100:300] = 255,255,255
"""

#line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,255,255),2)
#rectangle
cv2.rectangle(img,(0,0),(250,300),(255,0,255),2)
#circels
cv2.circle(img,(250,250),100,(255,215,255),2)
#tesxt
cv2.putText(img,"OpenCV ",(150,100),cv2.FONT_HERSHEY_COMPLEX,2,255,2)

cv2.imshow('img', img)
cv2.waitKey(0)