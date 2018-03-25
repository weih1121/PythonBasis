#迭代器 每次迭代的结果，作为下一次迭代的初始值
#通常的迭代器有，列表，元组，字符串，字典

for i in 'stre':    #此处字符串是一个容器也是一个迭代器
    print(i)        #for语句触发迭代器的迭代功能

    #使用迭代器遍历字典
dicts = {'a' : 15, 'b' : 12, 'c' : 13, 'd' : 14}
for item in dicts:
    print(dicts[item])

#两个BIF,一个是iter()，一个是next()

string = 'abcdefghijklmn'
it = iter(string)
for i in range(len(string)):  
    print(next(it), end = '')

print()
print('----以下是生成器内容----')
#生成器 如果一个函数中包含yield关键字，则这个函数便是生成器函数
#函数执行过程

#先写一个简单的生成器函数
def f():
    print('in f()', 112)
    yield 1
    print('in f()', 'asd')
    yield 2
    print('in f()', '1vxcv12')
    yield 3
    print('in f()', 'erytrg45')
    yield 4
g = f()
g.__next__()
g.__next__()
g.__next__()
g.__next__()
#g.__next__()   #超出迭代范围报错
#yeild函数在执行过程中，当执行到yield语句时，将会跳出函数，并且保存函数当前状态
#下次函数调用时，会继续从上次跳出的位置继续向下执行

print(g.__iter__() is g)        #通过__iter__()返回自身，再通过__next__()迭代
g1 = f()

for item in g1:
    print(item)

#yeild例子
class MyNumber:
    def __init__(self, start, end):
        self.start = start
        self.end   = end

    def isMuNumber(self, num):
        if num < 2:
            return False
        for k in range(2, num):
            if num % k == 0:
                return False
        return True

    def __iter__(self):
        for number in range(self.start, self.end + 1):
            if self.isMuNumber(number):
                yield number

for x in MyNumber(1, 20):
    print(x)

#推导式:
#列表推导式 [表达式 for 循环]
MyList = [x ** x for x in range(1, 5)]
print(MyList) 

#判断奇偶第一种方法
list1 = [x for x in range(15)]
MyList = [x for x in(list(filter(lambda x : x % 2 != 0, list1)))]
print(MyList) 

#判断奇偶第二种方法。，与1按位与 为1是奇数
MyList1 = [x for x in list1 if x & 1 == 0]
print(MyList1)

tup = (x for x in list1 if x & 1 == 0) #这是一个生成器对象，而不是元组
print(tup)

print(dir(tup))
print(tup.__next__())

#生成器的一种创建方式:
 #(表达式 for if) -> generator(生成器对象)
 #generator.__next__()
    #获取生成器中的数据,将数据返回，并且不能保存数据
    #生成器中的数据只有在使用的时候才会创建 
    #节约内存
#字典推导式:
    #{ }
MyList2 = [x for x in range(16)]
dict1 = {key : {1, 'q'} for key in MyList2}
print(dict1)

#关键字a-z， 值[1, 2, 3, 4, 5]

character = [chr(x) for x in range(97, 123)]
print(character)
dict2 = {key : index + 1 for index, key in enumerate(character)}
print(dict2)