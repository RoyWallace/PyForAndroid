#encoding=utf-8
from xml.etree import ElementTree as ET

def modify(temp,defineType):
	item = temp.split('/')[1]
	tempR = defineType + " " +item + " = (" + defineType +")findViewById(R.id."+ item + ");"
	return tempR

#读取文件的路径
read_file = 'D:/work/github/workspace-py/PyForAndroid/xml_for_test/activity_main.xml'
#写入的文件路径
file_path = open("D://work//github//workspace-py//PyForAndroid//result.java","w")
#固定前缀
prefix = "{http://schemas.android.com/apk/res/android}"

#结果列表
result = []

#需要找的标签
typelist = ['TextView' , 'Button']

per=ET.parse(read_file)

for typeT in typelist:
	p=per.findall("./"+typeT)
	for oneper in p:  
		temp = oneper.get(prefix+'id')
		temp = modify(temp,typeT)
		print ("temp is ", temp)
		result.append(str(temp))

print (result)
finalString = '\n'.join(result)
file_path.write(finalString)
file_path.close()


    
    