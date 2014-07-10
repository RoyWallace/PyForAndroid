#coding=utf-8
import json
import sys , os 
#f = file('E:\github\PyForAndroid\\table.json')
#source = f.read()
#target = json.JSONDecoder().decode(source)
#print (target)
class Web(object):
    def _init_(self,name,email,homepage):
        self.name = name
        self.email = email
        self.homepage = homepage
    
    def _repr_(self):
        return 'Web object name :  %s, email : %s , homepage : %s' %(self.name,self.email,self.homepage)
        
def object2web(obj):
    web = {}
    web['']

jsonobject = json.load(open('E:/github/PyForAndroid/test.json'))
print ("list : ",jsonobject)
web1 = jsonobject[0]
print ("object : ",web1)

name = web1[1]
print ("name : ",name) 



