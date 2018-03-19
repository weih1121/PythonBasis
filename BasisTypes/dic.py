#8.1 字典时python中唯一的映射类型，采用键值对(key-value)的形式存储数据。
#python对key进行哈希函数运算，根据计算结果决定value的存储地址，字典时无需存储的，key
#必须是可哈希的。可哈希表示key必须是不可变类型的，如:数字，字符串，元组
#字典时除列表以外python中最灵活的内置数据结构类型，列表是有序的对象结合，字典时无序的对象的集合。
#区别在于:字典当中的元素是通过键来存取的，而列表是通过便宜存取的

#8.2创建字典:
dict0 = {}          #创建空字典
dict3 = dict()      #创建空字典
dict1 = {'name':"alex", 'age':36, 'sex':'male'}                 #通过键值对直接构造字典
dict2 = dict((('name','alex'), ('age',15), ('sex', 'male')))    #通过键值对和dict()构造函数构造字典

names = ['a', 'b', 'c', 'd']
ages = [10, 15, 18, 0]
dict4 = {name : age for name, age in zip(names, ages)}          #通过迭代器生成字典


# for name, age in zip(names, ages):
#     dict[name] = age

#增
dict5 = {}
dict5['name'] = 'alex'
dict5['age']  = 18
print(dict5)

a = dict5.setdefault('name', 'hei')
b = dict5.setdefault('age', 88)
print(a, b)
print(dict5)