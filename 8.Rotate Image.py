import cv2
img=cv2.imread("images.jfif")
img_90=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
img_180=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("90",img_90)
cv2.imshow("180",img_180)
cv2.waitKey(0)