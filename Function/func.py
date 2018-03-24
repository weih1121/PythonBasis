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

#函数参数:
# 必备参数:(函数定义时)
# 函数的参数在定义时只有参数名，没有值，这种定义的方式使得函数调用时一定得
# 传入参数才能够正常的调用函数。必备参数的个数和顺序必须是和定义时是一致的，
# 除非调用时使用了关键字参数就可以改变参数顺序传入,那么如何改变参数传入位置呢？
# 答案就在本文内部，请自行查找。
def MyAdd0(x, y = 10):
    return x + y

print(MyAdd0(1, 2))

#默认参数:(函数定义)
# 函数的参数在定义时给出了初始值，这时参数在调用时如果不传入值给这个参数，函数就会使用
# 定义时的默认值，如果传了值进来给这个参数，那么默认值就会被丢弃而使用传进来的这个值。
# 定义带有默认参数的函数，默认参数只能放在后边
def MyAdd1(x, y = 10):
    return x + y

print(MyAdd1(5))     #只传入一个参数x = 5, y等于默认参数15
print(MyAdd1(5, 5))  #x = 5, y = 5

#关键字参数:(函数调用)
# 是指在函数调用的时候，传参时把定义函数时参数名和对应的值一起传入函数中，
# 这时传入的参数的顺序就不用考虑了。上述的传参顺序问题解决。
print(MyAdd0(y = 15, x = 12))
print(MyAdd1(y=9, x=3))

#1 不定长参数:(定义和调用)
def MyAdd2(x, y, *args):
    print(type(args), end=" ")
    print(args)
    return x + y

#调用不定长参数,args的类型是元组的类型
MyAdd2(6, 6)
MyAdd2(6, 6, 7, 7, 7, 8)

#2 不定长参数
def MyAdd3(x, y, *args, **kwards):
    print(type(args), end=" ")
    print(args)
    print(type(kwards), end=" ")
    print(kwards)
    return x + y

MyAdd3(6, 7, 8, 8, 8, name="1", age="1", sex="1")
#MyAdd3函数中6， 7分别传递给x, y，(8, 8, 8)以元组的形式传递给args,
#其余参数以字典的方式传递给dict

def MyAdd4(x, y, z):
    return x * y + z

numList = [3, 2, 1]
print(MyAdd4(*numList))

tp  = 1, 0, 3, 2
print(type(tp))