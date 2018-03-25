#文件操作
#文件读写过程操作类似于手动操作windows下文件过程
#首先打开文件，之后对文件进行读写，最后关闭文件。
#open()函数参数，文件名，操作模式，编码方式
#文件名 = 全路径(绝对路径或者相对路径 默认为当前路径)
#打开模式:
    # w 只写模式打开，清空(不是覆盖) + 写 注:数据库操作慎用
    # r 只读    文件不存在则报错
    # a 在文件末尾追加  注:文件不存在则创建一个新文件
    # wb 二进制写
    # rb 二进制读
    # ab 二进制追加
    # w+ 读写模式
    # r+
    # a+
    # wb+
    # rb+
    # ab+
#以下三个函数测试w,r,a作用
# f = open('test', 'w', encoding='utf8')           #文件打开以后，
#                                 #会在内存生成一段数字(文件句柄或者文件对象)
# f.write('Hello world!')
# f.close()

# fread = open('test', 'r', buffering=-1, encoding='utf-8')
# content = fread.read()
# print('读文件' + ' ' + content)
# fread.close()

# fappend = open('test_append', 'a', encoding='utf-8')
# fappend.write("嘻嘻嘻")
# fappend.close()

#copy一个文件到当前路径
#1.先打开目标图片
#2.读图片内容(binary)
#3.在当前文件建立一个文件
#4.将图片内容写入文件
#5.关闭文件

#写二进制文件
# fresource = open(r'C:\Users\H\Desktop\pythonbasis\FileOperation\ez.jpg', 'rb')
# fdestanation = open('ezcopy1.jpg', 'wb')
# bbate = fresource.read()
# print(bbate)                    #将会打印二进制数
# fdestanation.write(bbate)
# fresource.close()
# fdestanation.close()

#视频，图片，文件很多以二进制方式保存的
#抛出一个问题，读写文件是二进制模式更快，还是非二进制模式更快呢？

#执行写操作时，首先将内容放入缓冲区，之后再进行写操作。
#read()函数一次性将文件读取，加载到内存中，在处理大文件时不适用

#读取一行
# fline = open('lines', 'r')
# line = fline.readline()
# print(line)
# fline.close()

#通过一行一行读取整个文件
# fline = open('lines', 'r')
# for line in fline:
#     print(line)
# fline.close()

#一行一行写
l = ['1', '2', '3']
fwriteline = open('write', 'w')
for item in l:
    fwriteline.write(item + '\n')
fwriteline.close()

#readlines()函数,将文件内容按行的模式以列表的形式返回
# flines = open("lines", 'r')
# print(flines.readlines())
# flines.close()

#只想读取中间某几行tell()   返回当前文件操作指针所在位置
# with open('lines', 'r') as f:
#     f.readline()
#     f.seek(0)              #将文件操作指针移动到指定位置
#     print(f.tell())

#如果想要在某个位置插入一段内容，首先需要将文件读取并用一个数据结构
#存下来，之后操作该数据再执行写入
#文件操作仍有许多内容，大家可以根据以上的基础进行跟深入的研究。
