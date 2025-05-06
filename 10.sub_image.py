import cv2
img1=cv2.imread("images.jfif")
img2=cv2.imread("download.jpg")
img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
Subtract_image=cv2.subtract(img1,img2)
cv2.imshow("Subtracted Image",Subtract_image)
cv2.waitKey(0)