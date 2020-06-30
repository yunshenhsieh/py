import urllib.request,os
import numpy
import pandas as pd
from sklearn import preprocessing

url="http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls"
filepath='C:\\Users\\Big data\\Desktop\\data\\titanic3.xls'
if not os.path.isfile(filepath):
    result=urllib.request.urlretrieve(url,filepath)
    print('downloaded:',result)

all_df=pd.read_excel(filepath)
cols=['survived','name','pclass','sex','age','sibsp','parch','fare','embarked']
all_df=all_df[cols]
df=all_df.drop(['name'],axis=1)
age_mean = df['age'].mean()
df['age']=df['age'].fillna(age_mean)
fare_mean = df['fare'].mean()
df['fare']=df['fare'].fillna(fare_mean)
df['sex']=df['sex'].map({'female':0,'male':1}).astype(int)
x_OneHot_df=pd.get_dummies(data=df,columns=["embarked"])
ndarray=x_OneHot_df.values
Label=ndarray[:,0]
Features=ndarray[:,1:]
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
scaledFeatures=minmax_scale.fit_transform(Features)

msk = numpy.random.rand(len(all_df))<0.8
train_df=all_df[msk]
test_df=all_df[~msk]

def PreprocessData(raw_df):
    df=raw_df.drop(['name'],axis=1)
    age_mean=df['age'].mean()
    df['age']=df['age'].fillna(age_mean)
    fare_mean=df['fare'].mean()
    df['fare']=df['fare'].fillna(fare_mean)
    df['sex']=df['sex'].map({'female':0,'male':1}).astype(int)
    x_OneHot_df=pd.get_dummies(data=df,columns=['embarked'])

    ndarray=x_OneHot_df.values
    Features=ndarray[:,1:]
    Label=ndarray[:,0]

    minmax_scale=preprocessing.MinMaxScaler(feature_range=(0,1))
    scaledFeatures=minmax_scale.fit_transform(Features)
    return scaledFeatures,Label

train_Features,train_Label=PreprocessData(train_df)
test_Features,test_Label=PreprocessData(test_df)

print(train_Features[:2])
print(train_Label[:2])