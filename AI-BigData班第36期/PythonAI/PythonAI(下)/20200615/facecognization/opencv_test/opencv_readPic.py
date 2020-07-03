# encoding:utf-8
import cv2

# 輸入一張圖片路徑
imgdata = cv2.imread('face/face0.jpg')


# 讓視窗可以自由縮放大小
cv2.namedWindow('img', cv2.WINDOW_NORMAL)


#將圖像顯示在視窗
cv2.imshow('img', #視窗題目
           imgdata #圖片資訊
           )

# 等待隨機一個按鍵
cv2.waitKey(0)

#另存一個新的檔案
cv2.imwrite("capture\save.jpg",  #指定存檔路徑
            imgdata #圖片資訊
            )

#關閉視窗
cv2.destroyAllWindows()
