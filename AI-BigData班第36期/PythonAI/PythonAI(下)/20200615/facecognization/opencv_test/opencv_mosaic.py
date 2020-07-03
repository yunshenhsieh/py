# encoding:utf-8
import cv2
import numpy as np

# 輸入一張圖片路徑
imgdata = cv2.imread('face/face0.jpg')
print(imgdata.shape)

#產生一張感興趣的範圍 ROI (Region of Interest)
roi_image = imgdata[200:400,  #圖片左上角 Y座標值200 到 往下Y座標值400的位置
                     300:600   #圖片左上角 X座標值300 到 往下Y座標值600的位置
                    ]
#產生一個馬賽克圖片大小為 200x300
mask =np.random.randint(0, #隨機整數的最小值
                        256, #隨機整數的最大值
                        (200,300,3)  #圖片的形狀
                        )
#取得原始影像要馬賽克的ROI範圍設定馬賽克資訊, 200:400 -> 400-200 = 200,  300:600 -> 600-300 = 300
imgdata[200:400,300:600] = mask

#將圖像顯示在視窗
cv2.imshow('mask', #視窗題目
           imgdata #圖片資訊
           )

#將圖像顯示在視窗
cv2.imshow('after-mask', #視窗題目
           roi_image #圖片資訊
           )

# 等待隨機一個按鍵
cv2.waitKey(0)

#另存一個新的檔案
cv2.imwrite("capture\save.jpg",  #指定存檔路徑
            imgdata #圖片資訊
            )

#關閉視窗
cv2.destroyAllWindows()
