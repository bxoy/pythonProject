import requests
from multiprocessing.dummy import Pool


def text():
    url = 'https://www.baodu.com'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    r = requests.get(url=url, headers=headers)
    print(r)
