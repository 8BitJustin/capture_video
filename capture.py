import cv2, time
# object - captures video, places within video titled object. Could be actual file, 0 means one webcam
video = cv2.VideoCapture(0)
# used to count frames
a = 1
# will run until 'q' is hit. each revolution == 1 frame
while True:
    # increments a variable to count frames
    a = a + 1
    # frame reads images from the video capture object, check is boolean type
    check, frame = video.read()
    # prints True
    print(check)
    # prints numpy array that represents the image
    print(frame)
    # creates gray version of the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # initially used to give webcam time to turn on, not needed in final version
    # time.sleep(3)
    # display window, title and what is being displayed (gray)
    cv2.imshow("Capturing", gray)
    # makes sure frame window is closed - 0 allows anykey to close
    key = cv2.waitKey(1)
    # function - if the key/waitkey equals q, while loop breaks
    if key == ord('q'):
        break
# prints framecount when finished
print(a)
# closes capturing device, in this case the webcam
video.release()
# as described, this closes the opened highgui window
cv2.destroyAllWindows()