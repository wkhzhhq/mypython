#encoding=utf-8
import re,requests
class Link():
    def getPageNumber(self,in_link,pat):
        header={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
        r=requests.get(in_link,headers=header)
        pat=re.compile(pat)
        l=pat.findall(r.text)
        words=[]
        for i in l:
            words.append(int(i))
        return max(words)
    def getUrls(self,format_word,start_page,end_page):
        urls=[]
        for i in xrange(start_page,end_page+1):
            url=format_word % i
            urls.append(url)
        return urls

