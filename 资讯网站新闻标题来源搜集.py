//尝试抓取正文内容总是失败，望赐教
//attempted to collect text content but failed, please help me

import urllib.request
import re
from bs4 import BeautifulSoup

page_list = ['http://www.traveldaily.cn/search?kw=%%E8%%8A%%92%%E6%%9E%%9C&page=1',]
for page in range(2,5):  #需要抓取的页码 pages
    raw_url = "http://www.traveldaily.cn/search?kw=%%E8%%8A%%92%%E6%%9E%%9C&page=%s" %page
    page_list.append(raw_url)
#print(art_list)  此时有了所有需要页面的url地址，打开找到需要的所有文章编号 
for i in range(len(page_list)):
    html1 = urllib.request.urlopen(page_list[i]).read().decode('utf-8')
    art_list = re.findall(r'<a href="/article/(.*)" target="_blank">',html1)
#print(art_list) 获得了需要的所有的文章编号，可以在url中直接访问

arturl_list = []
for nn in range(len(art_list)):
    arturl_list.append('http://www.traveldaily.cn/article/%s' %art_list[nn])
#print(arturl_list) #这样得到所有新闻的url地址，可以open后抓取了

num = 0
for urlll in arturl_list:
    num += 1
    ss = urllib.request.urlopen(urlll).read().decode('utf-8')
    soup = BeautifulSoup(ss)
    title = re.findall(r'<title>(.*)</title>',ss)
    time = re.findall(r'<span class="time">(.*)</span>',ss)
    source = re.findall(r'<span class="source">(.*)</span>',ss)
   # content = re.findall(r'<div class="content-text"> <p>(.*)</p>',ss)
    content = soup.find_all("class=\"content-text\"")
    f1 = open(str(num)+".txt",'w')
    f1.close()
    f = open(str(num)+".txt",'a')
    f.write(title[0])
    f.write('\n'+time[0])
    f.write('   '+source[0])
    f.write('\n')
    for words in content:
        f.write(words)
    f.close()

