#4 python bytes类型
#4.1 创建bytes类型
#创建bytes时可以指定编码
a = bytes('中国', 'utf8')
b = bytes('hello', 'gbk')

#4.2输出bytes类型
print(a)    #b'\xe4\xb8\xad\xe5\x9b\xbd'
print(b)    #b'hello'   hello编码后的结果与ASCII表对应

#4.2.1输出某个字符的unicode编码值
print(ord("中"))
print(ord('h'))

#4.3bytes的解码
c = a.decode('utf8')
d = b.decode('gbk') #在解码时需要注意，编码和解码应该是一样的，否则会报错
#d = a.decode('gbk')    #报错 a的编码是utf8， 无法转换为gbk

print(c)    #解码后就是中国
print(d)    #解码后是hello
