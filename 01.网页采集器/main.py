import requests
'''
UA：User-Agent
UA检测：门户网站的服务器会检测请求主体的身份标识，如果载体的身份标识是某一款浏览器，
说明该请求为正常请求；如果检测到载体是爬虫，就会拒绝此次请求
UA伪装：让爬虫对应的请求载体身份伪装为某一款浏览器
'''

if __name__ == '__main__':
    # UA伪装：将User-Agent封装到字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; '
                     'x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/88.0.4324.190 Safari/537.36'
    }
    url = 'https://www.baidu.com/s'
    # 处理url的参数，封装到字典中
    kw = input('enter a word:')
    param = {
        'wd':kw
    }
    # 对指定的url发起请求，并携带参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    file_name = kw+'.html'
    # 对爬取到的数据持久化存储
    with open(file_name,'w',encoding='utf_8') as fp:
        fp.write(page_text)
    print(file_name+'保存成功！')

