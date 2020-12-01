from mitmproxy import http
import json


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
        # 把响应数据转化为Python对象，保存到data中
        data = json.loads(flow.response.content)
        # 第二个股票名字加长一倍
        data['data']['items'][1]['quote']['name'] *= 2
        # 第三个股票名字变成空
        data['data']['items'][2]['quote']['name'] = " "
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)
