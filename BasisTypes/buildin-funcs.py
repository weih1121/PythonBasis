#3 python 常用的内置函数类型
from math import *
from operator import *

x = 3.14    #定义两个number x, y
y = 4.25
print(abs(-x))  #abs返回数字的绝对值abs返回数字的绝对值
print(fabs(x))
print(ceil(x))  #返回输入数字的上入整数
print(floor(x)) #返回输入数字的下舍整数

print(le(x, y)) #l -> less, e-> equal, g -> greater 比较函数
print(lt(x, y))
print(eq(x, y))
print(gt(x, y))
print(ge(x, y))

a = 2
print(exp(a))   #返回e的a次幂

print(log(100, 10)) #返回以10为底100的对数  返回对数
print(log(e, e))    #返回以e为底e的对数

listNum = [1, 2, 3, 5, 8, 19, 2, 8]
print(max(listNum)) #返回最大值
print(min(listNum)) #返回最小值

num = 15.23
num1, num2 = modf(num)  #返回num的小数部分与整数部分
print(num1, num2)

powx, powy = 2, 5
print(pow(powx, powy))  #返回powx的powy次幂 即：powx ** powy

roundx = 3.1546
n = 3
print(round(roundx, n))      #返回浮点数四舍五入的结果，保留到小数点后n位

print(round(2.635, 2))  #2.63
print(round(2.645, 2))  #2.65
print(round(2.655, 2))  #2.65
print(round(2.665, 2))  #2.67
print(round(2.675, 2))  #2.67   由此可见round函数存在缺陷

'''
The behavior of round() for floats can be surprising: for example,
 round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug:
  it’s a resultof the fact that most decimal fractions 
  can’t be represented exactly as a float. See Floating Point Arithmetic: 
  Issues and Limitations for more information.
'''

sqrtx = 16
print(sqrt(sqrtx))  #返回sqrtx的平方根
