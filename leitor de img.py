import cv2
import pytesseract

# importando img
img = cv2.imread('exemplo.JPG')

# extraindo txt
txt = pytesseract.image_to_string(img)
print(txt)
