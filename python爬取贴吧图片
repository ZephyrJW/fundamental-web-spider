import urllib.request
import re

a = input('请输入希望抓取的链接:')
b = int(input('请输入希望抓取几个页面的图片:'))

def getima(aaa):
    reg = re.compile(r'src="(.*?)" pic_ext=')
    name = re.findall(r'src="(.*?)" pic_ext=',aaa)
    print(type(name))
    l = re.findall(reg,aaa)
    tem = 0
    for x in l:
        tem += 1  
        rename = name[tem-1][-5:-1]
        urllib.request.urlretrieve(x,"%s %d.jpg" %(rename,tem))  #do not forget the tuple'()'
    
for i in range(b):
    n = str(i+1)
    a1 = urllib.request.urlopen(a+"?pn="+n).read().decode('utf-8')
    print("downloading.."+a+"?pn="+n)
    getima(a1) 

#for example: http://tieba.baidu.com/p/3990366972
