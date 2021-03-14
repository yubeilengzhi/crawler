import json

import requests


if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                      'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36'
    }
    # 设置URL以及参数
    post_url = 'https://fanyi.baidu.com/sug'
    kw_data = input('enter a word:')
    data = {
        'kw':kw_data
    }
    # 发送post请求
    response = requests.post(url=post_url,data=data,headers=headers)
    # 获取响应数据；json()方法返回的是obj，（如果确认响应数据是json类型，才能使用json()）
    dic_obj = response.json()
    # 持久化存储
    file_name = kw_data+'.json'
    fp = open(file_name,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!!!')