import requests
import json
import time

for a in range(3):
    url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(a*20)
    file = requests.get(url_visit).json()   #这里跟之前的不一样，因为返回的是 json 文件
    time.sleep(6)

    for i in range(20):
        dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
        urlname=dict['url']
        title=dict['title']
        rate=dict['rate']
        cast=dict['casts']
    
        print('{}  {}  {}  {}\n'.format(title,rate,'  '.join(cast),urlname))