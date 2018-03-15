# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:39:42 2018

@author: zhangliangkai
"""

import itertools
import urllib
import re


def download(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
    except urllib.error.URLError as e:
        print('Download error', e.reason)
        html = ''
        if(num_retries > 0):
            if(hasattr(e, 'code') & 500 <= e.code <= 600):
                return download(url, user_agent, num_retries-1)
    return html.decode('utf-8')


# download('http://httpstat.us/500')


def crawl_sitemap(url):
    sitemap = download(url+'/sitemap.xml')
    r = re.compile(url+'.*?\.html')
    links = re.findall(r, sitemap)
    for link in links:
        html = download(link)


# crawl_sitemap('http://www.ranzhi.org')
