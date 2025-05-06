import cv2
img=cv2.imread("images.jfif")
zoom_image=img[100:300,100:300]
cv2.imshow("Zommed Image",zoom_image)
cv2.waitKey(0)