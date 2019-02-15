#!/usr/bin/python
#coding: utf-8
#@Author:liyichao

"""
返回每个单词的首行位置
yield用法

"""
def index_words(text):
    if text:
        yield
    for index,letter in enumerate(text):
        if letter == ' ':
            yield index+1

def main():
    line='i am chinese'
    print(list(index_words(line)))

if __name__ == '__main__':
    main()
    
