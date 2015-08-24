import urllib.request
import re
import time

list1 = ["集团","科技"]
for item in list1:
	gjc = urllib.request.quote(item)
	url = 'http://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word='+gjc

	headers = {
				"GET":url,
				"host":'sug.so.360.cn',
				"Referer":"http://www.haosou.com/",
				"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
				}

	req = urllib.request.Request(url)
	for key in headers:
		req.add_header(key,headers[key])

	html = urllib.request.urlopen(req).read().decode('utf-8')
	ss = re.findall("\"word\":\"(.*?)\"",html)
	for item in ss:
		print(item)
	time.sleep(6)
