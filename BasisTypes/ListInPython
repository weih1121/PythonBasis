#6 列表是python以及其他语言中最常用到的数据结构之一。Python中使用[]来创建列表
#列表中的每项是可以改变的，这一点区别于元组
#6.1 列表的创建，遍历及增删改查
#创建
names = ["mike", 'jud', 'huihui', 'wang', 'tian', 'kaggle']
#遍历
for name in names:
    print(name)
#查 切片查
print(names[2])         #打印第三个名字
print(names[0 : 3])     #切片处理， 打印前三个
print(names[0 : 10])    #当切片长度大于列表长度，就按照列表长度切片
print(names[-1])        #输出列表最后一个，当数字为负数时，输出倒数第n个
print(names[2 : 3])     #左闭右开
print(names[0 : 5 : 1]) #切片操作[start : end : size]切取[start-end)区间的子序列，start默认值为0 size != 0
print(names[5 : 0 : -3])#和上一个一样
print(names[::-1])      #相当于反转
print(names[:])         #相当于0-最大长度

#增(append, insert)
names.append('alex')
names.insert(5, 'alvin')
print(names)

#改(重新赋值)
names = ['章叁', '李四', '王五', '赵六']

names[2] = "孙三"
names[0 : 2] = ["liu", 'wang']
print(names)

names = ['章叁', '李四', '王五', '赵六']
#删(remove, del, pop(返回值))
names.remove("章叁")
print(names)
del names[0]
print(names)
del names           #names变量在内存中被析构

names = ['章叁', '李四', '王五', '赵六']
names.pop()
print(names)

#其他操作 count
lists = ['to', 'be', 'or', 'not', 'to', 'be']
print(lists.count('to'))                        #查询某个元素在列表中出现的次数

#6.2 extend 该方法可以在列表的末尾一次性追加另一个序列中的多个值
lista = [1, 2, 3]
listb = [4, 5, 6]
lista.extend(listb)
print(lista)

#index 该方法用于返回元素在列表中的位置
print(lista.index(3))

#reverse
lista.reverse()
print(lista)

listc = [5, 2, 4, 12, 9, 0]
listc.sort()
print(listc)

#深浅拷贝
names = ['章叁', '李四', '王五', '赵六']
names_copy = ['章叁', '李四', '王五', '赵六']
print(id(names))        #2438619076232
print(id(names_copy))   #2438618956936

for name, name_copy in zip(names, names_copy):
    print(id(name), id(name_copy))

#输出：
#2438618789208 2438618789208
#2438618789296 2438618789296
#2438618789384 2438618789384
#2438618789472 2438618789472
#由此可以看出names_copy的元素的地址和names的元素地址相同，是浅拷贝

print("------------------------")
names_copy[0] = "图像"
for name, name_copy in zip(names, names_copy):
    print(id(name), id(name_copy))
#在执行names_copy[0] = "图像"就会把原本指向'章叁'的地址的指针，指向'图像'所在的地址

b, d, e, *c = ['1', '2', 3, 4, 5]      #将列表中的元素赋值给等号左边变量，当左边的变量不能完全接受列表元素，会存在c列表中
print(type(b), type(d), type(c))
print(b, d, e, c)
