import cv2
img=cv2.imread("images.jfif")
brithness_level=70
bright_image=cv2.convertScaleAbs(img,alpha=1,beta=brithness_level)
cv2.imshow("Brithhness Level",bright_image)
cv2.waitKey(0)