from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据

findLink = re.compile(r'<div id="content">"(.*?)"')

def main():
    pass

def getHtml(url):
    user={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"}
    requests =urllib.request.Request(url,headers=user)
    html = ""
    try:
        response = urllib.request.urlopen(requests,timeout=1)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getData():
    list =[]
    url="https://www.xbiquwx.la/10_10240/5018128.html"
    html=getHtml(url)
    soup = BeautifulSoup(html, "html.parser")
    p=soup.find_all(soup,"div")
    for s in   p:
        print(s)


if __name__ == '__main__':
    getData()
