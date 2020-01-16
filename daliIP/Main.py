#encoding=utf-8
import Links,getShuju
pat=r'href=\"/wt/(\d+)\"'
in_link='https://www.xicidaili.com/wt/3'
link=Links.Link()
pageNum=link.getPageNumber(in_link,pat)
print pageNum
format1='https://www.xicidaili.com/wt/%d'
urls=link.getUrls(format1,6,10)
print urls
s=getShuju.Shuju()
pat1=r'<td>(.+?)</td>\s+<td>(\d+)</td>'
s.IP_port(urls,pat1)
