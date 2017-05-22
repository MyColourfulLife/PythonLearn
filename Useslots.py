#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
    pass

s = Student()
s.name = 'Mike'
print s.name
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age

s2 = Student()
# print s2.age

def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,None,Student)
s.set_score(100)
print s.score

s2.set_score(99)
print s.score

# 使用__slots__限制类可以绑定的属性 仅对当前类有效,子类不写对子类无效
class Mystudent(object):
    __slots__ = ('name','age')

a = Mystudent()
a.name = 'mIke'
a.age = 25
# a.score = 99