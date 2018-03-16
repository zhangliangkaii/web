# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 09:45:21 2018

@author: zhangliangkai
"""

from urllib import request
from urllib import error

if __name__ == '__main__':
#    url = 'http://www.csdn.net/'
#    head = {}
#    head['User-Agent'] = 'Mozilla/5.0 (' + \
#        'Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
#    req = request.Request(url, headers=head)
    url = 'http://www.whatismyip.com.tw/'
    proxy = {'http': '171.81.31.76:808'}
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    opener.addheaders = [(
            'User-Agent',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) ' +
            'Gecko/20100101 Firefox/21.0'
            )]
    request.install_opener(opener)
    
    try:
        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        if(hasattr(e, 'code')):
            print('HTTPError')
            print(e.reason)
        elif(hasattr(e, 'reason')):
            print('URLError')
            print(e.reason)
