from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('mYXe5hBvYKaj616/3U9dzxwzKn2ZFtIYXPhxPY2QdVGYBSPgFJTBTELybJacYixVXWoIDQnVEDbHrF5EfPD6XY+tBv/KQZ/eyb06zisknKegQgNexGGOM/HcWYiXfmUPrXcN7PRLgMQE1bGqCXwCygdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('de835c790a309dd82099e139f033a2de')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

def Keyboard(text)
	KeywordDict = ("Hi":"Hello"
                   "Oh":"Ya"
				   "He":"Ha")
    for k in KeyboardDict.keys():
	    if text.find(k)  |= -1:
		    return [True,keyWordDict[k]]
    return [False]
	
def Reply(event):
    Ktemp = KeyWord(event.message.text)
    if Ktemp[0]:
	    line_bot_api.reply_message(event.reply_token,
		    TextSendMessage(text = Ktemp[1]))
	else:
	    line_bot_api.reply_message(event.reply_token,
		    TextSendMessage(text = event.message.text))
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
