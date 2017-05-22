#!/usr/bin/env python
#-*- coding:utf-8 -*-


# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
#
# Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。用的时候，先尝试导入cPickle，如果失败，再导入pickle：


try:
    import cPickle as pickle
except ImportError:
    import pickle

# 首先，我们尝试把一个对象序列化并写入文件：
d = dict(name = 'bob',age = 20, score = 88)
pickle.dumps(d)


# pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

# 可以先把内容读到一个str，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
# 我们打开另一个Python命令行来反序列化刚才保存的对象：

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d

# 此序列化问题，就是它只能用于Python
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式 比如JOSN

import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。


# 序列化自定义类

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print json.dumps(s,default=student2dict)
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON。

# 下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print json.dumps(s,default=lambda obj:obj.__dict__)
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
