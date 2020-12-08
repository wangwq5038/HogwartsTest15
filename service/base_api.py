import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wwa9838ed5429d61e4'
        corpsecret = 'QxAWVke4E-0nVmHnn59ymMEaOI6j5w9q1ZsI_eDYe0c'
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r
