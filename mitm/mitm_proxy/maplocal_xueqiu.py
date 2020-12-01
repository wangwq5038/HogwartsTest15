from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 发起请求，判端url是不是我们预期的url
    if "quote.json" in flow.request.pretty_url:
        # 创造一个response
        with open("\\Users\\wangwq\\Desktop\\quote.json") as f:
            flow.response = http.HTTPResponse.make(
                200,
                # 读取文件内容作为数据
                f.read(),
                {"Content-Type": "application/json"}
            )
