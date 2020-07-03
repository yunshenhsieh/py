import face_recognition
import glob
import time
import pandas as pd
import numpy  as np
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#建立人名路徑DataFrame
faceName = glob.glob('FaceData/*.jpg')
NAME_PATH_DF = pd.DataFrame(faceName, columns=["namePath"])
print(NAME_PATH_DF)

faceEncodings = []
start = time.process_time()
for index,imagePath in NAME_PATH_DF['namePath'].items():
    print('目前訓練', imagePath)
    iknow_image = face_recognition.load_image_file(imagePath)
    iknow_face_locations = face_recognition.face_locations(iknow_image, number_of_times_to_upsample=0, model="hog")
    iknow_image_encoding = \
        face_recognition.face_encodings(iknow_image, known_face_locations=iknow_face_locations, num_jitters=10)[0]
    faceEncodings.append(iknow_image_encoding)
end = time.process_time()
report = '編碼訓練時間:', round(end - start), '秒'
logging.info(report)

#查看人臉特徵值
#print(faceEncodings)

FACE_ENCODING_DF=pd.DataFrame(faceEncodings) #特徵值用行寫入
FACE_MODE_PD=NAME_PATH_DF.join(FACE_ENCODING_DF)
print(FACE_MODE_PD)
SAVE_PD_FILE = "FACE_MODE_PD.csv"
FACE_MODE_PD.to_csv(SAVE_PD_FILE, index=False)
print("儲存face mode",SAVE_PD_FILE)

#取得所有人臉的encoding
df = pd.read_csv('FACE_MODE_PD.csv')
FACEENCODING_DF = df.iloc[0:,1:]
#change pd to list
encoding_data = np.array(df.iloc[0:,1:])#取得encoding
encoding_list=encoding_data.tolist()#list

