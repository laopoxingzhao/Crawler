from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #excel4
import  sqlite3 #数据库操作


#主要执行
def main():
    baseurl="https://movie.douban.com/top250?start="
    getDataS(baseurl)
    savepath=".\\豆瓣电影.xls"
    saveData(savepath)


#爬取网页
def getDataS(baseurl):
    data=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=getData(url)

    return  data

#得到指定url的网页内容
def getData(url):
    cookie={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
        }
    requests=urllib.request.Request(url,headers=cookie)
    try:
        response=urllib.request.urlopen(requests)
        html=""+response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):#hasattr()用于判断对象是否包含某一属性
            print(e.reason)
    return html
def saveData(path):
    pass




if __name__ == '__main__':

    getData("https://movie.douban.com/top250?start=")