import cv2
img=cv2.imread("images.jfif")
cv2.rectangle(img,(50,50),(200,150),(0,255,0),3)
cv2.imshow("Image With Rectangle",img)
cv2.waitKey(0)