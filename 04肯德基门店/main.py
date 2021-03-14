import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    # UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; '
                     'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/88.0.4324.190 Safari/537.36'
    }
    cname = input('enter a city:')

    data = {
        'cname':cname,
        'pid':'',
        'pageIndex':'1',
        'pageSize':'10'
    }
    param = {
        'op':'cname'
    }
    response = requests.post(url=url, data=data, params=param, headers=headers)
    text_data = response.text
    # print(text_data)
    file_name = cname + '.json'
    fp = open(file_name, 'w', encoding='utf-8')
    result = json.loads(text_data)
    json.dump(result, fp=fp, ensure_ascii=False)
    print('over!!!')
