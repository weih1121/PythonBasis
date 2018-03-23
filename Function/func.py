#python解释器的本质-python.exe
#python代码运行的本质-使用python.exe打开python脚本
#程序的构成-值，表达式，语句
#函数，用于进行某种计算的一系列语句的有名称的组合
#函数定义:
    #关键字：def
    #规则:字母,数字,下划线 注意:变量名/脚本名不能和关键字重复
    #定义一个函数会创建一个'function'类型的函数对象
    #调用自定义函数和调用内置函数的方式一样
    #定义一个函数可以在其他函数中调用
#函数执行过程:在脚本执行过程中，遇到def关键字，会在内存中开辟一块空间，
# 将函数体加载进去(函数体并不会立即执行)，并且用函数名指向函数体所在内存
#在函数被调用的时候，首先通过函数名找到函数体所在内存的地址，执行内存中保存的函数体

#不带形参的自定义函数
def PrinText():
    print(1)

def PrintTwice():
    PrinText()
    PrinText()

PrintTwice()

#带形参的自定义函数
def PrintText1(text):        #text是形参
    print(text)

def PrintTwice1(text):
    PrintText1(text)
    PrintText1(text)

PrintTwice1('abc')            #abc是实参
name = 'defg'
PrintTwice1(name)             #name也是实参
    

#打印田
def DoTwice(f):
    f()
    f()

def PrintLine():
    print('+ - - - -', end = '')

def PrintOneLine():
    DoTwice(PrintLine)
    print('+') 

def PrintRow():
    print('|        ', end = '')

def PrintOneRow():
    DoTwice(PrintRow)
    print('|')

def PrintHalfTian():
    PrintOneLine()
    DoTwice(PrintOneRow)
    DoTwice(PrintOneRow)
    
def PrintTable():
    DoTwice(PrintHalfTian)
    PrintOneLine()

PrintTable()

#为什么要有函数？
    #代码易读
    #减少重复代码
    # ...

