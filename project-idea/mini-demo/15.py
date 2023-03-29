# 人脸检测
# 目的：编写一个Python脚本，可以检测图像中的人脸，并将所有的人脸保存在一个文件夹中。
# 提示：可以使用haar级联分类器对人脸进行检测。它返回的人脸坐标信息，可以保存在一个文件中。
# 安装：OpenCV。
# 下载：haarcascade_frontalface_default.xml

import cv2

# Load the cascade
pathf = 'C:\\Users\\11004142\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pathf) 


img = cv2.imread("./data/grace_hopper.jpg")        # Read the input image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert into grayscale  
faces = face_cascade.detectMultiScale(gray, 1.3, 4)     # Detect faces

# Draw rectangle around the faces       
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    crop_face = img[ y:y+h, x:x+w ]
    cv2.imwrite( str(w) + str(h) + "_faces.jpg", crop_face)
# Display the output
cv2.imshow("img", img)
cv2.imshow("imgcropped", crop_face)
cv2.waitKey()



