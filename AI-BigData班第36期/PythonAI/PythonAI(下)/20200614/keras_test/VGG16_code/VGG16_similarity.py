from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os

# 相似矩陣的計算
# 將test2目錄內的每一張jpg取出其特徵向量，並相互比較，利用 cosine 函數計算兩張照片特徵向量的角度，越接近 1，表示越相似
def cosine_similarity(featuresVector):
    #與自己的轉置矩陣(T)做內積運算(dot)
    sim = featuresVector.dot(featuresVector.T)
    if not isinstance(sim, np.ndarray):
        sim = sim.toarray()
    #np.diagonal取對角線 np.sqrt取平方根
    norms = np.array([np.sqrt(np.diagonal(sim))])
    return (sim/norms/norms.T)


# 自 vgg16TestPic 目錄找出所有 JPEG 檔案
images_filename_list = []
images_data_tuple = []
for img_path in os.listdir("vgg16TestPic"):
    if img_path.endswith(".jpg"):
        img = image.load_img("vgg16TestPic/" + img_path, target_size=(224, 224))
        images_filename_list.append(img_path)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        if len(images_data_tuple) == 0:
            images_data_tuple = x
        else:
            images_data_tuple = np.concatenate((images_data_tuple, x))

# 轉圖片為VGG的格式
images_data_tuple = preprocess_input(images_data_tuple)
# include_top=False，表示只計算出特徵, 不使用最後3層的全連接層(不使用原來的分類器)
model = VGG16(weights='imagenet', include_top=False)
# 顯示出模型摘要
model.summary()

# 預測出特徵
features = model.predict(images_data_tuple)

#計算特徵向量
featuresVector = features.reshape(len(images_filename_list), 7 * 7 * 512)

# 計算相似矩陣
sim = cosine_similarity(featuresVector)
print(sim) #印出所有照片之間的特徵值, 越接近1.0, 照片越相近

#印出目錄內的檔案
print(images_filename_list)
#測試檔案在目錄內的位置
testPicID = 2
#np.argsort 進行由小到大的排序, -sim表式將資料列反向, 最後會得到由大到小的排序
top = np.argsort(-sim[testPicID], axis=0)

rank = [images_filename_list[i] for i in top]
print('目錄內的所有照片與測試檔案 {}的相似度排序(越前面的越相似):{}'.format(images_filename_list[testPicID],rank))
