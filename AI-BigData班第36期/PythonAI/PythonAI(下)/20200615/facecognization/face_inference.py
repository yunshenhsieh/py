import dlib
import face_recognition
import time
import json
import pandas as pd
import numpy as np
from decimal import Decimal
import base64
import logging

#print('dlib',dlib.__version__)
print('face_recognition',face_recognition.__version__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#辨識門檻值
TOLERANCE =0.3

df = pd.read_csv('FACE_MODE_PD.csv')
#取得所有人臉的encoding
FACEENCODING_DF = df.iloc[0:,1:]
#change pd to list
encoding_data = np.array(df.iloc[0:,1:])#取得encoding
encoding_list=encoding_data.tolist()#list

#取得所有人名
NAME_DF = df.iloc[0:,0]
#change pd to list
name_data = np.array(NAME_DF)#np.ndarray()
name_list=name_data.tolist()#list

def startInference(report, unknown_image_encoding):
    #開始推論
    logging.info('開始推論...')
    Candidate_dist=1
    Candidate_name=''
    have_predict_result = "False" #假設有結果have_predict_result="True"

    start = time.process_time()
    for namefile,encoding in zip(name_list,encoding_list):
        #print(namefile)
        #print(encoding)
        result = face_recognition.compare_faces([encoding], unknown_image_encoding, tolerance=TOLERANCE)
        dist = face_recognition.face_distance([encoding], unknown_image_encoding)
        print(namefile, result[0], dist[0])

        if(float(dist[0])<=Candidate_dist): #目前的距離若小於候選 則替換候選人
            Candidate_dist = float(dist[0])
            Candidate_name = namefile.split("FaceData\\")[1].split(".jpg")[0]

        if result[0]==True:
            have_predict_result=True

    if have_predict_result==True:
        report = '辨識出 '+Candidate_name+' 信心值 '+str(Decimal((1.0-float(Candidate_dist))*100).quantize(Decimal('0.00')))+"%"
    else:
        report = "沒有辨識出,但最有可能為 "+Candidate_name+' 信心值 '+str(Decimal((1.0-float(Candidate_dist))*100).quantize(Decimal('0.00')))+"%"

    end = time.process_time()
    report = report + " " + '推論完成時間: '+ str(round(end - start))+ ' 秒'
    logging.info(report)
    return report



#tempfile_path = "FaceData/Aaron老師.jpg"
tempfile_path = "FaceData/衛生福利部部長陳時中.jpg"

data_samples = []
with open(tempfile_path, "rb") as imageFile:
    image_str = base64.b64encode(imageFile.read()).decode('utf-8')
    data_samples.append({'image_bytes': {'b64': image_str}})

# 將接收到的待測照片轉為base64
#print(image_str)
payload = json.dumps({"instances": data_samples})

#Decoding JSON : to get base64 json.loads(payload)['instances'][0]['image_bytes']['b64']
#將base64編碼轉成待測圖片
BASE64TOIMAGE_FILE = 'b64image.jpg'
with open(BASE64TOIMAGE_FILE, "wb") as fh:
    fh.write(base64.b64decode(json.loads(payload)['instances'][0]['image_bytes']['b64']))

'''
server_endpoint = 'YOUR_SERVER_ENDPOINT'
# Send prediction request
r = requests.post(server_endpoint, data=payload)
probability = json.loads(r.content)['predictions']
'''

#取得待測圖片的encoding
unknown_image = face_recognition.load_image_file(BASE64TOIMAGE_FILE)
unknown_face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=0, model="hog")
print("unknown_face_locations",unknown_face_locations)

if unknown_face_locations ==[]:
    report = '這...我無法辨識...請給我正常的人臉...最好不要戴墨鏡.'

else:
    unknown_image_encoding = face_recognition.face_encodings(unknown_image, known_face_locations=unknown_face_locations, num_jitters=1)[0]
    report=''
    startInference(report,unknown_image_encoding)

