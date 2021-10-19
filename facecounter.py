# Import required libraries
import cv2
import numpy as np
import dlib
 
 
# Connects to your computer's default camera
# floor_08.mp4 **** Water Dance_720p.mp4

# cap = cv2.VideoCapture('floor_08.mp4')
cap = cv2.VideoCapture('Water Dance_720p.mp4') 
 
# Detect the coordinates
detector = dlib.get_frontal_face_detector()
img=0
 
# Capture frames continuously
while True:
 
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 1)
 
    # RGB to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
 
    # Iterator to count faces
    i = 0

    for face in faces:
 
        # Get the coordinates of faces
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
 
        # Increment iterator for each face in faces
        i = i+1
 
        # Display the box and faces
        cv2.putText(frame, 'Face Number. '+str(img+i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)
         # if video is still left continue creating images
        name = 'D:/python_ai/OpenCV_FaceCounter/data/face' + str(img+i) + '_face.jpg'
        print ('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, frame)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # This command let's us quit with the "q" button on a keyboard.
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break
img=img+1 
# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()