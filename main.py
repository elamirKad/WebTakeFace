import cv2

face = cv2.CascadeClassifier("face.xml")

#cap = cv2.VideoCapture(0)



for i in range(int(input("input number"))):
    frame = cv2.imread("testPics/h({}).jpg".format(i+1))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 1, minSize=(40,40),flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]

          
    try:
        cv2.imshow("Croped", crop_img)
        cv2.imwrite("cropped/h{}crop.jpg".format(i),crop_img)
    except:
        print("Don't recognized")
    cv2.imshow("Main", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
