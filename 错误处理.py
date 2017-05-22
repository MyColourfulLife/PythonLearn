#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    print 'try....'
    r = 10/int('a')
    print 'result:',r
except ValueError,e:
    print 'valueError:',e
except ZeroDivisionError,e:
    print 'except:',e
else:
    print 'no error'

finally:
    print 'finally...'
print 'End'


# Python内置的logging模块可以非常容易地记录错误信息：
import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError,e:
        print 'Error!',e
        logging.exception(e)
    finally:
        print 'finally'

main()


# 抛出错误
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value:%s' % s)
    return 10/n
foo('0')


def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('0')

main()

# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个Error!后，又把错误通过raise语句抛出去了，这不有病么？
#
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
#
# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')