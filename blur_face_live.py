import cv2
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret , photo = cap.read()
    co_ordinates  = model.detectMultiScale(photo)
    if len(co_ordinates) == 0:
        print("no face detected")
    elif len(co_ordinates) ==1:
        x1 = co_ordinates[0][0]
        y1 = co_ordinates[0][1]
        x2 = co_ordinates[0][2] + x1
        y2 = co_ordinates[0][3] + y1
        rectangle_photo = cv2.rectangle(photo , (x1 , y1) , (x2 , y2) ,[0,255,0] , 5)
        crop_face = rectangle_photo[y1:y2 , x1:x2]
        blur_face = cv2.blur(crop_face , ksize=(30,30))
        #below line may give some shape error so we'll resolve soon
        photo[y1:y2 , x1:x2] = blur_face
        
        cv2.imshow("hi" , photo)
        if cv2.waitKey(10)==13:
            break
    elif len(co_ordinates) ==2:
        x1 = co_ordinates[0][0]
        y1 = co_ordinates[0][1]
        x2 = co_ordinates[0][2] + x1
        y2 = co_ordinates[0][3] + y1
        xx1 = co_ordinates[1][0]
        yy1 = co_ordinates[1][1]
        xx2 = co_ordinates[1][2] + xx1
        yy2 = co_ordinates[1][3] + yy1
        rectangle_photo1 = cv2.rectangle(photo , (x1 , y1) , (x2 , y2) ,[0,255,0] , 5)
        rectangle_photo2 = cv2.rectangle(rectangle_photo1 , (xx1 , yy1) , (xx2 , yy2) ,[0,255,0] , 5)
        crop_face1 = rectangle_photo1[y1:y2 , x1:x2]
        blur_face1 = cv2.blur(crop_face1 , ksize=(30,30))
        rectangle_photo1[y1:y2 , x1:x2] = blur_face1
        
        crop_face2 = rectangle_photo1[yy1:yy2 , xx1:xx2]
        blur_face2 = cv2.blur(crop_face2 , ksize=(30,30))
        rectangle_photo2[yy1:yy2 , xx1:xx2] = blur_face2

        cv2.imshow("hi" , rectangle_photo2)
        if cv2.waitKey(10)==13:
            break
cv2.destroyAllWindows()

cap.release()