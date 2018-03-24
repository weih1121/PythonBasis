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

