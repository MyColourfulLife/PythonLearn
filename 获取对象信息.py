#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类型判断type
print type(123)
print type('str')
print type(None)
print type(abs)
class Animal(object):
    pass
a = Animal()
print type(a)

print type(123) == type(456)
print type('abc') == type('123')
print type(123) == type('abc')

import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType
print type(int) == type(str) == types.TypeType

# 使用isinstance

a = [1,2,3]
print isinstance(a,list)

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
print isinstance('a',(str, unicode))
print isinstance(u'a',basestring)

# 使用dir()获取对象所有的属性和方法
# print dir('abc')

print len('abc')
print 'abc'.__len__()


class Myobject(object):
    def __len__(self):
        return 100
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = Myobject()
print len(obj)

print '...................'
print hasattr(obj, 'x')
print obj.x

print hasattr(obj,'y')
setattr(obj,'y',19)
print hasattr(obj,'y')
print getattr(obj,'y')
print obj.y

print getattr(obj,'z',404)

print hasattr(obj,'power')
fn = getattr(obj,'power')
print fn()
