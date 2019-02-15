"""
1.json
2.mysql
3.hashlib
4.time
5.zipfile
6.log

"""
import json

d={'a':'1','b':'2','abc':'123'}

#print json.dumps(d)  #返回json字符串
ft=open('json.txt','w')
#json.dump(d,ft)  #

js=json.load(ft)  #报错：文件不存在？？
js=json.load(open('json.txt'))
#js=json.loads('123')  #返回python对象
print type(js)

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()

#f=open('txt','r')
#m={}
##print f.readline()
#while True:
    #line=f.readline()
    #if line.__len__() ==0:
        #break
    #l=line.split()
    ##m[l[0]]=[]
    ##print l[0],l[1]
    #if m.has_key(l[0]):
        #m[l[0]].append(l[1])
    #else:
        #m[l[0]]=[l[1]]
#print m

###################################
import h

h.fib(10)

from h import fib,fib2
fib(20)

from h import *  #加载所有不易—__开头的函数，不建议

#计算hash值
import hashlib
#SHA1、SHA224、SHA256、SHA384、SHA512、MD5
h=hashlib.new('md5', string='20170110012501.bjmggsn2.dat')
m=hashlib.md5()
m.update('20170110012501.bjmggsn2.dat')
print m.hexdigest()
print h
print h.digest(),h.hexdigest()
print h.digest_size
print len(h.digest()),len(h.hexdigest())
print len ('20170110012501.bjmggsn2.dat')

#计算多个hash值

#python读取大文件

import time

starttime=time.time()

#1  0.253999948502  0.566999912262
with open(r'C:\Users\lenovo\Desktop\python\upload.log') as f:
    for line in f:
        line.find('Downloading')
f.close()

#2  0.291999816895  0.540999889374
#f=open(r'C:\Users\lenovo\Desktop\python\upload.log')
#for line in f.readlines():
    #line.find('Downloading')
#f.close()

#3 0.526000022888   1.02900004387
#f=open(r'C:\Users\lenovo\Desktop\python\upload.log')
#line=f.readline()
#while line:
    #line.find('Downloading')
    #line=f.readline()
#f.close()

stoptime=time.time()

print 'cost is {0}'.format(stoptime-starttime)

import threading,zipfile,logging

class AsycZip(threading.Thread):
    def __init__(self,infile,outfile):
        threading.Thread.__init__(self)
        self.infile=infile
        self.outfile=outfile
    def run(self):
        f=zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_STORED)
        f.write(self.infile)
        f.close()
        logging.info('zipfile done')
        #print 'zipfile done'
backgroup=AsycZip('1.txt','1.txt.zip')
backgroup.start()
#print 'start'
logging.warn('start')
backgroup.join()
#print 'done'
logging.error('end')







