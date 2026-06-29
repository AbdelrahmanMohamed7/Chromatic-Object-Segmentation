#Importing Libraries 
import cv2
import numpy as np
#Object Detection
def detect_objects(image):
    # Converting the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    #Color bound for yellow colour 
    lower_bound = np.array([20,60,80])     
    upper_bound = np.array([30, 255, 255])
    
    
    msk = cv2.inRange(hsv_image, lower_bound, upper_bound)
    # Applying the masks to the original image
    obj1 = cv2.bitwise_and(image, image, mask=msk)
    obj2 = cv2.bitwise_and(image, image, mask=msk)
    
    # Combine the results
    output = cv2.add(obj1, obj2)
    
    return output

# Loading the image
image = cv2.imread('13.png')

# Detection of yellow objects in the image
result = detect_objects(image)

# Display the extracted output
cv2.imshow('Origanl Image', image)
cv2.imshow('Extracted Output', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

