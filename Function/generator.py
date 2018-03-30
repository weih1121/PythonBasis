#带有yield的函数被称为generator(生成器),那么什么是生成器呢？
#首先先理解Yield概念

#如何生成斐波那契数列？
#第一个版本
def fib0(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        b, a = a + b, b
        n += 1
fib0(5)
#输出为1 1 2 3 5
#结果没有问题，但是在fib函数中直接打印每次迭代的结果，
#会使得fib()函数的复用性较差，并且fib返回值为None,其他函数无法获得生成的数列

#第二个版本
def fib1(num):
    n, a, b = 0, 0, 1
    l = []
    while n < num:
        l.append(b)
        a, b = b, a + b
        n += 1
    return l

for item in fib1(5):
    print(item)
#此版本的输出也是1 1 2 3 5乍看之下也没问题，也提高了复用性
#但是有没有问题呢？如果输入一个很大的数，list所占用的内存就让人有点不想接受了
#所以如果想要不占用这么大的内存那么该如何办呢？

#第三个版本，通过迭代对象来迭代
#举个栗子
for x in range(1000):pass
#在这个操作执行过程中，通过每次迭代返回下一个数值，并不会产生长度为1000的任何数据结构
# 而是返回一个可迭代对象，内存空间占用很小，如果做到似乎可以满足我们的需求，那么开始实现

#第三个版本
class Fib:
    def __init__(self, num):
        self.num = num
        self.n, self.a, self.b = 0, 0, 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.num:
            res = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return res
        raise StopIteration()       #迭代器迭代到最后的信号

#类Fib通过next()函数不断返回数列的下一个数，使得内存占用始终为常数级
for item in Fib(5):
    print(item)

it = Fib(5).__iter__()
print("第三版本", it.__next__())
print("第三版本", it.__next__())
print("第三版本", it.__next__())
print("第三版本", it.__next__())
print("第三版本", it.__next__())
#此版本的Fib类最终也成功输出1 1 2 3 5实现了通过迭代对象产生斐波那契数列
#但是这个版本的Python代码和第一版本的相比较过于复杂，不符合Python代码的一贯作风
#所以此时若想实现相同的迭代效果，并且代码又要很简洁，yield就派上用场了

#第四版本
def fib2(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1

for item in fib2(5):
    print(item)

#最终也是成功输出1 1 2 3 5，此版本和第一版本相比唯一修改的地方就是将原本的print()
#更改为yield
#在生成器函数的执行过程中，当for循环开始被使用时，首先获得fib2(5)的迭代器，之后对循环进行迭代操作
it = fib2(5).__iter__()
print("生成器迭代", it.__next__())
print("生成器迭代", it.__next__())
print("生成器迭代", it.__next__())
print("生成器迭代", it.__next__())
print("生成器迭代", it.__next__())

it = fib2(5)            #这个和上述那个一样，都是返回生成器类型，均可用于迭代
print(type(it))

#简单地讲，yield 的作用就是把一个函数变成一个 generator，
# 带有 yield 的函数不再是一个普通函数，
# Python 解释器会将其视为一个 generator，
# 调用 fab(5) 不会执行 fab 函数，
# 而是返回一个 iterable 对象！
# 在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
# 执行到 yield b 时，fab 函数就返回一个迭代值，
# 下次迭代时，代码从 yield b 的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。

#总结:一个带有 yield 的函数就是一个 generator，
# 它和普通函数不同，生成一个 generator 看起来像函数调用，
# 但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
# 并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
# 每次中断都会通过 yield 返回当前的迭代值。

#yield 的好处是显而易见的，
# 把一个函数改写为一个 generator 就获得了迭代能力，
# 比起用类的实例保存状态来计算下一个 next() 的值，
# 不仅代码简洁，而且执行流程异常清晰。

#如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
from inspect import isgeneratorfunction
print(isgeneratorfunction(fib2))

#此处需要注意fib2和fib2(5)的区别， fib2是一个生成器函数，而fib2(5)是调用fib2中的函数
#返回的一个generator实例,就好比类的定义和类的实例之间的区别
print(type(fib2))                   #fib2是一个函数类型
print(isgeneratorfunction(fib2(5))) #fib2(5)是一个生成器类型

#return作用 在一个generator function中，如果没有return，则默认执行至函数完毕
#如果在执行过程中return，则直接抛出StopIteration终止迭代

#另一个yield的例子来源于文件读写，如果直接对文件执行read()操作,会导致不可预测的内存占用
#比较好的方法是利用固定长度的缓冲区来不断读取文件内容。
#通过yield使得我们不必编写读文件的迭代类，就可以轻松实现文件读取

#yield读文件的例子
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        block = f.read(BLOCK_SIZE)
        if block:
            yield block
        else:
            return

path = 'SmallTasks.txt'
for item in read_file(path):
    pass



