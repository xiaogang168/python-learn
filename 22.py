#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
"""
 使用辅助类维护程序的状态
"""
#原始版本
class SimpleGradebook(object):
    def __init__(self):
        self._grades={}
    def add_student(self,name):
        self._grades[name]=[]
    def report_grade(self,name,score):
        self._grades[name].append(score)
    def average_grade(self,name):
        grades=self._grades[name]
        return sum(grades)/len(grades)

#增加需求之后的辅助版本
from collections import namedtuple
Grade=namedtuple('Grade',('score','weight'))

class Subject(object):
    def __init__(self):
        self._grades=[]
    def report_grades(self,score,weight):
        self._grades.append(Grade(score,weight))
    def average_grade(self):
        total,total_weight=0,0
        for grade in self._grades:
            total+=grade.score * grade.weight
            total_weight+=grade.weight
        return total/total_weight

class Student(object):
    def __init__(self):
        self._subjects={}
    def subject(self,name):
        if name not in self._subjects:
            self._subjects[name]=Subject()
        return self._subjects[name]
    def average_grade(self):
        total,count=0,0
        for subject in self._subjects.values():
            total+=subject.average_grade()
            count+=1
        return total/count

class GradeBook(object):
    def __init__(self):
        self._students={}
    def student(self,name):
        if name not in self._students:
            self._students[name]=Student()
        return self._students[name]

def main():
    book=GradeBook()
    alert=book.student('einstin')
    math=alert.subject('math')
    math.report_grades(80,0.1)
    print(alert.average_grade())

if __name__  =='__main__':
    main()
