import cv2
import os
import datetime
cam = cv2.VideoCapture(0)
# waitKey = 10
while True:
    check, frame = cam.read()
    cv2.namedWindow('video', cv2.WINDOW_NORMAL) 
    # cv2.resizeWindow('video', 1080, 1080)
    cv2.imshow('video', frame)
    

    key = cv2.waitKey(10)

    if key == ord("s"):
        now = datetime.datetime.now()

        filename = f"prarthana.jpg"
        path = r'C:\Users\dell\OneDrive\Desktop'
        cv2.imwrite(os.path.join(path, 'prarthana.jpg' ),frame)

        filename 
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()