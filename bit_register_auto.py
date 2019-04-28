#!/usr/bin/env python
# -*- coding:utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
import re
import time
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')
entry_uri = 'https://jinshuju.net/f/OXacm8'
cookie_filename = 'cookies.txt'
configure_filename = 'configure.txt'

if __name__ == '__main__':
    configure_content = open(configure_filename, 'rb').read()
    cookie_content = open(cookie_filename, 'rb').read()
    configure_dt=datetime.datetime.now().strftime('%Y-%m-%d')
    dt_index = re.search('\d{4}-\d{2}-\d{2}', configure_content).span()
    configure_content = configure_content[:dt_index[0]] + configure_dt + configure_content[dt_index[1]:]
    try_count = 0
    register_code=None
    success_info=None
    response_code=None
    register_dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    item_list=configure_content.split('&')
    print u'上传的字段值为：'
    for item in item_list:
        print (u'第%d个字段值为：%s'%(item_list.index(item),item[item.index('=')+1:])),
    print ''
    while True:
        try_count += 1
        json_obj = None
        try:
            print u"尝试第%d次自动签到....."%try_count
            request = urllib2.Request(url = entry_uri, data = configure_content)
            request.add_header('Host', 'jinshuju.net')
            request.add_header('Connection', 'keep-alive')
            request.add_header('Origin', 'https://jinshuju.net')
            request.add_header('Upgrade-Insecure-Requests', '1')
            request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3')
            request.add_header('Referer', 'https://jinshuju.net/f/OXacm8')
            #request.add_header('Accept-Encoding', 'gzip, deflate, br')
            request.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
            request.add_header('Content-Type', 'application/x-www-form-urlencoded')
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36')
            request.add_header('Cookie', cookie_content)
            response = urllib2.urlopen(request)
            #response_text = response.getcode()
            response_code=response.getcode()
            html_doc = response.read()

            soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
            register_code = soup.find('p',attrs={'class': 'form-title'}).text
            success_info = soup.find('div',attrs={'class':'message'}).text.strip()

        except:
            status = "___timeout"

        if response_code==200 and success_info==u'提交成功':

            print ''
            print u'%s,签到时间为：%s,服务器返回状态码为：%s，返回结果为：%s'%(register_code,register_dt,response_code,success_info)
            break
        else:
            time.sleep(10)