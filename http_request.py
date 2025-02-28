import requests

# 伪造成谷歌浏览器内核请求
headers = {
    "User-Agent": "",  # 谷歌内核
    "Accept": "",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Site": "none",
    "TE": "trailers",
}
r = requests.get("https://www.baidu.com", headers=headers)
# print(r.status_code)
# print(r.cookies)
print(r.headers)
# print(r.encoding)
# print(r.url)
# print(r.history)
# print(r.content)
