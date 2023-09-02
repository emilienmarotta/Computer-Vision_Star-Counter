import cv2
import numpy as np

imgPath = "image.jpg" # Photo by Samuel Richard (@mumbolicious on unsplash.com)

imgInGrayScale = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Load the image in grayscale

if imgInGrayScale is not None : # Only if we are able to open the image

    # Used to distinguish between glued dots
    dotPattern = np.ones((2, 2), np.uint8) # Dot pattern definition
    dilatedImg = cv2.dilate(imgInGrayScale, dotPattern, iterations=1)  

    # Used to identify the dots
    dots = cv2.Canny(dilatedImg, threshold1=30, threshold2=90) # Dots detection
    contours, _ = cv2.findContours(dots, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find external contours
    dotsNb = len(contours)

    print("Number of celestial bodies (aproximately) : ", dotsNb)
else :
    print("Unable to open the file")