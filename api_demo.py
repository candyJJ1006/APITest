# -*- coding: utf-8 -*-
import requests


def main():
    url = "https://www.baidu.com"
    try:
        response = requests.get(url).text
    except Exception as e:
        return f'错误:{e}'
    return response

if __name__ == "__main__":
    result = main()
    print(result)
    print("程序结束")
