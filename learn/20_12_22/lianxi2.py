import urllib.request
import os

url = "https://twitter.com/ding290"



req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
response = urllib.request.urlopen(req)
html = response.read()

print(html)