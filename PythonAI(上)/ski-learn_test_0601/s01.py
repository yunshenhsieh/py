import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5) #設定隨機種子

iris = datasets.load_iris()  #鳶尾花資料集
X = iris.data   #花的四種特徵
print("iris.data",X,X.shape)
y = iris.target #花的種類
print("iris.target",y,y.shape)

model = KMeans(n_clusters=3) #建立KMeans模型
model.fit(X)  #將花的特徵數據 X套用到 KMeans模型進行分類
labels = model.labels_  #模型自動產生的分類標記
print("labels",labels,labels.shape)

#模型之後可以用下列方法預測未知的資料
#model.fit_predict(X)
print("model.fit_predict",model.fit_predict(X),model.fit_predict(X).shape)

#KMeans自動分群結果與原始標籤比對
i=0
for labels_name,target_name in zip(labels,y):
    #修正KMeans自動分群標籤labels_name 1為0而0為1
    if labels_name == 1:
        labels_name=0
    elif labels_name == 0:
        labels_name = 1
    if labels_name != target_name:
        print(labels_name, target_name)
        i=i+1
print("Accuracy:",str((len(X)-i)/len(X)),"%")

fig = plt.figure('f0', figsize=(5, 4))  #建立圖型
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

#用三個特徵值數列，畫出3D圖型上的點
ax.scatter(X[:, 3], X[:, 0], X[:, 2],
           c=labels.astype(np.float), edgecolor='k')

#畫出KMeans模型的重心(質心)
C = model.cluster_centers_
ax.scatter(C[:, 3], C[:, 0], C[:, 2],
          c='red', s=100, alpha=0.5)

ax.w_xaxis.set_ticklabels([])  #取消 x軸刻度
ax.w_yaxis.set_ticklabels([])  #取消 y軸刻度
ax.w_zaxis.set_ticklabels([])  #取消 z軸刻度

ax.set_xlabel('花瓣寬度', fontproperties="SimSun") #宋體
ax.set_ylabel('花萼長度', fontproperties="SimSun")#宋體
ax.set_zlabel('花瓣長度', fontproperties="SimSun")#宋體
ax.set_title('k_means_iris_3D')
ax.dist = 12  #與3D圖的距離
plt.show()








