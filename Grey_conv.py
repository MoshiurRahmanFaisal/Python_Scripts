
# GRAY CONVERSION

from glob import glob
import cv2

src = glob("DE\\*.png")

for j in src:
    jj=j.split('\\')[1]
    img=cv2.imread(j)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(j[:-3]+'png',img)


with open('person_data\\Faisal\\faisal\\label\\faisal1_frame-60.txt') as f:
    lines = f.read()
    print(type(lines))
with open('person_data\\Faisal\\faisal\\label\\faisal1_frame-60.txt','r') as f:
    for line in f:
        print(line.split(' ')[0])