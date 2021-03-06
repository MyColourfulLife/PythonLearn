#!/usr/bin/env python
#-*- coding:utf-8 -*-


def fn(self,name = 'world'):
    print ('hello, %s' % name)

Hello = type('Hello',(object,),dict(hello = fn)) #创建Hello class
h = Hello()
h.hello()
print type(Hello)
print type(h)
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls,name,bases,attrs)
class Mylist(list):
    __metaclass__ = ListMetaclass #指示使用ListMetaclass来定制类

L = Mylist()
L.add(1)
print L

# l = list()
# l.add(1)


# 1.定义Field类,它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field基础上定义各类型的Field 比如StringField,IntegerField等等

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

# 编写元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)
# 基类 Model
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model,self).__init__(self,**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r" 'Model' objiect has no attribute '%s' " % key)
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args   = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)

print '========================'
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()