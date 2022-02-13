import requests
import json

req_url = "https://inputtools.google.com/request?text={}&itc=zh-t-i0-pinyin&num=11&cp=0&cs=1&ie=utf-8&oe=utf-8&app=demopage"

proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "http://127.0.0.1:1080",
}


def parse_pinyin(pinyin_seq):
    resp = requests.get(req_url.format(pinyin_seq), proxies=proxies)
    data = json.loads(resp.text)
    try:
        result = data[1][0][1][0]
    except IndexError:
        result = ''
    return result


if __name__ == '__main__':
    r = parse_pinyin("huashengdun")
    print(r)
