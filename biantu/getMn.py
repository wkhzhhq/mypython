#encoding=utf-8
import getUrls,down
module_url='http://pic.netbian.com/4kmeinv/index_%d.html'
H=getUrls.getHtml(module_url)
H.html(1,10)
pattern='<a href=\"/tupian/(\d{3,6})\.html\" target=\"_blank\">'
U=getUrls.url()
U.getUrl(pattern)
down.Down()

