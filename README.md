# MCR
monitor return code of squid access logs
实现过程（Python2.6 + rrdtool）：
1)	针对fc的access日志进行监控(系统会每5分钟会生成一个.gz的squid log压缩文件)
2)	对.gz日志文件进行格式化并统计的Return Code
3)	利用rrdtool存储数据并画图
4)	使用httpd发布一个监控页面（return_code.html, 8080端口），5分钟自动刷新一次
