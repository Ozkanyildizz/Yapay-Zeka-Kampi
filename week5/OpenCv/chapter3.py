
# Resizing and Cropping

import  cv2

img = cv2.imread('Resources/lena.png', cv2.IMREAD_COLOR)
print(img.shape) # (h,w,bgr)

# Resizing image
imgResized = cv2.resize(img, (600,450))
print(imgResized.shape)

# cropping image
imgCropped = imgResized[0:500,100:500]

cv2.imshow('Img', img)
cv2.imshow('Resized', imgResized)
cv2.imshow('Cropped', imgCropped)

cv2.waitKey(0)