# encoding:utf-8
import cv2

# 輸入一張圖片路徑
imgdata = cv2.imread('face/face0.jpg')

# 原始影像
cv2.imshow('imgdata', imgdata )

#重直翻轉
flip_image = cv2.flip(imgdata,0)
cv2.imshow('flip_image1', flip_image )

#水平翻轉
flip_image = cv2.flip(imgdata,1)
cv2.imshow('flip_image2', flip_image )

#同時水平與重直翻轉
flip_image = cv2.flip(imgdata,-1)
cv2.imshow('flip_image3', flip_image )


# 等待隨機一個按鍵
cv2.waitKey(0)
#關閉視窗
cv2.destroyAllWindows()