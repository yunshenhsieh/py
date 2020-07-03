# encoding:utf-8
import cv2

# 輸入一張圖片路徑
imgdata = cv2.imread('face/face0.jpg')
height, width = imgdata.shape[:2]

# 原始影像
cv2.imshow('imgdata', imgdata )

#旋轉影像 產生矩陣資料
M = cv2.getRotationMatrix2D((height/2,width/2),
                            60, #逆時針旋轉60度
                            0.6 #縮小60%
                            )

#輸入原始資料與旋轉矩陣資料,輸出的尺寸
rotation_image = cv2.warpAffine(imgdata,M,(height, width))
cv2.imshow('rotation_image', rotation_image )

# 等待隨機一個按鍵
cv2.waitKey(0)
#關閉視窗
cv2.destroyAllWindows()