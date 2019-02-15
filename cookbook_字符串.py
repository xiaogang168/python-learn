#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
"""
这一章主要是字符串的常用技巧
"""
def main():

#正则查找
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    for month, day, year in datepat.findall(text):
        pass
    #方式二
    for m in datepat.finditer(text):
        print(m.groups())

#规定字符串的行宽
    import textwrap
    print(textwrap.fill(s, 70)) #行宽为70个字符
    print(textwrap.fill(s, 40, initial_indent='    ')) #初始字符留空格

#字符串填充
    text.rjust(20,'=')  #左填充
    text.center(20,'*')
    x = 1.2345
    format(x, '=^10.2f')

# 多行正则匹配
        

#使用正则查找替换
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\1-\2', text))
    #方式二
    from calendar import month_abbr
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
    print(datepat.sub(change_date, text))  #注意change_date也是函数

#根据空格、tab符分割字符串
    line = 'asdf fjdk; afed, fjek,asdf,      foo'
    parts = re.split(r'[;,\s]\s*', line)
    print(parts)

#格式化字符串，将指定的内容
    s = '{name} has {n} messages.'
    name = 'Guido'
    n = 37
    print(s.format_map(vars())) #如果n缺失，则程序会报错
    class safesub(dict):
        def __missing__(self, key):
            return '{%s}' % key
    print(s.format_map(safesub(vars()))) #安全的方式


if __name__ == '__main__':
    main()
    
