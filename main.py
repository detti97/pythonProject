import cv2

capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("file/haarcascade_frontalface_default.xml")

while True:
    _, camera = capture.read()
    camera_gray = cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(camera_gray)
    for x,y, width, height in faces:
        cv2.rectangle(camera, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=5)
    cv2.imshow("Kamera", camera)
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()