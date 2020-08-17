# 引用Web Server套件
from flask import Flask, request, abort,json

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

#
from linebot.exceptions import (
    InvalidSignatureError
)

# 將消息模型，文字收取消息與文字寄發消息 引入
from linebot.models import *

# 設定Server啟用細節
app = Flask(__name__)
# 生成實體物件
line_bot_api = LineBotApi('<your Channel access token>')
handler = WebhookHandler('<your Channel secret>')

# 啟動server對外接口，使Line能丟消息進來
@app.route("/", methods=['POST'])
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
        abort(400)

    return 'OK'

# 儲存使用者上傳的圖片，存在本地端
from linebot.models import ImageMessage
@handler.add(MessageEvent,message=ImageMessage)
def handle_image_message(event):
    # 請line_bot_api 把圖片從line抓回來，儲存到本地端
    # 圖片的名字以消息的id做命名
    # line_bot_api get message content line-bot-sdk
    message_content=line_bot_api.get_message_content(event.message.id)
    file_name =event.message.id + '.jpg'
    with open('./image/'+file_name,'wb')as f:
        for chunk in message_content.iter_content():
            f.write(chunk)

    # 請line_bot_api 回覆用戶，說圖片已儲存。
    # line_bot_api reply TextSendMessage
    line_bot_api.reply_message(
        event.reply_token,
        [
         TextSendMessage(text='圖片已儲存，檔名為：' + file_name),
         TextSendMessage(text='I am so busy')
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)