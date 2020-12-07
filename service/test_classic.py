import json
import time

import requests


def test_tag_list():
    corpid = 'wwa9838ed5429d61e4'
    corpsecret = 'QxAWVke4E-0nVmHnn59ymMEaOI6j5w9q1ZsI_eDYe0c'
    # 获取token
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
        params={'corpid': corpid, 'corpsecret': corpsecret}

    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

    token = r.json()['access_token']
    # 获取tag标签列表
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={"tag_id": []}
    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0
    tag_name = 'tag1_new'+time.strftime("%H_%M_%S")
    # 修改tag标签
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={"access_token": token},
        json={
            'id': 'et8b3HDQAAoA0lffIubF4vix-7u1ey3Q',
            'name': tag_name
        }
    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

    # 获取tag标签列表
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={"tag_id": []}
    )
    # print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == 'python15'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    # jsonpath(f"$..[?(@.name='{tag_name}')]") jmepath
    print(tags)
    assert tags != []



