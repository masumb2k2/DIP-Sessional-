import cv2
img=cv2.imread("images.jfif")
gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret,thresh=cv2.threshold(gray_image,70,255,0)
cv2.imshow("Binary Image",thresh)
cv2.waitKey(0)