#encoding=utf-8
import requests,getUrls,os,re
def Down():
    try:
        #os.system('mkdir "勾魂美女"')
        pic_urls=getUrls.pic_urls
        n=1
        for url in pic_urls:
            r=requests.get(url)
            pattern='<img src=\"(.+?)\" data-pic'
            p_url=re.findall(pattern,r.text)
            for p in p_url:
                p="http://pic.netbian.com"+str(p)
                p_r=requests.get(p)
                with open('勾魂美女/girl-%d.jpg'%(n),'wb') as f:
                    f.write(p_r.content)
                    f.close()
                n+=1
    except:
        pass


