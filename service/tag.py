import json
import time

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()
    def get_token(self):
        corpid = 'wwa9838ed5429d61e4'
        corpsecret = 'QxAWVke4E-0nVmHnn59ymMEaOI6j5w9q1ZsI_eDYe0c'
        # 获取token
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}

        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        token = r.json()['access_token']
        return token
    def add(self):
        pass
    def list(self):
        # 获取tag标签列表
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={"tag_id": []}
        )
        # print(json.dumps(r.json(), indent=2))
        return r
    def updata(self, id, tag_name):
        # 修改tag标签
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                'id': id,
                'name': tag_name
            }
        )
        # print(json.dumps(r.json(), indent=2))
        return r
    def delete(self):
        pass