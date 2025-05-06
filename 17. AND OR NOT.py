import cv2
img1 = cv2.imread('images.jfif')
img2 = cv2.imread('download.jpg')
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
and_img = cv2.bitwise_and(img1, img2)
or_img = cv2.bitwise_or(img1, img2)
not_img = cv2.bitwise_not(img1)
cv2.imshow('Bitwise AND', and_img)

cv2.imshow('Bitwise OR', or_img)
cv2.imshow('Bitwise NOT', not_img)
cv2.waitKey(0)