from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 发起请求，判端url是不是我们预期的url
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个response
        flow.response = http.HTTPResponse.make(
            200,
            # 读取文件内容作为数据
            b"hello world",
            {"Content-Type": "text/html"}
        )
