# concurrent库 实现请求http请求
import concurrent.futures
import urllib.request
import time

URLS = [
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
    "http://www.baidu.com",
]


def load_url(url, timeout):
    print(f"Start loading {url} at {time.time()}")
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        result = conn.read()
    print(f"Finished loading {url} at {time.time()}")
    return result


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print("%r generated an exception: %s" % (url, exc))
        else:
            print("%r page is %d bytes" % (url, len(data)))
