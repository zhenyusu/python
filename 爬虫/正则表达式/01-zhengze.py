
#-*- coding: UTF-8 -*-
import re
'''
    findall
'''
pattern = re.compile('[a-zA-Z]+') #compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
str1 = '123abc456def789'
result = pattern.findall(str1) #在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
print(result)

pattern = re.compile('([a-z])[a-z]([a-z])')
str1 = '123abc456def789'
result = pattern.findall(str1) #在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
print(result) #findall 遇上分组的时候只返回分组匹配的结果

'''
    finditer 可以返回完整的正则匹配结果，以及分组的匹配结果
'''
pattern = re.compile('([a-z])[a-z]([a-z])')
str1 = '123abc456def789'
result = pattern.finditer(str1) #返回一个迭代器
print(result)
for i in result:
    print(i.group())
    print(i.group(2))


'''
    split 分割
'''
str = 'one,two,three,four'
pattern = re.compile('\W+')
print(re.split(pattern,str))

'''
    sub 替换
    subn 返回替换的次数
'''

pattern = re.compile('\d')
str = 'one1two2three3four'
print(pattern.sub('-',str))
print(pattern.subn('-',str))

'''引用分组'''
str = 'hello 123,world 321'
pattern = re.compile('(\w+) (\d+)')
for i in pattern.finditer(str):
    print(i.group(1))
print(pattern.sub(r'\2 \1',str)) #取得分组  \1 \2

#13588997789
#15****7789

'''
    贪婪与非贪婪
    贪婪：在整个表达式匹配成功的前提下，尽可能多的匹配
    非贪婪：在整个表达式匹配成功的前提下，尽可能少的匹配

'''

str = 'aaa<p>hello</p>bbb<p>world</p>ccc'
pattern = re.compile('<p>.*</p>')
print(pattern.findall(str)) #贪婪模式

str = 'aaa<p>hello</p>bbb<p>world</p>ccc'
pattern = re.compile('<p>.*? </p>')
print(pattern.findall(str)) #非贪婪模式

'''
    匹配中文字符
'''
str = '你好,hello,帅哥'
pattern = re.compile('[\u4e00-\u9fa5]+')
print(pattern.findall(str))

