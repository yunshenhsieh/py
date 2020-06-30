from flask import Flask, jsonify, request, abort
import time
import base64
import json
import requests
import os
import logging
import face_recognition
import pandas as pd
import numpy as np
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    ImageMessage)

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["JSON_AS_ASCII"] = False
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'JPEG', 'jpeg', 'PNG', 'gif', 'GIF'])

#YOUR_CHANNEL_ACCESS_TOKEN
line_bot_api = LineBotApi('R/BBkgkNKCVgjEa6uc+/NBkSOev2IkbMqI0JGm5y8fHvwg55Ra2TioQ8NTbhdpyZmkhS0qHZwrOAto/KcArLEY4pp30FtoX7Fw7VWZfd4GJqrsge8FF19qMWpWUdAiFKyZE1CoGTK2v2k1VmQqkg5wdB04t89/1O/w1cDnyilFU=')
#YOUR_CHANNEL_SECRET
handler = WebhookHandler('3fdc868fafeeba9b10a873fb39f25b7c')

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


def startInference(unknown_image_encoding,startTime):
    #開始推論
    print('開始推論...')
    Candidate_dist=1
    Candidate_name=''
    have_predict_result = "False" #假設有結果have_predict_result="True"

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
            print("有辨識出...通過門檻")
            have_predict_result=True


    if have_predict_result==True:
        report = '辨識出 '+Candidate_name+' 信心值 '+str(Decimal((1.0-float(Candidate_dist))*100).quantize(Decimal('0.00')))+"%"
        print(report)
    else:
        report = "沒有辨識出,但最有可能為 "+Candidate_name+' 信心值 '+str(Decimal((1.0-float(Candidate_dist))*100).quantize(Decimal('0.00')))+"%"
        print(report)

    end = time.process_time()
    report = report + " " + '推論完成時間: '+ str(round(end - startTime))+ ' 秒'
    print(report)
    return report



#透過/callback這個 webhook , 接收來自Line Server的聊天訊息
@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


#line server發過來的文字訊息的處理邏輯
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #不處理官方發來的訊息
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text) #event.message.text得到傳來的文字
        )


#line server發過來的影像訊息的處理邏輯
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    #不處理官方發來的訊息
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        # 這次我加了上面這一行

        #透過 event.message.id 得到圖片內容
        message_content = line_bot_api.get_message_content(event.message.id)
        # 將圖片內容儲存成檔案
        tempfile_path = os.path.join("tmp", event.message.id + ".jpg")
        with open(tempfile_path, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

        #將圖片做成base64編碼
        data_samples = []
        with open(tempfile_path, "rb") as imageFile:
            image_str = base64.b64encode(imageFile.read()).decode('utf-8')
            data_samples.append({'image_bytes': {'b64': image_str}})

        # 將base64編碼使用json格式傳給 圖片辨識伺服器API( http://127.0.0.1:5000/exebase64 )
        payload = json.dumps({"instances": data_samples})
        server_endpoint = 'http://127.0.0.1:5000/exebase64'
        r = requests.post(server_endpoint, data=payload)
        #圖片辨識伺服器API的回應
        report = json.loads(r.content)['msg']
        logging.info(report)
        # 將回應送回Line
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=report)
        )


# 接受圖片的base64編碼,另存成圖片 tmp/imageb64.jpg, 取得BASE64TOIMAGE_FILE 照片的encoding
@app.route('/exebase64', methods=['POST'], strict_slashes=False)
def api_upload_base64():
    #get data of post-request
    tmpString = request.data.decode("utf-8")
    jsonString = json.loads(tmpString)
    #print(jsonString['instances'][0]['image_bytes']['b64'])

    BASE64TOIMAGE_FILE = "tmp/imageb64.jpg"
    with open(BASE64TOIMAGE_FILE,"wb") as fh:
        fh.write(base64.b64decode(jsonString['instances'][0]['image_bytes']['b64']))

    # 取得BASE64TOIMAGE_FILE 照片的encoding
    unknown_image = face_recognition.load_image_file(BASE64TOIMAGE_FILE)  # 未知照片
    unknown_face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=0, model="hog")
    print("unknown_face_locations", unknown_face_locations)
    if unknown_face_locations == []:
        logging.info('這...我無法辨識...請給我正常的人臉...最好不要戴墨鏡.')
        report = '這...我無法辨識...請給我正常的人臉...最好不要戴墨鏡.'

    else:
        unknown_image_encoding = \
        face_recognition.face_encodings(unknown_image, known_face_locations=unknown_face_locations, num_jitters=1)[0]
        report = startInference(unknown_image_encoding,time.process_time())

    return jsonify({"msg": report})

if __name__ == "__main__":
    #允許所有IP存取服務, 打開port 5000
    app.run(debug=True,port='5000',host='0.0.0.0')