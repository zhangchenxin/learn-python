class Student():
    def __init__(self, name="noname", age= 18):
        self.name = name
        self.age = age

    def Say(self):
        print("My name is {0} , I am {1} years old".format(self.name, self.age))

def sayhello():
    print("生活是美好的,好好享受吧")
if  __name__ == '__main__':# 表示文件名称为自己的名称,建议每段程序的入口都可以是这句话
    print("我不需要在函数或者类中,我就是这么厉害")