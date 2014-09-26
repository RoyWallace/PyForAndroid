#encoding=utf-8
import sys
import os
import configparser
from xml.etree import ElementTree as ET
 
def mimport():
    importstr = "import android.os.Bundle;\nimport android.app.Activity;\nimport android.view.LayoutInflater;\nimport android.view.View;\nimport android.view.ViewGroup;\nimport android.widget.Button;\nimport android.widget.EditText;\nimport android.widget.GridView;\nimport android.widget.ImageButton;\nimport android.widget.ImageView;\nimport android.widget.LinearLayout;\nimport android.widget.ListView;\nimport android.widget.RelativeLayout;\nimport android.widget.ScrollView;\nimport android.widget.TextView;\n\n"
    return importstr
    
def moncreate():
    str="\n@Override\nprotected void onCreate(Bundle savedInstanceState) {\nsuper.onCreate(savedInstanceState);\nsetContentView(R.layout.activity_main);\n}"
    return str

def classdef(str,filename):
    fileS = filename.split("\\")
    className = fileS[len(fileS) - 1].split("_")[0].capitalize() + "Adapter"
    classdef = mimport() + "public class " + className +" extends BaseAdapter {\nprivate Context context;\nprivate List<Object> objectList = new ArrayList<Object>();\n"+ "\npublic "+className +"(Context context, List<Object> objectList){\nthis.context = context;\nthis.objectList = objectList;\n}"
    return classdef
    
def method():
    methodStr = "@Override\npublic int getCount() {\nreturn commentList.size();\n}\n@Override\npublic Object getItem(int i) {\nreturn null;\nt}\n@Override\npublic long getItemId(int i) {\nreturn 0;\n}\n"
    return methodStr
    
def getView(findAllViewStr):
    getViewStr = "\t@verride\tpublic View getView(int position,View view,ViewGroup viewGroup){\t\tViewHolder holder = null;\t\tif(view== null){\nview = LayoutInflater.from(context).inflate(R.layout.item_comment,null);\nholder = new ViewHolder();\n" + findAllViewStr +"view.setTag(holder);\n}else{\nholder = (ViewHolder)view.getTag();\n}\n" + setData() + "\nreturn view;\n}\n"
    return getViewStr
    
def classname(filename):
    fileS = filename.split("\\")
    fileName = fileS[0] + "\\" + fileS[len(fileS) - 1].split("_")[0].capitalize() + "Adapter"
    print(fileName)
    return fileName

def declare(temp,defineType):
    item = temp.split('/')[1]
    tempR = "\t" + defineType + " " + item + ";"
    return tempR
    
def holder():
    holderStr = "\tprivate class ViewHolder{" + "\n" + str + "\n" + "\t}"
    return holderStr

def implementString(temp,defineType):
    item = temp.split('/')[1]
    tempR = "\t\t" + item + " = (" + defineType + ")findViewById(R.id."+ item + ");"
    return tempR

def findAllView(str):
    findAllViewStr = "\tprivate void findAllView(){" + "\n" + str + "\n" + "\t}"
    return findAllViewStr

# def make_file(fileName):
#     #结果列表
#     resultDef = []
#     resultImple = []

#     per=ET.parse(fileName)

#     for typeT in typelist:
#         p=per.findall("./"+typeT)
#         for oneper in p:  
#             temp = oneper.get(prefix+'id')
#             tempD = declare(temp,typeT)
#             tempI = implementString(temp,typeT)
#             resultDef.append(tempD)
#             resultImple.append(tempI)

#     finalStringI = '\n'.join(resultImple)
#     finalStringD = '\n'.join(resultDef)

#     string1 = findAllView(finalStringI)
#     string2 = finalStringD + "\n\n"+ string1
#     string3 = classdef(string2,fileName)
#     return string3
    
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

    string1 = getView(finalStringI)
    string2 = finalStringD + "\n\n"+ string1
    string3 = classdef(string2,fileName)
    return string3

#输入的目录路径
#dir_path = sys.argv[1]
dir_path = "E:/github/PyForAndroid/xml_for_test"

# #指定包名
# package_name = sys.argv[1]

#输出指定的文件夹目录
dir_write = "E://github//PyForAndroid"

#固定前缀
prefix = "{http://schemas.android.com/apk/res/android}"

#需要执行批处理的文件
fileTypelist = ['activity' , 'item']

#需要找的标签
#typelist = ['TextView' , 'Button' , 'ImageView' , 'ImageButton' , 'EditText' , 'LinearLayout' , 'RelativeLayout' , 'ListView' , 'GridView' , 'ScrollView']

#初始化读取配置文件对象
cf = configparser.ConfigParser()
cf.read('E:\github\PyForAndroid\init.conf')
#需要找的标签
typelist = cf.sections()

#读取文件的路径
for root, dirs, files in os.walk(dir_path):
    for f in files:
        fileFullName = os.path.join(root, f)
        print(fileFullName)
        #get file Name
        fileName = fileFullName.split("\\")[1]
        print(fileName)
        nameList = fileName.split("_")
        #get file Type
        fileType = fileName.split("_")[1].split(".")[0]
        print(fileType)
        #new file name
        newFileName = nameList[0].capitalize() + fileType.capitalize()
        print(newFileName)
        
        # for fileName in fileNameList :
        #     print(fileName)
        # if(fileType == fileTypelist[1]) :
        #     print(fileTypelist[1])
            
        # print (fileFullName)
        # str = make_file(fileFullName)
        # file_path_write = open(classname(fileFullName) + ".java","w")
        # file_path_write.write(str)
        # file_path_write.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        