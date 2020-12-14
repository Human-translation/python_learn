import requests

response = requests.get('https://item.jd.com/100009077475.html')
print(response.text)

