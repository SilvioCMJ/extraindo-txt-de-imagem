import cv2
import pytesseract

# importando img
img = cv2.imread('print_magalu.JPG')

# extraindo txt
txt = pytesseract.image_to_string(img)
print(txt)
