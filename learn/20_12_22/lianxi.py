import urllib.request
import os



def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()

    return html

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    print("3")
    a = html.find("middleURL")
    

    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+12:b+4])
        else:
            b = a+12
        a = html.find("middleURL",b) 
    
    for each in img_addrs:
        print(each)
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        if "\\" not  in each:
            filename = each.split('/')[-1]
            with open(filename,"wb") as f:
                img = url_open(each)
                f.write(img)

def download_mm(folder="OOXX"):
    os.mkdir(folder)
    os.chdir(folder)

    page_url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1608561608521_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85"
    img_addrs = find_imgs(page_url)
    save_imgs(folder,img_addrs)


download_mm()

