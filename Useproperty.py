# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an interger!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# a = Student()
# a.set_score(60)
# print a.get_score()
# # a.set_score(9999)

class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def socre(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
# s.score = 90
print s.score