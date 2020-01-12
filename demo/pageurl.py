import requests
import re
pattern=r'<a href=\"(.*?)\" target=\"_blank\">'
url='http://www.jj20.com/bz/nxxz/nxmt/list_57_1.html'
r=requests.get(url)
page_urls=re.findall(pattern,r.text)
urls=[]
for i in page_urls:
    i='http://www.jj20.com'+str(i)
    global urls
    urls.append(i)
print urls
