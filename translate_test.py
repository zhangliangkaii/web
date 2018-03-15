# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:08:21 2018

@author: zhangliangkai
"""

from urllib import request
from urllib import parse
import json

if __name__ == 'main':
    Request_URL = 'http://fanyi.youdao.com/' \
    'translate_o?smartresult=dict&smartresult=rule'
    Form_Data = {}
    Form_Data['type'] = 'AUTO'
    Form_Data['i'] = 'jack'
    Form_Data['doctype'] = 'json'
    Form_Data['xmlVersion'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['ue'] = 'UTF-8'
    Form_Data['action'] = 'FY_BY_REALTIME'
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL, data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
