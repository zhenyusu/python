#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
'''
#请求页面获取html
r = requests.get('http://www.baidu.com').content.decode('UTF-8')
soup = BeautifulSoup(r,'html.parser')
print(type(soup)) #解析html文档对象
html = soup.prettify()
print(html)
'''
soup = BeautifulSoup(open('web.html','r',encoding='utf-8'),'lxml')
'''
    四大对象
'''

#tag
print(soup.html.head.meta )
print(soup.div.input.name) #返回标签名
print(soup.div.input.attrs) #返回标签里面的属性 字典格式