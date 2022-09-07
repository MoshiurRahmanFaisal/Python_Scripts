# rename files

import os
from os import path
import shutil

Source_Path = 'cropped_person_data/obj'
Destination = 'Cropped_cleanded'
Source_Path2 = 'cropped_person_data/obj'
Destination2 = 'Cropped_cleanded'

# Source_Path3 = 'input\\New folder (2)\\not taken_organized\\frames_25-04-2022_12_25_39_trackID=32\\image'   
# Destination3 = 'input\\New folder (2)\\not taken_organized\\frames_25-04-2022_12_25_39_trackID=32\\image'
# Source_Path4 = 'input\\New folder (2)\\not taken_organized\\frames_25-04-2022_12_25_39_trackID=32\\label'
# Destination4 = 'input\\New folder (2)\\not taken_organized\\frames_25-04-2022_12_25_39_trackID=32\\label'
# dst_folder = os.mkdir(Destination)


def main():
    for count, filename in enumerate(os.listdir(Source_Path)):
        jjj=filename.split('.')[0]
        # jjj=filename.split('\\')[1]
        print(jjj)
    
        dst = "person_"+str(count) + ".png"
        os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))

    for count, filename2 in enumerate(os.listdir(Source_Path2)):
        # # rename all the files
        
        jj=filename2.split('.')[0]
        # jjj=filename.split('\\')[1]
        # print(jjj)
    
        dst2 = "person_"+str(count) + ".txt"

        # # rename all the files
        os.rename(os.path.join(Source_Path2, filename2),  os.path.join(Destination2, dst2))

    # for count, filename3 in enumerate(os.listdir(Source_Path3)):
    #     jjj=filename3.split('.')[0]
    #     # jjj=filename.split('\\')[1]
    #     # print(jjj)
    
    #     dst3 = "abir47_"+jjj + ".jpeg"
    #     os.rename(os.path.join(Source_Path3, filename3),  os.path.join(Destination3, dst3))

    # for count, filename4 in enumerate(os.listdir(Source_Path4)):
    #     # # rename all the files
        
    #     jj=filename4.split('.')[0]
    #     # jjj=filename.split('\\')[1]
    #     # print(jjj)
    
    #     dst4 = "abir47_"+jj + ".txt"

    #     # # rename all the files
        # os.rename(os.path.join(Source_Path4, filename4),  os.path.join(Destination4, dst4))


# Driver Code
if __name__ == '__main__':
    main()