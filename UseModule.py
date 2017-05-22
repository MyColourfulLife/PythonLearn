#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Huang Jiashu'



# 第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
#
# 第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#
# 第6行使用__author__变量把作者写进去
import sys
# from __future__ import unicode_literals

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import json
except ImportError:
    import simplejson as json

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello world!'
    elif len(args)==2:
        print 'hello, %s' % args[1]
    else:
        print 'Too many arguments!'



def _private_1(name):
    return 'hello, %s' % name

def _private_2(name):
    return 'hi, %s' % name
def greeting(name):
    if len(name) > 2:
        return _private_1(name)
    else:
        return _private_2(name)


if __name__ == '__main__':
    test()