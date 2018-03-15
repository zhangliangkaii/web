#/usr/bin/env python
#coding=utf8
 
import http
import hashlib
import urllib
import random
import json

appid = '20180314000135302'
secretKey = 'maNhQB1uqAsbznsNAgyM'


def TranslateByBaidu(text, fromLang='auto', toLang = 'zh'):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = text
    salt = random.randint(32768, 65536)
    
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.request.quote(q)+'&from='+\
    fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        result = response.read()
        data = json.loads(result)
        answer = data['trans_result'][0]['dst'] 
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return answer

if(__name__ == '__main__'):
    TranslateByBaidu('apple')