import cv2
img=cv2.imread("images.jfif")
gray_image=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray Image",gray_image)
cv2.waitKey(0)