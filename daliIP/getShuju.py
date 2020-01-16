#encoding=utf-8
import re,requests,time
class Shuju():
    def IP_port(self,urls,pat):
        for url in urls:
            try:
                header={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}
                r=requests.get(url,headers=header)
                pat=re.compile(pat)
                s=pat.findall(r.text)
                words=[]
                for i in s:
                    words.append(i)
                time.sleep(1)
            except:
                print 'IP获取失败'
                pass
            finally:
                print '数据获取成功',url
        try:
            with open('代理IP及端口号.txt','a') as f:
                #title='IP地址'+' '*8+'端口号'
                #f.write(title)
                f.write('\n')
                for t in words:
                    i,j=t
                    line=str(i)+' '*5+str(j)
                    f.write(line)
                    f.write('\n')
                f.close()
        except:
            print '写入失败'
        finally:
            print '程序执行完毕'


