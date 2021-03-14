import json

import requests

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                      'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36'
    }
    param = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': '20'
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    fp = open('movie.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!!!')
