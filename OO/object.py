#对象 = 属性 + 方法
#类名首字母大写 self相当于this指针
class bat:
    def setName(self, name):
        self.name = name
    def act(self):
        print('a')
#__init__(self)构造函数，类被实例化的时候自动调用
#公有和私有 私有使用双下划线

#类实例化最先调用的函数是__new(cls[,...])       注意:不一样的东西！！！  
class CapStr(str):                          #CapStr类继承与str
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)
str1 = CapStr("hdgs")
print(str1)

#__del__(self)析构函数

#既不需要访问实例属性也不需要访问类属性，可以考虑把这个方法封装成一个静态方法
#调用类的静态方法不需要创建类的实例对象

class stu:
    num = 5
    def __init__(self):
        pass
    
    @staticmethod           #告诉编译器这是一个静态方法
    def getNum(num):
        print("静态属性不需要访问类属性也不需要访问实例属性。" * num)          #难道静态函数不能使用类属性？是的！！！！

    @staticmethod
    def g():
        print('GG')


stu.g()
stu.getNum(5)

#继承原理 对于定义的每一个类，python会计算出一个方法解析顺序(MRO)列表-所有基类的线性顺序列表
#为了实现继承，python会在MRO列表上从左到右查找基类，直到找到第一个匹配这个属性的类位置
#这个MRO列表的构造是通过一个C3线性化算法实现的，实际上就是合并所有父类的MRO列表并遵循一下三条准则:
#1.子类会优先于父类被检查   2.多个父类会根据他们在列表中的顺序被检查    3.如果对下一个类存在两个合法的选择，选择第一个类


#子类中调用父类的方法
#方法一:
class Vehicle:
    Country = 'China'
    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power
    
    def run(self):
        print('开动啦...........')

class Subway(Vehicle):
    def __init__(self, name, speed, load, power, line):
        Vehicle.__init__(self, name, speed, load, power)
        self.line = line

    def run(self):
        print('地铁{}号线欢迎你'.format(self.line))
        Vehicle.run(self)                                   #子类中调用父类方法
    
line = Subway('中国地铁','180m/s','1000人/箱','电',13)
line.run()

#方法二: super()
class Vehicle1:
    Country = 'China'
    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print('火车开动了......')

class Subway1(Vehicle1):
    def __init__(self, name, speed, load, power, line):
        super().__init__(name, speed, load, power)
        self.line = line

    def run(self):
        print('地铁{}号欢迎您！'.format(self.line))
        super(Subway1, self).run()

line = Subway1('中国地铁','180m/s','1000人/箱','电',133)
line.run()

#当使用super()时，python会在MRO表上继续搜索下一个类。只要每个重定义的方法统一使用super()并只调用它一次,那么控制流最终会遍历完整个MRO列表,
# 每个方法也只会被调用一次使用super调用的所有属性，都是从MRO列表当前的位置往后找，千万不要通过看代码去找继承关系，
# 一定要看MRO列表

#多态与多态性   多态即：不同类调用相同方法产生不同的结果
#抽象类 抽象类只有抽象方法没有具体实现，该类不能实例化，只能被继承，子类必须实现抽象方法
#abc模块作用：Python本身并不提供抽象类和接口机制，要想实现抽象类，可以借助abc模块。abc->Abstract Base Class
#abc.ABCMeta() 用来生成抽象基础类的元类，由他生成的类可以被直接继承
#abc.abstractmethod(fun)    表明抽象方法的生成器
#abc.abstractproperty([fget[,fset[,fdel[,doc]]]])   表明一个抽象属性

import abc

class Animal(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass
    
class People(Animal):
    def talk(self):
        print('Say hello!')

class Dog(Animal):
    def talk(self):
        print('Say wangwang!')

class Pig(Animal):
    def talk(self):
        print('Say aoao!')

def func(animal):
    animal.talk()

people = People()
dog = Dog()
pig = Pig()

func(people)
func(dog)
func(pig)


#特性property 访问她时会执行一段功能(函数)然后返回值
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def permeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print(c.radius)                             #可以向访问数据属性一样去访问area，会触发一个函数的执行，动态计算出一个值
print(c.area)                               #但是此时诸如c.area不能接受赋值
print(c.permeter)

