#encoding=utf-8
htmls=[]
#获取图片所在网页的html地址
class getHtml():
    def __init__(self,target_url):
        self.target_url=target_url
    def html(self,start_page,page_num):
        for i in xrange(start_page,page_num+1):
            h=self.target_url % i
            global htmls
            htmls.append(h)
#获取图片地址
import requests,re
pic_urls=[]
class url():
    def getUrl(self,pattern_words):
        for url in htmls:
            r=requests.get(url)
            pics=re.findall(pattern_words,r.text)
            for pic in pics:
                pic='http://pic.netbian.com/tupian/'+pic+'.html'
                global pic_urls
                pic_urls.append(str(pic))
            





        


