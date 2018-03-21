#Closure 闭包:在一个内部函数中，对外部作用域的变量进行引用
# (并且一般外部函数的返回值为内部函数)，那么内部函数就被认
# 为是闭包
#闭包作用:闭包可以保存当前的运行环境

#e.g.
def Increase(x):
    def IncreaseByB(b):
        return x + b
    return IncreaseByB

res = Increase(5)
print(res(6))   #11

#闭包修改函数外的变量 

z = 0
def OuterFunc():
    x = 0
    z = 1
    print(z)                            #很遗憾未发生改变
    def InnerFunc():
        x = 1
        print(id(x))
    print('x in OuterFunc() is :', x)
    InnerFunc()
    print('x in OuterFunc() is :',  x)  #执行完闭包后，x的值仍未改变 -> 那么对于全局作用域的值在函数内部能不能改变呢？
OuterFunc()


#总结:函数外部的变量对函数内部可见，但是若在函数内部直接声明一个同名变量，在函数内部的变量会屏蔽外部变量
#若想在函数内部访问外部变量需要使用globle/nonlocal定义变量

#python循环中不包含域的概念
flist = []
for i in range(3):          #循环在python中没有域的概念，flist在向列表中添加func的时候，并没有保存i的值
    def func(x):            #当执行f(2)的时候才去取，这时候循环已经结束，i的值是2
        return x * i
    flist.append(func)

for f in flist: #输出4， 4， 4 而不是0， 2， 4
    print(f(2))

#修改方案
flist = []
for i in range(3):
    def makefunc(i):
        def func(x):         #func形成闭包
            return x * i
        return func
    flist.append(makefunc(i))

for f in flist:
    print(f(2))