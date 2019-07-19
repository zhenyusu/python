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
print(soup.div.input.attrs['type']) #返回标签里面的属性

#NavigableString
print(soup.div.span.string)

print(type(soup.div.span.string))

'''
    遍历文档树
'''
#直接子节点
print(soup.div.contents)
print(soup.div.contents[0])
print(soup.div.contents[1])
print(soup.div.contents[2])
print(soup.div.contents[3].attrs['type'])

print(soup.div.children)

#节点内容
print(soup.div.contents[1].string)
print(soup.div.contents[1].text)


#父节点
print(soup.div.contents[1].parent)
print(soup.div.contents[1].parents)


#兄弟节点
print(soup.div)
print(soup.div.next_sibling.next_sibling)
print(soup.div.next_sibling.next_sibling.previous_sibling)


print("----------------------------------------------")
#查找文档树
#find all
#print(soup.find_all('div')) #查找所有的div
print(soup.find_all('a'))
result = soup.find_all('a')
for i in result:
    print(i.text)
