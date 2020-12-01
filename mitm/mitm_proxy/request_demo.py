

#request方法名不能修改
from mitmproxy import http


def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "feier"
    print(flow.request.headers)