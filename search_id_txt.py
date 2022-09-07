# search class id from txt file 
import glob
import os
import shutil
for filename in glob.glob('input\\old_annotation_jpeg\\label\\*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
        for line in f:
            value=line.split(' ')[0]
            if(value!="0"):
                # line = line.replace(value, "0")
                # print(line[2:])
                print(filename)
                # shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
            else:
                print("annotation ok")

import glob
import os
for filename in glob.glob('person_data\\full_test_data\\test\\*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:

        for line in f:
            value=line.split(' ')[0]
            if(value!="0"):
                data = value.replace(value, "0")

                with open(os.path.join(os.getcwd(), filename), 'w') as file:

                    # Writing the replaced data in our
                    # text file
                    file.write(data)



import os
import shutil
sourcepath='balanced/test'
sourcefiles = os.listdir(sourcepath)
# sourcepath2='anpr_data\\train'
# sourcefiles2 = os.listdir(sourcepath2)

destinationpath = 'balanced/test_label'
for file in sourcefiles:
    # for file2 in sourcefiles2:
    #     if file!=file2:
            if file.endswith('.txt'):
                shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
