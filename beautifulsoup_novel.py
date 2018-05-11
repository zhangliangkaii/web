# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:18:59 2018

@author: zhangliangkai
"""

import urllib
from bs4 import BeautifulSoup
import sys

if __name__ == '__main__':
    url = 'http://www.biqukan.com/1_1094/'
    header = {}
    header['User_Agent'] = 'Mozilla/5.0 (' +\
        'Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
    target_req = urllib.request.Request(url, headers=header)
    target_response = urllib.request.urlopen(target_req)
    target_html = target_response.read().decode('gbk', 'ignore')
    target_response.close()
    list_soup = BeautifulSoup(target_html, 'lxml')
    chapters = list_soup.find_all('div', class_='listmain')
    chapter_list = BeautifulSoup(str(chapters), 'lxml')
    begin_flag = False
    number = len(chapter_list.dl.contents) / 2
    index = 1
    f = open('D://novel.txt', 'w')
    for child in chapter_list.dl.children:
        if child != '\n':
            if child.string == '《一念永恒》正文卷':
                begin_flag = True
            if begin_flag and child.a is not None:
                download_url = 'http://www.biqukan.com' + child.a.get('href')
                download_name = child.string
                download_request = urllib.request.Request(
                        download_url, headers=header)
                try:
                    download_response = urllib.request.urlopen(
                            download_request, timeout=10)
                    html = download_response.read().decode('gbk', 'ignore')
                    download_response.close()
                except Exception as e:
                    download_response = urllib.request.urlopen(
                            download_request, timeout=10)
                    html = download_response.read().decode('gbk', 'ignore')
                    download_response.close()
                soup_text = BeautifulSoup(html, 'lxml')
                content = soup_text.find_all(id='content', class_='showtxt')
                text = BeautifulSoup(str(content), 'lxml')
                f.write(download_name + '\n')
                f.write(
                    text.div.text.replace('\xa0', ' ').replace('     ', '\n'))
                f.write('\n\n\n')
                sys.stdout.write('已下载:%.3f%%' % float(index/number) +
                                 '目前章节:%s' % download_name + '\r')
                sys.stdout.flush()
                index = index + 1
    f.close()

#download_url = 'http://www.biqukan.com/1_1094/5386269.html'
#download_request = urllib.request.Request(download_url, headers=header)
#download_response = urllib.request.urlopen(download_request)
#html = download_response.read().decode('gbk', 'ignore')
#soup_text = BeautifulSoup(html, 'lxml')
#content = soup_text.find_all(id='content', class_='showtxt')
#text = BeautifulSoup(str(content), 'lxml')
#print(text.div.text.replace('\xa0', ' ').replace('     ', '\n'))
