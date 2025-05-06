import cv2
img=cv2.imread("images.jfif")
resize_image=cv2.resize(img,(400,600))
cv2.imshow("Resized Image",resize_image)
cv2.waitKey(0)