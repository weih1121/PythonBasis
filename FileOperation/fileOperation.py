#11 文件操作
#文件操作基本流程
#1.打开文件，得到文件句柄并赋值给变量           f = open('')
#2.通过获得的句柄对文件进行操作                data = f.read()读文件
#3关闭文件                                   f.close()

#windows的文本文档默认的编码是ansi编码，直接打开会乱码
#文件打开模式
#'r' 默认的打开方式，只读
#'w' 打开写入，首先截断文件(若文件不空，首先清空文件)
#'x' 创建一个新文件，只写
#'a' 只写打开文件，如果文件不空追加到文件末尾
#'b' 二进制模式 
#'t' 文本模式 也是默认的模式
#'+' 打开磁盘文件准备更新（读和写）
#'U' 通用换行模式(不建议使用)

#read()方法不一定能全读出来， 只做一次系统调用
#注意:python只能将字符串写入文件

#总结先写前头，如果想要字符数据并且观看内容使用r模式，如果不需要观看只需rb便可。
#在python3中对于seek()函数，所操作的文件必须是rb

f = open('test', encoding='utf8')
data = f.read()                    #将文件内容直接加载到内存中
print(data)

#只读n个字符
f.seek(0)                           #文件指针指到行首
data = f.read(10)                   #读10个字节
print(data)

#只读前五行
f.seek(0)
for i in range(5):
    print(f.readline())

#以列表的方式读取整个文件，文件大内存容易出问题，慎用！！！！！！！！！！注意注意！！
f.seek(0)
print("以列表的方式读取整个文件")
for line in f.readlines():
    print(line)
f.close()

#读取一行
with open('test', encoding='utf8') as f:
    print(f.readline())

#写入文件，参数为字符串 
with open('test', 'a+', encoding='utf8') as f:
    f.write('嗯！ 你说的很对！！我同意')

#写入文件，参数是序列,比如列表，元组等。
with open('test', 'a+', encoding='utf8') as f:
    f.writelines(['小子', '你', '真聪明！'])

#判断文件是否是这个Return whether this is an 'interactive' stream
with open('test', 'r+', encoding='utf8') as f:
    ret = f.isatty()
    read = f.readable()
    print('判断是否可读:', read)
    print(ret)
    
#指定/指出文件中指针的位置
with open('test','r', encoding='utf8') as f:
    f.read(15)
    print(f.tell()) #指出文件指针的位置
    f.seek(20)
    print(f.tell())   #指定文件指针


#截断文件数据，仅保留指定之前的数据(字节数)
with open('test', 'r+', encoding='utf8') as f:
    f.truncate(0)

