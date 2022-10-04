import cv2
vidcap = cv2.VideoCapture('5min_clip/L14_C4 Part 2.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("l14c4_part2_%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
  if count==1:
    break