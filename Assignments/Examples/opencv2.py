import numpy as np
import cv2

# Create a black image
img = np.zeros((1000,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),20)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
