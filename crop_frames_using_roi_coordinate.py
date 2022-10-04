import cv2
import time

ROI_BOX = {
    "box1": [(591, 289), (366, 402)],
    "box2": [(104, 324), (376, 378)],
    "box3": [(991, 37), (193, 226)],
    "box4": [(738, 0), (278, 239)],
    "box5": [(472, 63), (297, 248)],
    "box6": [(179, 34), (317, 311)]
    }

VIDEO_URL = "501/501_d2.mp4"
cap = cv2.VideoCapture(VIDEO_URL)

seconds = 5
fps = cap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
multiplier = fps * seconds

count =0



frame_id = 0
while cap.isOpened():
    frameId = int(round(cap.get(1)))
    _, frame = cap.read()
    
    frame = cv2.resize(frame, (1280, 720))
    tm=time.time()
    for key in ROI_BOX.keys():
        box = ROI_BOX[key]
        box_id = key

        x, y, w, h = box[0][0], box[0][1], box[1][0], box[1][1] 
        cropped = frame[y:y+h, x:x+w]
        if frameId % multiplier == 0:
            cv2.imwrite('cropped/test/frame'+str(frame_id)+"_"+str(tm)+"_"+str(box_id)+'.png', cropped)
        # cv2.rectangle(frame, box[0], box[1], (0, 255, 0), 2)
        
    cv2.imshow("video", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    frame_id += 1

cv2.destroyAllWindows()
cap.release()
