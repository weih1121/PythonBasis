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

names = tuple(['a', 'b', 'c', 'd'])
ages = [10, 15, 18, 0]
dict4 = {name : age for name, age in zip(names, ages)}          #通过迭代器生成字典

dict6 = {}
for name, age in zip(names, ages):                              #生成字典，使用setdefault()函数向字典中添加新的item
        dict6.setdefault(name, age)

print(type(dict6))
print(dict6)
#增
dict5 = {}
dict5['name'] = 'alex'
dict5['age']  = 18
print(dict5)

a = dict5.setdefault('name')         #获取指定key的value,如果key不错在，则创建并且返回值为None
b = dict5.setdefault('age')
print(a, b)
print(dict5)

#查
dict1 = {'name':"alex", 'age':36, 'sex':'male'}
print(dict1.items())                #输出字典中的键值对
print(dict1.keys())                 #输出字典中的关键字 类型是<class 'dict_keys'>
print(type(dict1.values()))         #输出字典中的值 类型是<class 'dict_values'>

print(dict1['name'])                #按关键字输出字典中的value 如果关键不在字典中则会报关键字错误
print('name' in dict1)              #判断某个关键字是否在字典中
print(dict1.get('names'))           #get函数返回字典中关键字所对应的值，如果键不在字典中返回None

dict7 = {}
dict7.update(dict1)
print(dict7)

#改
print('-------------------------')
print(dict1)
dict1['name'] = "jquery"
print(dict1)

#删
#dict1.clear()
#print(dict1)                        #清空字典

del dict1['name']
print(dict1)
item = dict1.popitem()
print(item)
print(dict1)
print(dict1.pop('age'))
print(dict1)
del dict1                              #删除字典，在内存中将字典所占用的内存析构


#其他操作涉及到的方法
dict8 = dict.fromkeys(['host1', 'host2', 'host3', 'host4'], 'Mac')  #返回一个新字典，并将每个关键字的值设为默认的value
print(dict8)

dict8['host1'] = 'xiaomi'
print(dict8)

dict9 = dict.fromkeys(['host1', 'host2', 'host3', 'host4'], ['xiaomi', 'mac', 'apple'])
print(dict9)
dict9['host2'][0] = 'huawei'
print(dict9)

#字典嵌套
cla = {
    '本校':{
        '一年级':5,
        '二年级':10,
        '三年级':10,
        '四年级':10     
    },
    '外校':{
        '一年级':50,
        '二年级':100,
        '三年级':100,
        '四年级':100 
    }
}
print(cla)
print('===========================')
#字典排序
dict10 = {'z':5, 'c':8, 'b':6, 'n':56}
print(sorted(dict10))                   #返回一个有序的包含字典所有key的列表

dict11 = {'name':"alex", 'age':36, 'sex':'male'}

#字典的遍历
for i in dict11:                        #i将会得到字典的关键字
    print(i, dict11[i])

for item in dict11.items():
    print(item)

for key, value in dict11.items():
    print(key, value)
