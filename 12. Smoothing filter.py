import cv2
img=cv2.imread("images.jfif")
mean_filtered=cv2.blur(img,(5,5))
median_filtered=cv2.medianBlur(img,5)
cv2.imshow("mean",mean_filtered)
cv2.imshow("median",median_filtered)
cv2.waitKey(0)