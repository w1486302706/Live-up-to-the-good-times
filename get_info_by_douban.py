# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup           # 网页解析
import requests     # URL操作，获取网页数据
import pandas as pd
from sqlalchemy import create_engine
import re

# 请求伪装成浏览器
hearders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

# n = pd.read_table('name.txt')
# names = n['name']
names = ['斗破苍穹','斗罗大陆']
res = []
for name in names:
    # url = f'https://www.douban.com/search?cat=1002&q={name}' # 仅影视
    url = f'https://www.douban.com/search?q={name}'
    # 获取查询结果，解析为soup
    request = requests.get(url,headers=hearders)
    soup = BeautifulSoup(request.text, "html.parser")
    # 获取查询结果列表
    information_list = soup.find('div', class_='result-list').find_all('div',class_='result')
    li = []
    for information in information_list:
        # 获取详细信息链接
        if name not in information.find('h3').find('a').text:
            continue
        information_url = information.find('h3').find('a')['href']
        # 获取详细信息页面，解析为soup
        request_inf = requests.get(information_url,headers=hearders)
        soup_inf = BeautifulSoup(request_inf.text, "html.parser")
        # 定位信息标签
        info = soup_inf.find('div',id='info')
        # 获取信息标签列表
        try:
            pl = info.find_all('span',class_='pl')
        except Exception as e:
            print(information.find('h3').find('a').text,'获取信息标签列表错误',e)
            continue
        # 解析信息，生成字典
        dic = {}
        dic['系列'] = name
        dic['名称'] = soup_inf.find('span',property='v:itemreviewed').text
        for i in pl:
            key =re.sub(r'[ :]','',i.text)
            if i.parent.name == 'span':
                try:
                    dic[key] = i.parent.find('span',class_='attrs').text
                except Exception as e:
                    dic[key] = i.parent.find('a').text
            elif i.next_sibling.next_sibling.name == "a":
                dic[key] = i.next_sibling.next_sibling.text.replace('\n','')
            elif i.text == '类型:':
                genre = ''
                for j in info.find_all('span',property='v:genre'):
                    genre = genre+j.text+'/'
                dic[key] = genre[:-1]
            elif i.text == '首播:' or i.text == '上映日期:':
                dic[key] = info.find('span',property='v:initialReleaseDate').text[:10]
            elif i.text == '片长:':
                dic[key] = info.find('span',property='v:runtime').text
            else:
                dic[key] = i.next_sibling.replace(' ','')
        li.append(dic)
    res.extend(li)

df = pd.DataFrame(res)

# 连接本地数据库
engine = create_engine("mysql+pymysql://root:cy123789@127.0.0.1:3306/myhappiness?charset=utf8")
with engine.connect() as conn:
    df.to_sql("NoInfo", conn, if_exists="append", index=False)

engine.dispose()