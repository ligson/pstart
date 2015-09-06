# coding=UTF-8
'''
Created on 2013年10月14日

@author: ligson
'''


# 元组和列表十分类似,只不过元组和字符串一样是不可变的,即你不能修改元组。help(tuple)
# 元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候,即被使用的元组的值不会改变。
def tupleTest():
    tuple = ("122", "33", "ddd")
    print len(tuple)
    tuple = ("你好", tuple)
    print len(tuple)

    for st in tuple:
        print st

    print tuple[1][1]

    tuple.count("你好")


# list
def listTest():
    list = ["asfd", "asdf"]
    print list
    list.append("dfdf")
    print list.index("asfd")


# map
def mapTest():
    map = {"name": "ligo", "age": 111}
    print map
    print map.keys()
    print map["name"]


if __name__ == '__main__':
    # tupleTest()
    # listTest()
    mapTest()
