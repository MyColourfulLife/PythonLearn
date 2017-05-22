class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        self.flower = 8

    def print_score(self):
        print '%s:%s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('aili',100)
bart.print_score()
print hasattr(bart,'flower')