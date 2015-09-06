# coding=utf8
'''
Created on 2013年10月12日

@author: Administrator
'''

'''
文件测试
'''


import os
import subprocess



# 获取当前路径
print os.getcwd()

files = os.listdir("E:/")

for file in files:
    filepath = "E:/" + file
    fileName = str(file).decode("gbk").encode("utf8")
    fileIsFile = os.path.isfile(filepath) and "文件" or "目录"
    fileExsit = os.path.exists(filepath) and "存在" or "不存在"
    fileSize = str(os.path.getsize(filepath))
    outs = fileName + "---" + fileSize + "==" + fileIsFile + "===" + fileExsit
    print outs  

print os.name

# print os.system("notepad")

# subprocess.call("cmd")

# 定义一个方法
def toUTF8(string):
    return str(string).decode("gbk").encode("utf8")

result = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT);
for line in result.stdout.readlines():
    print str(line).decode("gbk").encode("utf8")
    

#测试文件读
file = "E:/1.txt"
fp = open(file, "r+")
result = fp.readlines()
for line in result:
    print toUTF8(line)
fp.close()

#测试文件写
fp = open(file, "a")
fp.write("\n这是一个测试爱爱爱".decode("utf8").encode("gbk"))
fp.close()
    

