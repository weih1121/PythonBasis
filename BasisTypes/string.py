#2. 字符串类型(string)
#2.1 创建字符串
'''
字符串以单引号或双引号括起来的任意文本
'''

str1 = 'hello python!'      #len = 13
str2 = "python is great!"   #len = 16
print(type(str1), id(str2))
print(str1)
print(str2)
print(len(str1), len(str2))

#2.2字符串操作
#2.2.1 *重复输出字符串
print(str1 * 2)

#2.2.2 [], [:]通过索引获取字符串中的字符， 这里和列表的切片操作是相同的，具体内容看列表操作
print("helloworld" [2:])     #n > 0 取第n个字符后边的字符串
print("helloworld" [-5:])    #n < 0取字符串前n个字符
print("helloworld" [0:])     #n == 0 不切片

#2.2.3 in成员运算符 如果字符串中包含给定的字符返回True
print("l" in "hello")

#2.2.4 格式化字符串
print('hello world')
print('hello %s' %'world')     #使用%
print('hello {}'.format("world"))   #使用format
print('{first} {second}.'.format(first = "hello", second = "world"))#并使用关键字
print("Hi, {0}, {0} is a great {1}".format("Python", "language"))   #使用位置参数

li = ['hello', 'python']    #li -> list
print("{0[0]}, this is {0[1]}".format(li))  #使用下标参数

#2.3内置函数
'''
['__add__', '__class__', '__contains__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', 
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 
'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

# # 小写 
# S.lower() 
# # 大写 
# S.upper() 
# #大小写互换 
# S.swapcase() 
# # 首字母大写 
# S.capitalize() 

# # 输出width个字符，S左对齐，不足部分用fillchar填充，默认的为空格。 
# S.ljust(width,[fillchar]) 
# # 右对齐 
# S.rjust(width,[fillchar]) 
# # 中间对齐 
# S.center(width, [fillchar]) 

# # 返回S中出现substr的第一个字母的标号，如果S中没有substr则返回-1。start和end作用就相当于在S[start:end]中搜索 
# S.find(substr, [start, [end]]) 
# # 返回S中最后出现的substr的第一个字母的标号，如果S中没有substr则返回-1，也就是说从右边算起的第一次出现的substr的首字母标号 
# S.rfind(substr, [start, [end]]) 
# # 计算substr在S中出现的次数 
# S.count(substr, [start, [end]]) 
# #把S中的oldstar替换为newstr，count为替换次数
# S.replace(oldstr, newstr, [count]) 

# # 把S中前后chars中有的字符全部去掉，可以理解为把S前后chars替换为None 
# S.strip([chars]) 
# S.lstrip([chars]) 
# S.rstrip([chars]) 

# # 以sep为分隔符，把S分成一个list。maxsplit表示分割的次数。默认的分割符为空白字符 
# S.split([sep, [maxsplit]]) 
# # 把seq代表的字符串序列，用S连接起来 
# S.join(seq)