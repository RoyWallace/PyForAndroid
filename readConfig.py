import configparser
import string, os, sys

cf = configparser.ConfigParser()

cf.read("E:\github\PyForAndroid\init.conf")

#return all section
secs = cf.sections()
print ('sections:', secs)

opts = cf.options("db")
print ('options:', opts)