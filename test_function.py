# -*- coding:utf-8
import datetime
import re
configure_filename = 'configure.txt'
configure_content = open(configure_filename, 'rb').read()
print(configure_content)
dt_index=re.search('\d{4}-\d{2}-\d{2}',configure_content).span()
configure_dt = datetime.datetime.now().strftime('%Y-%m-%d')
configure_dt = '2019-01-01'
configure_content=configure_content[:dt_index[0]]+configure_dt+configure_content[dt_index[1]:]
print(configure_content)

