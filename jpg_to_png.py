# jpg to png

from glob import glob                                                           
import cv2 
pngs = glob('input/train/non_covid/*.jpeg')

for j in pngs:
    jj=j.split('\\')[1]
    # print(j[:-4])
    img = cv2.imread(j)
    cv2.imwrite(j[:-4] + 'png', img)
