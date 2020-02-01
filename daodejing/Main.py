#encoding:utf-8
import os,requests,time,re
from lxml import etree
from threading import *

nMaxThread=5
ThreadLock=BoundedSemaphore(nMaxThread)

savePath='catelogue'

heads={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0','Cookie':'wptouch-pro-cache-state=desktop; __tins__3371828=%7B%22sid%22%3A%201580476243850%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201580478074716%7D; __51cke__=; __51laig__=2; bdshare_firstime=1580476244592; _ga=GA1.2.1802158164.1580476247; _gid=GA1.2.1674415068.1580476247; _gat=1','Referer':'https://www.baidu.com/link?url=-PmUrD5oAZRku8diPrhmsg8VkeKaWzF6tZpPL3nZISlyYM9rSy7Jiko1wzzZTLx4&wd=&eqid=95a3a1880002de7a000000055e342749','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Connection':'keep-alive','Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2','Accept-Encoding':'gzip, deflate','Host':'www.zxuew.cn'}

class Daodejing(Thread):
    def __init__(self,url):
        Thread.__init__(self)
        self.url=url

    def run(self):
        try:
            self.SaveContent()
        finally:
            ThreadLock.release()

    def SaveContent(self):
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        r=requests.get(self.url,headers=heads)
        if r.status_code==200:
            html=etree.HTML(r.content)
            title=html.xpath('//div[@id="art-main"]/div[@class="art-Sheet"]/div[@class="art-Sheet-body"]/div[@class="art-contentLayout"]/div[@class="art-content"]/div[@class="art-Post"]/div[@class="art-Post-body"]/div[@class="art-Post-inner art-article"]/div[@class="art-PostMetadataHeader"]/h2/span/a/text()')[0].strip().encode('utf-8')
            x1=html.xpath('//div[@id="art-main"]/div[@class="art-Sheet"]/div[@class="art-Sheet-body"]/div[@class="art-contentLayout"]/div[@class="art-content"]/div[@class="art-Post"]/div[@class="art-Post-body"]/div[@class="art-Post-inner art-article"]/div[@class="art-PostContent"]/p')
            x2=html.xpath('//div[@id="art-main"]/div[@class="art-Sheet"]/div[@class="art-Sheet-body"]/div[@class="art-contentLayout"]/div[@class="art-content"]/div[@class="art-Post"]/div[@class="art-Post-body"]/div[@class="art-Post-inner art-article"]/div[@class="art-PostContent"]/h1//text()')
            
            with open('%s/%s.txt' %(savePath,title),'w') as f:
                str_1=''
                for strtxt in x2:
                    str_1+=strtxt
                f.write(str_1.encode('utf-8'))
                f.write('\n')
                for i in range(1,len(x1)):
                    f.write(x1[i].xpath('string(.)').encode('utf-8'))
                    f.write('\n')
                
                f.close()
            print 'Download:%s' % title

def main():
    for i in range(1,82):
        ThreadLock.acquire()
        url="http://www.zxuew.cn/daodejing_%d/" % i
        t=Daodejing(url)
        t.start()

if __name__ == '__main__':
    main()
            
            

            
