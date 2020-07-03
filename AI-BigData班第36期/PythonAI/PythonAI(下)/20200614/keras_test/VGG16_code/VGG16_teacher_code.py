
# coding: utf-8
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 載入VGG16
model = VGG16(weights='imagenet')

# 顯示出模型摘要
model.summary()

# 辨識
def predict(filename, rank):
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    print(x.shape)

    #在 x array的第0維新增一個資料 (np.expand_dims 用於擴充維度)
    x = np.expand_dims(x, axis=0)
    print(x.shape)

    #預測圖片 #轉換成VGG16可以讀的格式
    preds = model.predict(preprocess_input(x))
    print(preds.shape)

    #rank 取前幾名排序
    results = decode_predictions(preds, top=rank)[0]
    return results

# 辨識
filename = "vgg16TestPic/0.jpg"

plt.figure()
im = Image.open(filename)
im_list = np.asarray(im)
plt.title("predict")
plt.axis("off")
plt.imshow(im_list)
plt.show()

results = predict(filename, 10)
for result in results:
    print(result)
