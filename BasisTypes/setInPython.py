#9 集合set 集合是一个无序，不重复的数据组合，主要功能:去重， 关系测试

l1 = [1, 2, 'a', 'b']   
set1 = set(l1)              #参数是一个可迭代类型
print(set1)

l2 = [1, 2, 1, 'a', 'a']
set2 = set(l2)              #自动去重
print(set2)

#集合对象是一组无序排列的可哈哈希的值，集合成员可以做字典的键
#l2 = [[1, 2], 'a', 'b']
#set3 = set(l2)              #TypeError: unhashable type: 'list'

#集合:可变集合和不可变集合
#可变集合set:可添加，删除元素，不可哈希， 不能作字典的键，不能作其他集合元素
#不可变集合frozenset:与上述相反
#l3 = [1, 'a', 'b']
#s = set(l3)
#dict = {s : '123'}  TypeError: unhashable type: 'set'

#创建集合，由于集合本身是无序的，所以不能为集合创建索引或切片操作，只能通过循环遍历或者in, not in来访问或判断几何元素
set3 = set("alain")
set4 = frozenset("yuan")

print(set3, type(set3))
print(set4, type(set4))
print('a' in set3)
print('b' not in set4)

#更新集合 add, update, remove
set5 = set('hello')
set5.add('1')
print(set5)

set5.update("UIO")
print(set5)

set5.remove("o")
print(set5)

del set5        #删除集合本身

#集合类型操作符
#in, not in
set5 = set('aliyun')
set6 = set('abcs')

print('a' in set5)
print('d' not in set6)
print(set5 < set6)

#联合 联合操作与集合操作or操作等价 还与union()操作等价
set7 = set("1589poi")
set8 = set("542kj")
set9 = set7 | set8
print(set9)
print(set7.union(set8))

#交集 与集合操作and等价，还与intersection()操作等价
set10 = set7 & set8
print(set10)
print(set7.intersection(set8))

#差集 - 与之相对应的操作是difference()
set11 = set7 - set8
print(set11)
print(set7.difference(set8))

#对称差集 元素不同时存在于两个集合之中 ^ 或者symmetric_difference()
set12 = set7 ^ set8
print(set12)
print(set7.symmetric_difference(set8))

