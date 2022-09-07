# data move 

import os
import shutil
sourcepath='Banpr_data2/train/train'
sourcefiles = os.listdir(sourcepath)
# sourcepath2='anpr_data\\train'
# sourcefiles2 = os.listdir(sourcepath2)

destinationpath = 'trash'
for file in sourcefiles:
    # for file2 in sourcefiles2:
    #     if file!=file2:
            if file.endswith('.xml'):
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))



import os
import shutil
sourcepath='Banpr_data2/test/test'
sourcefiles = os.listdir(sourcepath)
# destinationpath = 'anpr_data\\images\\val'
file1 = open("test.txt","w")#write mode
for file in sourcefiles:
    if file.endswith('.jpg'):
        file1.write("data/ts/"+file+'\n')
        # file1.close()