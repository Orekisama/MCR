#!/usr/bin/python2.6.6
# -*- coding: utf-8 -*-

import rrdtool
import time

title = "Squid Return Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("./flow.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title,
              "DEF:502=./xls/Flow.rrd:code502:AVERAGE",
              "DEF:500=./xls/Flow.rrd:code500:AVERAGE",
              "DEF:404=./xls/Flow.rrd:code404:AVERAGE",
              "DEF:403=./xls/Flow.rrd:code403:AVERAGE",
              "DEF:000=./xls/Flow.rrd:code000:AVERAGE",
              "LINE1:502#FF8833:Code_502",  
              "LINE1:500#FF0000:Code_500",  
              "LINE1:404#00FF00:Code_404",
              "LINE1:403#215E21:Code_403",
              "LINE1:000#5C4033:Code_000")
