#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name):
        self.name =  name
    def __str__(self):
        return 'Student object (name:%s)' % self.name

# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
    __repr__ = __str__

print Student('mike')

# __iter__如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    # 可以通过下标获取
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# for n in Fib():
#     print n
f = Fib()
print f[4]

print f[0:10]


class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
print s.age()
# print s.name


class Chain(object):
    def __init__(self,path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path,path))
    def __str__(self):
        return self._path
print Chain().status.user.timeline.list

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print 'my name si %s.' % self.name

s = Student('Mike')
s()

print callable(max)
print callable([1,2,3])