#move .txt amd image files

import os
from collections import defaultdict
import shutil

EXTENSIONS = {'.jpg', '.txt'}

directory = 'cars_train'

grouped_files = defaultdict(int)

count=0

for f in os.listdir(directory):
    name, ext = os.path.splitext(os.path.join(directory, f))
    if ext in EXTENSIONS:
        grouped_files[name] += 1

for name in grouped_files:
        if grouped_files[name] == len(EXTENSIONS):
                with open('{}.jpg'.format(name)) as image_file, \
                        open('{}.txt'.format(name)) as txt_file:
                    files_to_move = [txt_file, image_file]
                    # print(files_to_move)
                    for file in files_to_move:
                        # print(file.name)
                        count+=1
                        shutil.move(file.name, 'annoted_car_data')
print("\ntotal files moved:",count)