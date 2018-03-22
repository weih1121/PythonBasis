#什么是函数？
#将一段代码逻辑，通过特殊的语法组织起来，可以有参数，返回值，并且可以在函数外部被调用

def MySum(x, y):    #定义函数 def关键字 MySum函数名 x, y参数
    return x + y

print(MySum(5, 6))  #函数调用

#什么是装饰器？装饰器本质上就是一个函数
#作用:用来装饰别的函数，给其他的函数附加新的功能。
#两个原则:1.不能修改被装饰的函数的原代码 2.不能改变被装饰函数调用方式
#应用场景:比如插入日志，性能测试，处理事务

#有一个功能，要测试一个函数的大概运行时间
import time

def f():
    print("i am f")
    time.sleep(2)

#第一种方法 源码改变了 调用方式改变了
def new_f():
    s_time = time.time()    #开始时间
    f()
    e_time = time.time()
    print("耗时 %s秒" % (e_time - s_time))

new_f() #调用new_f()

#第二种方法:
def new_f1(func):
    def warpper1():
        s_time1 = time.time()
        func()
        e_time1 = time.time()
        print("{funcname}耗时 {time}秒" .format(funcname = func.__name__, time = (e_time1 - s_time1)))
    return warpper1

@new_f1 #相当于f = new_f1(f1) f()    #若不通过这行代码，可以去掉46 47行代码注释效果一样
def f1():
    print("i am f1")
    time.sleep(2)

#若正常通过new_f1()获得函数的执行时间需做如下操作:
##f1 = new_f1(f1)        #n = warpper1
f1()
#理解装饰器之前需要理解三句话:
#1.函数即变量 是一个函数对象，函数也可以作为函数参数或者返回值
#2.高阶函数:以函数作为参数或者返回值的函数
#3.嵌套函数/函数嵌套:函数里边定义函数 

#装饰器 = 高阶函数 + 嵌套函数
def log(func):
    def wrapper(*args, **kwargs):                   #动态参数
        print("begin call %s" % func.__name__)
        tmp = func(*args, **kwargs)
        print("after call %s" % func.__name__)
    return wrapper