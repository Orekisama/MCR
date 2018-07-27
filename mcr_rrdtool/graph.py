#!/usr/bin/python2.6.6
# -*- coding: utf-8 -*-

import rrdtool
import time

title = "Squid Return Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("/root/mcr/png/RCM.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title,
              "DEF:502=./xls/Flow.rrd:code502:MAX",
              "DEF:500=./xls/Flow.rrd:code500:MAX",
              "DEF:403=./xls/Flow.rrd:code403:MAX",
              "DEF:404=./xls/Flow.rrd:code404:MAX",
              "DEF:000=./xls/Flow.rrd:code000:MAX",
              "LINE1:502#0000FF:Code_502",
              "LINE1:500#FF0000:Code_500",
              "LINE1:404#FFFF00:Code_404",
              "LINE1:403#215E21:Code_403",
              "LINE1:000#00FF00:Code_000")

title_502 = "Squid Return 502 Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("/root/mcr/png/502.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title_502,
              "DEF:502=./xls/Flow.rrd:code502:MAX",
              "LINE1:502#0000FF:Code_502")

title_500 = "Squid Return 500 Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("/root/mcr/png/500.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title_500,
              "DEF:500=./xls/Flow.rrd:code500:MAX",
              "LINE1:500#0000FF:Code_500")

title_403 = "Squid Return 403 Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("/root/mcr/png/403.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title_403,
              "DEF:403=./xls/Flow.rrd:code403:MAX",
              "LINE1:403#0000FF:Code_403")

title_404 = "Squid Return 404 Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("/root/mcr/png/404.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title_404,
              "DEF:404=./xls/Flow.rrd:code404:MAX",
              "LINE1:404#0000FF:Code_404")

title_000 = "Squid Return 000 Code Statics (" + time.strftime('%Y-%m-%d', time.localtime(time.time())) + ")"
rrdtool.graph("/root/mcr/png/000.png", "--start", "-1d",
              "--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H",
              "--width", "650", "--height", "230", "--title", title_000,
              "DEF:000=./xls/Flow.rrd:code000:MAX",
              "LINE1:000#0000FF:Code_000")