from xml.etree import ElementTree as ET 
try:  
    tree = ET.parse("Campaign_Config.xml") #打开xml文档  
    root = tree.getroot() #获得root节点  
except Exception, e:  
    print "Error: cannot parse file: Campaign_Config.xml."  
    return -1     
eles_Paramter = root.find("Parameters").findall("Parameter") #找到Parameters节点下的所有Parameter节点  
for eachEle in eles_Paramter:  
    if eachEle.attrib.has_key("isControlled"): #如果有个节点拥有属性isControlledPSUsed  
        eachEle.set("isControlled", "False")    #就将该属性设置为False  
tree.write("Campaign_Config.xml")   #最后将结果写回文件  