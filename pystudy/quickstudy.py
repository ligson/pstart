# coding=utf8
# 字符串操作
word = "abcdefghijklmn"
print word[2]
print word[2:5]
print "len is " + str(len(word))

# 范围
a = range(5, 10)
print a

a = range(-10, -5)
print a

# 文件操作
path = "./a.txt"
f = open(path, "w")
f.write("xxxxxx\n")
f.writelines(str(range(1, 10)))
f.close()

f = open(path, "r")
for line in f:
    print line
f.close()

# 控制台输入
s = raw_input("input a string:\n")
if s == "":
    # 异常
    raise Exception("not empty")
print s + "\n"

try:
    print str(int(s))
except ValueError:
    print "not a number"
finally:
    print "GoobBye"


# 类定义
class Base:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)


class Child(Base):
    def plus(self, a, b):
        return a + b


child = Child()
child.add("abd")
print child.data
print child.plus(19, 29)


# 每一个.py文件称为一个module,module之间可以互相导入.请参看以下例子:
# a.py
def add_func(a, b):
    return a + b


# b.py
# from a import add_func # Also can be : import a

print "Import add_func from module a"
print "Result of 1 plus 2 is: "
print add_func(1, 2)  # If using "import a" , then here should be "a.add_func"
