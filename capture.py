import cv2, time

video = cv2.VideoCapture(0)

time.sleep(3)

check, frame = video.read()

print(check)
print(frame)

video.release()