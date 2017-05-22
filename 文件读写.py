#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
f = open('/Users/michael/test.txt', 'r')
# 如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
f.read()
# 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
f.close()
# Python引入了with语句来自动帮我们调用close()方法：
with open('/path/to/file', 'r') as f:
    print f.read()
# Withopen和 try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。


# 二进制文件前面讲的默认都是读取文本文件，并且是ASCII编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

f = open('/Users/michael/test.jpg', 'rb')
f.read()

# 字符编码要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
f = open('/Users/michael/gbk.txt', 'rb')
u = f.read().decode('gbk')
# Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'

# 写文件写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()