

<h1>【題目 : 使用 Python 發送 Line Notify 推播】</h1>

## 準備事項 : 
>1. 申請 Line Notify 權杖 (須記錄 token )
>2. 電腦要安裝 Python 執行環境
>3. 使用 Command 模式，執行 python linenotify.py  (linenotify 為以下 python 範例程式 )
===

## 程式說明

[以下程式來源 linenotify.py]:https://github.com/derricktsai0904/Python/blob/master/LineNotify/linenotify.py "linenotify.py"
[以下程式來源 linenotify.py ]
``` python
import requests

def lineNotifyMessage(token, msg):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload )
      return r.status_code


message = '這是PYTHON第一次測試Line Notify推播'
token = 'nc5m8LHju7IT5gU2OZ8zBdmdC2WsWDC5ZZHSz1q2Xyg'    // 需要先申請 Line Notify 權杖

lineNotifyMessage(token, message )

```
