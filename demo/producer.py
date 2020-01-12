#encoding=utf-8
import requests,re,listurl
all_urls=listurl.all_urls
all_img_urls=[]
class Producer():
    def getImage(self):
        while len(all_urls)>0:
            url=all_urls.pop()
            print '解析:'+url
            pattern=r'<a href=\"(.*?)\" target=\"_blank\">'
            r=requests.get(url)
            all_imgs=re.findall(pattern,r.text)
            for i in all_imgs:
                i='http://www.jj20.com'+str(i)
                global all_img_urls
                all_img_urls.append(i)
        print all_img_urls
                




