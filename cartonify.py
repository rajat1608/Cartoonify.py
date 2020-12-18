# -*- coding: utf-8 -*-




import cv2
import numpy as np
# reading image  
img = cv2.imread("suas.jpg") 
   
# Edges 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.medianBlur(gray, 5) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  
                                         cv2.THRESH_BINARY, 9, 9) 
   
# Cartoonization 
color = cv2.bilateralFilter(img, 9, 250, 250) 
cartoon = cv2.bitwise_and(color, color, mask=edges) 
   
   
cv2.imshow("Image", img) 
cv2.imshow("edges", edges) 
cv2.imshow("Cartoon", cartoon) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

class Cartoonizer:  
    """Cartoonizer effect  
        A class that applies a cartoon effect to an image.  
        The class uses a bilateral filter and adaptive thresholding to create  
        a cartoon effect.  
    """
    def __init__(self):  
        pass
  
    def render(self, img_rgb):  
        img_rgb = cv2.imread(img_rgb)  
        img_rgb = cv2.resize(img_rgb, (1366,768))  
        numDownSamples = 2   
        numBilateralFilters = 50   

        img_color = img_rgb  
        for _ in range(numDownSamples):  
            img_color = cv2.pyrDown(img_color)  
  
       
        for _ in range(numBilateralFilters):  
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)  
  
     
        for _ in range(numDownSamples):  
            img_color = cv2.pyrUp(img_color)  
    

        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)  
        img_blur = cv2.medianBlur(img_gray, 3)  
   
        img_edge = cv2.adaptiveThreshold(img_blur, 255,  
                                        cv2.ADAPTIVE_THRESH_MEAN_C,  
                                        cv2.THRESH_BINARY, 9, 2)  
     
        (x,y,z) = img_color.shape  
        img_edge = cv2.resize(img_edge,(y,x))  
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)  
        cv2.imwrite("edge.jpg",img_edge)  
     
        return cv2.bitwise_and(img_color, img_edge)  
  
tmp_canvas = Cartoonizer()  
  
file_name = "suas.jpg"
res = tmp_canvas.render(file_name)  
  
cv2.imwrite("Cartoon version.jpg", res)  
cv2.imshow("Cartoon version", res)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  