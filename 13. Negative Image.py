import cv2
img=cv2.imread("images.jfif")
negative_image=255-img
cv2.imshow("Negative Image",negative_image)
cv2.waitKey(0)