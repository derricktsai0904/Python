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
token = 'nc5m8LHju7IT5gU2OZ8zBdmdC2WsWDC5ZZHSz1q2Xyg'

lineNotifyMessage(token, message )