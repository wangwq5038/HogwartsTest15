

#request方法名不能修改
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 增加請求的頭信息中的字段
    flow.request.headers["myheader"] = "feier"
    print(flow.request.headers)