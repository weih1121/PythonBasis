#lambda表达式基本语法 lambda关键字，关键字后跟变量名，变量名后跟:, 之后是函数的返回追
lambda x : x + 5        #lambda即匿名函数
print(lambda x : x + 5) #返回函数的地址
func = lambda x : x + 5
print(func(5))

#两个参数的例子
def add(x, y):
    return x + y

lambda x, y : x + y
fun_add = lambda x, y : x + y

print('平凡的函数调用结果是: %d' %add(10, 15))
print('lambda表达式结果: %d' %fun_add(10, 15))  #两个函数效果一致

#作用:
# 1.Python写执行脚本时，使用lambda可以省下函数的定义过程,代码更简洁
# 2.对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，可以省略
# 起名这种比较令人头疼的问题
# 简化代码可读性 不需要去函数体内查看原函数

#过滤器filter(),通过过滤器可以筛选我们关注的信息。
#参数第一个可以是函数/None，第二个是可迭代的数据结构 
#第一个参数若是函数，则将第二个参数的每个元素作为函数参数，返回为True筛选
#为None,筛选为True的元素

#None的例子
res = filter(None, [1, 0, 5, False, True])  #返回一个filter对象
print(list(res))

#筛选出奇数的过滤器
num = []
for i in range(15):
    num.append(i)
print(list(filter(lambda x : x % 2, num)))

#map()映射第一个参数是一个函数，第二个参数是一个可迭代的对象
#将对象的每个元素作为函数的参数，运算加工，直到可迭代对象的每个
#元素都加工结束，返回新序列

print(list(map(lambda x : x + 5, num)))

