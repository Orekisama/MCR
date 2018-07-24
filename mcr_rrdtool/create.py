#!/usr/bin/python2.6.6
# -*- coding: utf-8 -*-

import rrdtool
import time

cur_time = str(int(time.time()))
rrd = rrdtool.create('./xls/Flow.rrd', '--step', '300', '--start', cur_time,
                     'DS:code502:GAUGE:600:0:1000000',
                     'DS:code500:GAUGE:600:0:1000000',
                     'DS:code404:GAUGE:600:0:1000000',
                     'DS:code403:GAUGE:600:0:1000000',
                     'DS:code000:GAUGE:600:0:1000000',
                     
                     'RRA:AVERAGE:0.5:1:600',
                     'RRA:AVERAGE:0.5:6:700',
                     'RRA:AVERAGE:0.5:24:775',
                     'RRA:AVERAGE:0.5:288:797',
                     'RRA:MAX:0.5:1:600',
                     'RRA:MAX:0.5:6:700',
                     'RRA:MAX:0.5:24:775',
                     'RRA:MAX:0.5:444:797',
                     'RRA:MIN:0.5:1:600',
                     'RRA:MIN:0.5:6:700',
                     'RRA:MIN:0.5:24:775',
                     'RRA:MIN:0.5:444:797)
if rrd:
    print rrdtool.error()
