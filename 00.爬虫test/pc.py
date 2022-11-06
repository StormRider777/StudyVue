#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECT_NAME: test
# @FileName  :pc.py
# @Time      :2022/11/5 10:28
# @Author    :StormRider
'''
多搜索引擎爬取图片
spider = getimg(kw=kw,page=n,website='sogou')
 kw--查询关键词,,page--搜索多少页,website--使用的搜索引擎
     website:
        baidu  百度 (默认)
        sogou  搜狗
        bing   bing

spider.get()
'''


import httpx
import re
import time
import os
import random
from concurrent.futures import ThreadPoolExecutor
import json

class getimg(object):
    def __init__(self,*args,**kwargs):
        self.user_agent_list=[
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
                'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
                'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
                'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
                'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
                'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
                'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
                'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
                'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
                'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
                'NOKIA5700/ UCWEB7.0.2.37/28/999',
                'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999'
            ]
        self.kw = kwargs.get('kw', '狗')
        self.page = kwargs.get('page', 1)
        self.header = {'user-agent': random.choice(self.user_agent_list)}
        self.func=kwargs.get('website','baidu')

    def get(self):
        if not self.kw or not self.page:
            print("\033[1;31;0m 缺少必要的参数! \033[0m")
            return False
        if self.func=='bing':
            self.getbingimg()
        if self.func=='baidu':
            self.getbaiduimg()
        if self.func=='sogou':
            self.getsogouimg()

    def baiduurldecode(self,url=''):
        # !/usr/bin/env python
        # -*- coding: utf-8 -*-
        if not url:
            return ''
        str_table = {
            '_z2C$q': ':',
            '_z&e3B': '.',
            'AzdH3F': '/'
        }

        char_table = {
            'w': 'a',
            'k': 'b',
            'v': 'c',
            '1': 'd',
            'j': 'e',
            'u': 'f',
            '2': 'g',
            'i': 'h',
            't': 'i',
            '3': 'j',
            'h': 'k',
            's': 'l',
            '4': 'm',
            'g': 'n',
            '5': 'o',
            'r': 'p',
            'q': 'q',
            '6': 'r',
            'f': 's',
            'p': 't',
            '7': 'u',
            'e': 'v',
            'o': 'w',
            '8': '1',
            'd': '2',
            'n': '3',
            '9': '4',
            'c': '5',
            'm': '6',
            '0': '7',
            'b': '8',
            'l': '9',
            'a': '0'
        }

        # str 的translate方法需要用单个字符的十进制unicode编码作为key
        # value 中的数字会被当成十进制unicode编码转换成字符
        # 也可以直接用字符串作为value
        char_table = {ord(key): ord(value) for key, value in char_table.items()}
        for key, value in str_table.items():
            url = url.replace(key, value)
        # 再替换剩下的字符
        return url.translate(char_table)

        '''
        url = r"ippr_z2C$qAzdH3FAzdH3Ffl_z&e3Bftgwt42_z&e3BvgAzdH3F4omlaAzdH3Faa8W3ZyEpymRmx3Y1p7bb&mla"
        print(decode(url)
        '''

    def getbaiduimg(self):
        self.baiduurl=r'https://image.baidu.com/search/acjson'
        self.baiduparams = {
            'tn': 'resultjson_com',
            'logid': '11375913495882037758',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'fr': '',
            'word': self.kw,
            'queryWord': self.kw,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'expermode': '',
            'nojc': '',
            'isAsync': '',
            'pn': self.page * 30,
            'rn': 30,
            'gsm': '1e',
            int(time.time() * 1000): '',
        }
        self.header['Referer']='https://image.baidu.com/'
        res=httpx.get(url=self.baiduurl,params=self.baiduparams,headers=self.header,timeout=7)
        if res.status_code!=200:
            print("\033[1;31;40m 网络连接错误! \033[0m")
            return False
        restext=res.content.decode('utf-8')

        data=json.loads(restext,strict=False)
        rows=data['data']

        with ThreadPoolExecutor(max_workers=10) as tp:
            for r in rows:
                objurl=r.get('objURL','')
                sourceurl=self.baiduurldecode(objurl)
                fname=r.get('fromPageTitle','')
                if not fname or not sourceurl:
                    continue

                imgurl=r.get('thumbURL','')
                imgtypes=['.jpg','.jpeg','.bmp','.png']
                lx=''
                for imgtype in imgtypes:
                    if sourceurl.upper().find(imgtype.upper()):
                        lx=imgtype
                        break

                if not lx:
                    lx='.jpg'

                tp.submit(self.saveimg,urlf=sourceurl,fname=fname,filetype=lx,mirurlf=imgurl)

    def getbingimg(self):
        # 'https://cn.bing.com/images/async'
        # 'https://cn.bing.com/images/search'
        self.bingurl = r'https://cn.bing.com/images/async'
        self.bingparams = {
            'q': self.kw,
            'first': self.page,
            'tsc': 'ImageHoverTitle'
        }
        res = httpx.get(url=self.bingurl,params=self.bingparams,headers={'user-agent': random.choice(self.user_agent_list)},timeout=3)
        if res.status_code!=200:
            print("\033[1;31;40m 网络连接错误! \033[0m")
            return False

        restext = res.content.decode('utf-8')
        resurls=re.findall("murl&quot;:&quot;(.*?)&quot;,&quot;turl&quot;:&quot;.*?&quot;,&quot;t&quot;:&quot;(.*?)&quot;,&quot;mid&quot;:&quot;",restext,re.S)
        i=0
        with ThreadPoolExecutor(max_workers=10) as tp:
            for r in resurls:
                i=i+1
                s=re.sub(u'\ue000', '',r[1])
                s=re.sub(u'\ue001', '', s).split('-')[0].strip()
                s=s.replace('|','_').replace(' ','').replace('*','').replace('/','').replace(r'\\','').replace('.','').replace('?','')
                tp.submit(self.saveimg,urlf=r[0],fname=s)

    def getsogouimg(self):
        self.sogouurl='http://pic.sogou.com/napi/pc/searchList'
        self.sogouparams={
            'mode':1,
            'start': self.page*48,
            'xml_len':48,
            'query': self.kw,
        }

        res=httpx.get(url=self.sogouurl,params=self.sogouparams,headers={'user-agent': random.choice(self.user_agent_list)},timeout=7)
        if res.status_code!=200:
            print("\033[1;31;40m 网络连接错误! \033[0m")
            return False
        data=res.json(strict=False)
        data=data.get('data',{})
        rows = data.get('items',[])
        with ThreadPoolExecutor(max_workers=10) as tp:
            for r in rows:
                jpg_url=r.get('picUrl','')
                jpg_title=r.get('title','')
                jpg_type=r.get('type','.jpg')
                jpg_size=r.get('size','')
                if jpg_url and jpg_title and jpg_type and jpg_size:
                    tp.submit(self.saveimg,urlf=jpg_url,fname=jpg_title,filetype=jpg_type)

    def saveimg(self,urlf='',fname='',filetype='.jpg',mirurlf=''):
        trytotal=3
        if urlf and fname:
            if not os.path.exists('jpg'):
                os.mkdir('jpg')
            fname = fname.replace('|', '_')\
                .replace(' ', '')\
                .replace('*', '')\
                .replace('/', '')\
                .replace('\\', '')\
                .replace('.', '')\
                .replace('?', '').replace('>','').replace('<','').replace('@','').replace('strong','')\
                .replace('#', '').replace(r'\t', '').replace(r'\n', '').replace(':', '').replace('丨','').replace('"','')

            mfile = os.path.join('jpg', fname + filetype)
            for i in range(1, trytotal):
                try:
                    jpgurl=httpx.get(url=urlf,headers={'user-agent': random.choice(self.user_agent_list)},timeout=7)
                    jpgdata=jpgurl.content
                    mirurldata=''
                    if mirurlf:
                        mirurl=httpx.get(url=mirurlf,headers={'user-agent': random.choice(self.user_agent_list)},timeout=7)
                        mirurldata=mirurl.content

                    jpgdata=jpgdata if len(jpgdata)>len(mirurldata) else mirurldata
                    if len(jpgdata) > 8000:
                        with open(mfile,'wb') as f:
                            f.write(jpgdata)
                            print(fname, '  is ok!')
                    else:
                        print("\033[1;31;0m Warning: \033[0m",fname,urlf)
                    jpgurl.close()
                    return True
                except Exception as e:
                    jpgurl.close()
                    if mirurlf:
                        mirurl.close()
                    print(repr(e),urlf,mfile)
                    print('尝试第 %d 次连接....'%i)
                    time.sleep(random.randint(1,5))
                    continue
                return False
        else:
            print('没有文件!')


if __name__ == '__main__':
    kw='陶虹'
    stp=random.randint(1,20)
    page=2
    for i in range(stp,stp+page):
        print('==================第 %d 页==================='%i)
        pc=getimg(kw=kw,page=i,website='bing')
        pc.get()


