#helloworld
print('hello world')

#1.变量 - varaible 
name = "Roku"
age = 30
is_learning = True

print(name)
print(age)
print(is_learning)
#1.1 可以随意给同名变量赋不同类型的值
x = 10
print(type(x))
x = "XXXX"
print(type(x))
#1.2 类型提示.这是提示,编译器不会处理它
name: str = "Roku"
age: int = 25
is_learning: bool = True
#1.3 数字
#python只有三个类型的数字,int(整数,长度不限),float(浮点数,长度不限),complex(实数)
x = 37216654545182186317
y = 57E04
z = 3.3333333333
a = 2.7+2j #j是虚数单位
print(type(x),type(y),type(z),type(a))
#1.3 布尔
#非零数字,非空字符串,非列表转换为bool时全是True,0/空字符串/空列表都是False
print(bool(39),bool("123"),bool({"apple","banana"}),"\n",bool(0),bool(""),bool([]))

