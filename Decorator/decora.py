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

def f():                #被测试函数 下列fn()函数原型均基于此
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
def new_f1(func):           #运行时间
    def warpper1():
        s_time1 = time.time()
        func()
        e_time1 = time.time()
        print("{funcname}耗时 {time}秒" .format(funcname = func.__name__, time = (e_time1 - s_time1)))
    return warpper1

@new_f1 #相当于f1 = new_f1(f1) 在f()掉用的时候直接执行warpper1()函数 
def f1():                      #若不通过上行代码，可以去掉45行代码注释效果一样
    print("i am f1")
    time.sleep(2)

#若正常通过new_f1()获得函数的执行时间需做如下操作:
#f1 = new_f1(f1)        #f1 = warpper1
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

#若果一个函数需要增加两个或多个功能 使用多重装饰

def log(func):
    def wrapprt2():
        print('Time')
        func()
    return wrapprt2

@log
@new_f1
def f2():
    print("i am f1")
    time.sleep(2)

f2()

#多重装饰过程:由里向外装饰

#如果被装饰的函数有返回值 类似于上述的装饰过程将不会有效
def new_f2(func):           #运行时间
    def warpper1():
        s_time1 = time.time()
        func()
        e_time1 = time.time()
        print("{funcname}耗时 {time}秒" .format(funcname = func.__name__, time = (e_time1 - s_time1)))
    return warpper1

@new_f2
def f3():
    print('f3')
    return 'a'

print(f3())     #f3()返回值是None

#而根据装饰器函数的执行过程，在f3()被调用之前，编译器首先记录new_f2(func)，在执行@new_f2时会将warpper1函数返回由f3函数接收，
# 即于接下来执行f3()时，便进入warpper1()函数体，在函数体内执行被装饰器装饰的f3()只需保存原f3()函数的返回值并在最终return
# 便可达到预期效果

def new_f3(func):           
    def warpper1():
        s_time1 = time.time()
        tmp = func()
        e_time1 = time.time()
        print("{funcname}耗时 {time}秒" .format(funcname = func.__name__, time = (e_time1 - s_time1)))
        return tmp
    return warpper1

@new_f3
def f4():
    print('f4')
    return 'abc'

print(f4())

#如果被装饰器装饰的函数有一个或多个参数那么该如何解决呢？ 做法同上
def new_f4(func):           
    def warpper1(x, y):
        s_time1 = time.time()
        tmp = func(x, y)
        e_time1 = time.time()
        print("{funcname}耗时 {time}秒" .format(funcname = func.__name__, time = (e_time1 - s_time1)))
        return tmp
    return warpper1

@new_f4
def f5(x, z):
    return x

print(f5("iou yuyi gjhgj", 8))

#若不知道被装饰的函数有多少个参数，则使用动态参数
def new_f5(func):           
    def warpper1(*args, **kwards):
        s_time1 = time.time()
        tmp = func(*args, **kwards)
        e_time1 = time.time()
        print("{funcname}耗时 {time}秒" .format(funcname = func.__name__, time = (e_time1 - s_time1)))
        return tmp
    return warpper1

@new_f4
def f5(x, z):
    return x

print(f5("iou yuyi gjhgj", 8))

#这便是完整的装饰器

#更高从层次目标如果需要在new_f5()函数中增添一个打印日志的函数，并且可以根据用户输入打印 
def log(text):
    def new_f6(func):
        def warpper(*args, **kwards):
            s_time = time.time()
            tmp = func(*args, **kwards)
            print(text)                                       #打印日志函数
            e_time = time.time()
            print("{funct}耗时{time}秒".format(funct = func.__name__, time = (e_time - s_time)))
            return tmp
        return warpper
    return new_f6

@log("qwe")
def f6(x, y, z):
    return x, y

print(f6(6, 7, 9))