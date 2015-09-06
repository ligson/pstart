# coding=UTF-8
'''

@author: ligson
'''


# python中没有重载
class Father:
    name = ""
    age = 10

    def __init__(self, name="test"):
        self.name = name

    def say(self, msg):
        print self.name + ":" + str(msg)


class Son(Father):
    height = 10
    # def say(self,age,msg):
    #    print self.name+"("+str(self.age)+"):"+str(msg)


if __name__ == '__main__':
    father1 = Father()
    # father1.name = "demo1"
    father1.say("helloA")

    father2 = Father()
    father2.name = "demo2"
    father2.say("helloB")

    son1 = Son()
    # son1.say(10, "==")
    son1.say("sfsfsfsf")
