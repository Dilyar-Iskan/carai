import cv2

img = cv2.imread("./Test/Test01.out.jpeg")

flipcode = 0  # 0: along x axis, 1: along y axis, -1: along both x and y axes
flipped_img = cv2.flip(img, flipcode)

cv2.imshow("car", img)
cv2.imshow("flipped_car", flipped_img)
cv2.waitKey()
cv2.destroyAllWindows()