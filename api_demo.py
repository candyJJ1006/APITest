# -*- coding: utf-8 -*-
import requests


def main():
    # 发送请求
    url = "https://www.baidu.com"
    try:
        response = requests.get(url).text
    except Exception as e:
        return f'错误:{e}'
    return response

if __name__ == "__main__":
    result = main()
    print(result)