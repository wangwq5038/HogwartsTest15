from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 发起请求，判端url是不是我们预期的url
    if "quote.json" in flow.request.pretty_url:
        with open("D:\HogwartsTest15\mitm\mitm_proxy\quote.json", encoding='utf-8') as f:
            # 创造一个response
            flow.response = http.HTTPResponse.make(
                200,
                # 读取文件内容作为数据
                f.read(),
                {"Content-Type": "application/json"}
            )

# def test_xxx():
#     with open("quote.json", encoding='utf-8') as f:
#         print(f.read())
