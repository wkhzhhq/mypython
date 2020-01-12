all_urls=[]
class Spider():
    def __init__(self,target_url,headers):
        self.target_url=target_url
        self.headers=headers
    def getUrls(self,start_page,page_num):
        global all_urls
        for i in xrange(start_page,page_num+1):
            url=self.target_url % i
            all_urls.append(url)

