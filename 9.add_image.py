import cv2
img1=cv2.imread("images.jfif")
img2=cv2.imread("download.jpg")
img2=cv2.resize(img2,(img1.shape[1],img1.shape[0]))
added_image=cv2.add(img1,img2)
cv2.imshow("Added Image",added_image)
cv2.waitKey(0)