import urllib.request
import urllib.parse
import json
import random


url = "http://jandan.net/ooxx"

iplist = ['157.7.143.36:1080','104.149.134.114:3128','157.7.197.239:1080','170.0.54.232:8080']

i = random.randint(0,len(iplist)-1)

proxy_support = urllib.request.ProxyHandler({"http":iplist[i]})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)


'''
with open(arr + str(count),"wb") as f:
    f.write(cat_img)
'''
