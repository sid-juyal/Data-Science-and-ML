import cv2
img=cv2.imread("C:/Users/SIDDHARTH/desktop/ML and Data Science/pokemon_pic.JPG")
grey_img=cv2.imread("C:/Users/SIDDHARTH/desktop/ML and Data Science/pokemon_pic.JPG",cv2.IMREAD_GRAYSCALE)
cv2.imshow('Pikachu',img)
cv2.imshow('Grey_Pikachu',grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
