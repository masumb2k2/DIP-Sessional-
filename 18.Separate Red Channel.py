import cv2
img=cv2.imread("images.jfif")
red_channel=img[:,:,2]
cv2.imshow("Red Channel",red_channel)
cv2.waitKey(0)