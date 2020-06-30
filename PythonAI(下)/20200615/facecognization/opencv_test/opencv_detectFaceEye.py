# encoding:utf-8
import cv2
import numpy as np

#設定 haarcascades的路徑
#載入偵測人臉模組
face_cascade = cv2.CascadeClassifier('c://haarcascades//haarcascade_frontalface_default.xml')
#載入偵測眼睛模組
eye_cascade = cv2.CascadeClassifier('c://haarcascades//haarcascade_eye.xml')

img = cv2.imread('face/face0.jpg') # 輸入一張圖像
#img = cv2.imread('face/face1.jpg') # 輸入一張圖像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 將圖像轉為灰階, 降低運算複雜度

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,  #有的人臉離鏡頭近，會比其他人臉更大
    minNeighbors=5,   #檢測矩形其周圍有多少物體進行偵測
    minSize=(30, 30), #檢測矩形的大小
    flags=cv2.CASCADE_SCALE_IMAGE
)
print('找到 ', len(faces), " 張臉")

for (x, y, w, h) in faces:
    #cv2.rectangle(影像, 頂點座標, 對向頂點座標, 顏色, 線條寬度)
    img = cv2.rectangle(img,
                        (x, y), #左上角座標
                        (x + w, y + h), #寬與高
                        (255, 0, 0), #顏色
                        2) #線框粗細
    #img = cv2.circle(img, ((x + x + w) // 2, (y + y + h) // 2), w // 2, (0, 255, 0), 2)

    roi_gray = gray[y: y + h, x: x + w] #取得灰階圖像偵測的範圍.
    roi_color = img[y: y + h, x: x + w] #取得彩色圖像偵測的範圍.

    # 儲存偵彩色圖像偵測的範圍
    cv2.imwrite('roi_color.jpg', roi_color)

    #使用 灰階圖像偵測的範圍 偵測眼睛
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print('找到 ', len(eyes), " 顆眼睛")
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
