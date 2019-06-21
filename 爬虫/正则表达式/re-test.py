#-*- coding:utf-8 -*-
import re
'''

    1. 将下列的字符串中所有的url匹配出来
'''

str = '''
2454911893@qq.com
hjas23@163.com
http://www.baidu.com
https://www.sae.com
ftp://www.nnn.org
ftps://www.jksad.net
'''


pattern = re.compile('[a-z]+:\/\/www(\.\w+)(\.\w+){1,2}')
result = pattern.finditer(str)
for i in result:
    print(i.group())