# encoding:utf-8
import cv2

# 輸入一張圖片路徑
imgdata = cv2.imread('face/face0.jpg')
print('原始影像圖片size與通道數',imgdata.shape) #包含R,G,B三種元色 , 每種元色各256種階度

graydata = cv2.cvtColor(imgdata, cv2.COLOR_BGR2GRAY) # 將圖像轉為灰階, 降低運算複雜度
print('灰階影像圖片size與通道數',graydata.shape) #包含一個灰階，共256個階度

# 讓視窗可以自由縮放大小
cv2.namedWindow('img-color', cv2.WINDOW_NORMAL)

#將彩色圖像顯示在視窗
cv2.imshow('img-color', #視窗題目
           imgdata #圖片資訊
           )

# 讓視窗可以自由縮放大小
cv2.namedWindow('img-gray', cv2.WINDOW_NORMAL)
#將灰階圖像顯示在視窗
cv2.imshow('img-gray', #視窗題目
           graydata #圖片資訊
           )

# 等待隨機一個按鍵
cv2.waitKey(0)

#另存一個新的檔案
cv2.imwrite("capture\save.jpg",  #指定存檔路徑
            imgdata #圖片資訊
            )

#關閉視窗
cv2.destroyAllWindows()