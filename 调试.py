#!/usr/bin/env python
#-*- coding: utf-8 -*-

'调试方法'
# 1.简单粗暴,使用print打印变量
# 2.断言 凡是用print来辅助查看的地方 都可以用断言assert替代
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero'
#     return 10/n
#
# foo(0)

# 3.logging 和 assert相比,logging不会抛出错误,而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' %n)
print 10/n

# 4.pdb 启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态python -m pdb err.py
# 可以断点调试,但是非常麻烦
# 5.pdb.set_trace() 不需要单步执行,我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
# 6.IDE如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm