# encoding:utf-8
import cv2

# 輸入一張圖片路徑
imgdata = cv2.imread('face/face0.jpg')
print(imgdata.shape)

#將彩色影像縮放
resize_image = cv2.resize(imgdata,(1000,500))

cv2.imshow('imgdata', imgdata )
cv2.imshow('resize_image', resize_image )

# 等待隨機一個按鍵
cv2.waitKey(0)
#關閉視窗
cv2.destroyAllWindows()