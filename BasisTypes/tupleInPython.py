#7.1 tuple 元组被称为只读列表，元素在元组中只可以被查询不能被修改，列表的切片操作同样适用于元组
#元组写在小括号里，元素之间用逗号隔开
#元组的元素虽然不可以改变，但是可以包含可变的对象，比如list
#构造包含0/1个元素的元组比较特殊，需要额外的语法规则

tup1 = ()   #空元组
tup2 = (20, )   #一个元素，需要在元素后边添加逗号
list1 = [1, 2, 3, 4]  
tup3 = (list1)  #参数为任意一个可迭代的类型
print(tup1)
print(tup2)
print(tup3)

tup3 = (5)          #若创建只有一个元素的元组时，不在唯一的元素后边加，则创建的对象不是tuple类型
print(type(tup3))

#7.2 元组的意义还在于，元组可以在映射（和集合的成员）中当作键使用——而列表则不行；元组作为很多内建函数和方法的返回值存在

#7.3 返回元组中指定元素的数量
tup4 = ('a', 'b', 'e', 'd', 'c')
print(tup4.count('e'))

#7.4 返回元组中指定元素的索引
print(tup4.index('e'))

#7.5 元组切片
print(tup4[:])              #切片有三个参数，起点，终点(不被包含)， 步长
print(tup4[0 : 2])
print(tup4[1 : 4 : 2])
print(tup4[4 : 1 : -1])

#7.6 向元组中添加元素
tup4 = tup4 + ('o', )     #不能直接添加字符串，只可以添加tuple
tup4 = tup4 + (3, 5)      #两个元组可以通过+添加到一起
#tup4 = tup4, (6, 7)       #返回一个元组，其中有2个元素
print(type(tup4))
print(tup4)

#7.7 删除元组 会在内存中将元组析构
#del tup4
#print(tup4)     #NameError: name 'tup4' is not defined
#若想删除元组单独的一个元素是不可能的，但是可以通过切片操作
#重组元组
tup5 = tup4[0 : 3]
print(tup5)

#7.8成元关系运算符in, not in
print('a' in tup4)
print('e' not in tup4)

#连接，重复操作符+， *
tup6 = tup5 + tup5
print(tup6)

tup7 = tup5 + ('x', 'y', 'z')
print(tup7)

tup8 = tup5 * 2
print(tup8)

#7.9 逻辑操作符 <, ==, >只比较第一个元素
tup9 = (6, 12)
tup10 = (11, 0)
print(tup9 > tup10)
print(tup9 == tup10)
print(tup9 < tup10)

#比较中间的元素，将返回的布尔值插入后建立的元组

tup11 = 6, 12 > 11, 0
print(tup11)

tup12 = 6, 12 == 11, 0
print(tup12)

tup13 = 6, 12 > 11, 0
print(tup13)

