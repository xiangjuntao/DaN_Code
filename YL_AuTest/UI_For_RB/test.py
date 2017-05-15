import json
from selenium import webdriver
ss={'a':'qwe','v':432}
m='a'
import requests
mm=requests.get('http://www.baidu.com')
print mm.status_code
def do(elements, todo):
    print str(elements)
    print eval('elements[\''+todo+'\']')
do(ss,m)
