import requests


def pinduoduo():
    url = 'https://apiv2.pinduoduo.com/api/jade/asics/search/goods_list'
    headers = {
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'anti-content': '0aqWtql5NcQaF22_EMOJXOMOxFg5Cwxrm_d0us76bFNbKlfJvZGQbvtZDMy_WIGxtUb0m1YLaNeTNnCu7C5aK8wR2PMSOElqmJBC0LECqmQtsM5Rs2vkyXs3SrGlaVWSbMYbkZYTLL6XsbDv3HANKzCZYD632Vp6iKIc25yd6ZHF45w7lc5lgAMXJXPcGrF6hRCTbCCZDi0ILwVU_4g_bIslewvhp1HQcKfzpvGwIAHqqScSB8r6uchA-CJRpL9e8PK5-5wwXSg3hMI4Oq3oRgn43KVjv0THcfee60-XTdBrHMtpDN0Y0VGLe0Q85a_ODfX5VmGrzD98iFPfkcpusqiGDR23Md4kjpvtptf8b2hPr6wVVOJu4COrrFhQ3BlPlauYmB9sFHiGLu3P45DOjYIEhuqNd16fTW0m6fR9So32Sdgn8_ik2pW1IHvjzyDqnVUHKwwaDKooxmCNV9HzPSLqTy0COxiFmIyPWV9',
        # 'Connection': 'keep-alive',
        # 'Content-Length': '89',
        'content-type': 'application/json',
        # 'Cookie': 'api_uid=79c917b9fc644ea7aef12c8a022854d1; request_id=a69e2e4944f84037b3a58df5b922004c',
        'Host': 'apiv2.pinduoduo.com',
        'Origin': 'https://m.pinduoduo.com',
        'Referer': 'https://m.pinduoduo.com/m_goods-list?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&page=1',
        # 'sec-ch-ua-platform': '"Android"',
        # 'sec-ch-ua-mobile': '?1',
        # 'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        # 'Sec-Fetch-Site': 'same-site',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Dest': 'empty',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    }
    data = {
        'page_info': {
            'current': 1    ,
            'page_size': 10
        },
        'keyword': "华为手机",
        'sort_type': "default"
    }
    r = requests.post(url=url, headers=headers, json=data).json()
    print(r)


if __name__ == '__main__':
    pinduoduo()
