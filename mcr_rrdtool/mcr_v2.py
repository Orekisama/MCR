#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import time
import sys
import gzip
import rrdtool

def format_time(timestamp):
	time_local = time.localtime(timestamp)
	time_local = time.strftime("%Y-%m-%d-%H:%M:%S", time_local)
	return time_local

file_name = os.listdir('/data/proclog/log/squid/access/')
file_name.sort(key=lambda fn:os.path.getmtime('/data/proclog/log/squid/access/' + fn))
file_new = os.path.join('/data/proclog/log/squid/access/', file_name[-1])
last_name = file_new.rpartition('/')[-1]
ungzip_name = last_name.rpartition('.')[0]

with open('/root/mcr/tmplog/' + ungzip_name, 'w+') as w:
	# 转换时间戳并格式化日志
	if '''fc-access.log-01''' in last_name:
		kongge = re.compile(r'\s+')
		for log in gzip.open(file_new):
			unix_time = log.split()[0]
			local_time = format_time(float(unix_time))
			log = log.replace(unix_time, local_time)
			log = log.split('"')[0]
			log = re.sub(kongge, ' ', log)
			w.write(log + '\n')
	else:
		print "Did not find new log file."

	# 统计返回码数量
	count = []
	with open('/root/mcr/tmplog/' + ungzip_name, 'r') as f:
		return_code = ['502', '500', '404', '403', '000']
		log_code = []
		lines = f.readlines()
		for line in lines:
			code = line.split()[3].split('/')[1]
			log_code.append(code)
		for i in return_code:
			result = log_code.count(i)
			count.append(result)

		code_502 = count[0]
		code_500 = count[1]
		code_404 = count[2]
		code_403 = count[3]
		code_000 = count[4]
		starttime = int(time.time())
		# 将数据更新值rrd数据库
		update = rrdtool.updatev('/root/mcr/xls/Flow.rrd', '%s:%s:%s:%s:%s:%s' % (str(starttime), str(code_502), str(code_500), str(code_404), str(code_403), str(code_000)))
		print update
