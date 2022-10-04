import cv2
import numpy as np

 #image_path
img_path="l14c5_0.jpg"

#read image
img_raw = cv2.imread(img_path)

#RESIZE IMAGE
img_resize = cv2.resize(img_raw,(1280,720))

#select ROIs function
ROIs = cv2.selectROIs("Select Rois",img_resize)

#print rectangle points of selected roi
print(ROIs)

#Crop selected roi ffrom raw image

#counter to save image with different name
crop_number=0 

#loop over every bounding box save in array "ROIs"
for rect in ROIs:

    #get x,y,w,h of every roi
    x,y,w,h = rect
    img_crop=img_resize[y:y+h,x:x+w]
    #save image with different name
    # cv2.imwrite("crop_"+str(crop_number)+".jpg",img_crop)
    # crop_number+=1
    #show image
    cv2.imshow("crop",img_crop)
cv2.waitKey(0)