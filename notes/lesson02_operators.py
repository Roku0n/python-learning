# 2.1 算数运算符
a = 10
b = 3
# / 是浮点除法,//是整数除法, **是幂运算
print(a + b, a - b, a * b, a / b, a // b, a % b, a**b)

# 2.2 比较运算符
# == 符号不会进行隐式类型转换(和JS不同)
print(a == b, a != b, a > b, a < b)

# 2.3逻辑运算符
# 和 是and关键字,或 是or,非 是not(不是&& || !那套)
print(True and False, True or False, not True)

# 2.4 字符串基本操作
first = "Hello"
last = "World"
# 拼接,用+
greeting = first + " " + last
print(greeting)
#*f-string格式化
greeting2 = f"{first} {last}"
print(greeting2)
# 长度
print(len(greeting))
# 大小写
print(first.upper())
print(first.lower())
