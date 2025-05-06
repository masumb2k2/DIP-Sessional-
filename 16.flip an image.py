import cv2
img=cv2.imread("images.jfif")
flip_horizontal=cv2.flip(img,0)
flip_Vertical=cv2.flip(img,1)
cv2.imshow("Horizontal",flip_horizontal)
cv2.imshow("Vertical",flip_Vertical)
cv2.waitKey(0)