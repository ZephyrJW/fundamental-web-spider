#try to correct some problems 

import urllib
import urllib2
from bs4 import BeautifulSoup

url = 'http://movie.douban.com/subject/3660428/?from=tag_all'
source_code = urllib2.urlopen(url).read()
plain_text = str(source_code)
#print plain_text
soup = BeautifulSoup(plain_text)
s = soup.find('div',{'id':'info'}).findAll('span')[2].string

print s

#这样可以对每一部电影的信息进行更为详尽的抓取，此为用《金色梦乡》导演信息进行的说明

#发现问题，也许不同电影的信息有些许不同，不应固定位置，在内容中再找寻信息比较合理，当尽快做出
