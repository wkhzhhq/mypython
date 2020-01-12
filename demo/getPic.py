#encoding=utf-8
import producer,requests,re
all_img_urls=producer.all_img_urls
pic_urls=[]
def Make():
    pattern=r'<img src=\"(.+?)\"'
    for i in all_img_urls:
        r=requests.get(i)
        pic_url=re.findall(pattern,r.text)
        for url in pic_url:
            global pic_urls
            pic_urls.append(str(url))
    n=1
    try:
        for url in pic_urls:
            r=requests.get(url)
            with open('Picture/性感美女_%d.jpg'%(n),'wb') as f:
                f.write(r.content)
                f.close()
            n+=1
    except:
        pass




