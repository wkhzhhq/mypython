from listurl import *
from producer import *
import getPic
myurl='http://www.jj20.com/bz/nxxz/nxmt/list_57_%d.html'
header={'User-Agent':'Mozilla/5.0 (X11 Linux x86_64'}
s=Spider(myurl,header)
s.getUrls(1,5)
print all_urls
p=Producer()
p.getImage()
getPic.Make()
