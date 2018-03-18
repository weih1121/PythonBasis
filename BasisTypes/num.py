#1.1 数字类型的创建
a = 10              #定义变量a，并且赋初值为10
b = a

print(a)
print(b)
print(type(a))
print(type(b))
print(id(a), id(b)) #a and b id is the same执行b = a,将a的地址赋给b，所以a和b指向相同的内存区

#1.2number cast
var1 = 3.14
var2 = 5
var3 = int(var1)
var4 = float(var2)

print(var3, var4)

#1.3division
print(var2 / var1)  #除法
print(var2 // var1) #整除
print(var2 % var3)  #q取余