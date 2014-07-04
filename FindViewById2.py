#encoding=utf-8
import sys
import os
from xml.etree import ElementTree as ET
def classdef(str,filename):
	fileS = filename.split("\\")
	fileName = fileS[len(fileS) - 1].split("_")[0].capitalize() + "Activity"
	classdef = "public class " + fileName +" extends Activity {\n" + str + "\n}"
	return classdef
    
def classname(filename):
    fileS = filename.split("\\")
    fileName = fileS[0] + "\\" + fileS[len(fileS) - 1].split("_")[0].capitalize() + "Activity"
    print("fileName: ",fileName)
    return fileName

def declare(temp,defineType):
	item = temp.split('/')[1]
	tempR = "\tprivate " + defineType + " " + item + ";"
	return tempR

def implementString(temp,defineType):
	item = temp.split('/')[1]
	tempR = "\t\t" + item + " = (" + defineType +")findViewById(R.id."+ item + ");"
	return tempR

def findAllView(str):
	findAllViewStr = "\tprivate void findAllView(){" + "\n" + str + "\n" + "\t}"
	return findAllViewStr

def make_file(fileName):
	#结果列表
	resultDef = []
	resultImple = []

	per=ET.parse(fileName)

	for typeT in typelist:
		p=per.findall("./"+typeT)
		for oneper in p:  
			temp = oneper.get(prefix+'id')
			tempD = declare(temp,typeT)
			tempI = implementString(temp,typeT)
			resultDef.append(tempD)
			resultImple.append(tempI)

	finalStringI = '\n'.join(resultImple)
	finalStringD = '\n'.join(resultDef)

	string1 = findAllView(finalStringI)
	string2 = finalStringD + "\n\n"+ string1
	string3 = classdef(string2,fileName)
	return string3

#输入的目录路径
dir_path = sys.argv[1]

#输出指定的文件夹目录
dir_write = "D://work//github//workspace-py//PyForAndroid"

#固定前缀
prefix = "{http://schemas.android.com/apk/res/android}"

#需要执行批处理的文件
fileTypelist = ['activity' , 'item']

#需要找的标签
typelist = ['TextView' , 'Button' , 'ImageView' , 'ImageButton' , 'EditText' , 'LinearLayout' , 'RelativeLayout' , 'ListView' , 'GridView' , 'ScrollView']

#读取文件的路径
for root, dirs, files in os.walk(dir_path):
    for f in files:
        fileFullName = os.path.join(root, f)
        fileNameList = fileFullName[len(fileFullName) - 1].split("_")
        for fileName in fileNameList :
            print(fileName)
        if(fileFullName[len(fileFullName) - 1].split("_")[0] == fileTypelist[0]) :
            print(fileTypelist[0] + "  " + fileFullName[len(fileFullName) - 1].split("_")[1])
            
        print (fileFullName)
        str = make_file(fileFullName)
        file_path_write = open(classname(fileFullName) + ".java","w")
        file_path_write.write(str)
        file_path_write.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        