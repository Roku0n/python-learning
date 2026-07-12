from datetime import datetime, time

# 3.1 条件语句
# 3.1.1 基本结构
age = 20
# if语句的后面必须有冒号,条件执行的语句必须缩进(四个空格),和java和js的大括号语句不一样
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# 3.1.2 elif
score = 75
# 声明变量必须赋值哦,None是个占位值
grade = None
if score >= 93:
    grade = "A"
elif score >= 90:
    grade = "A-"
elif score >= 87:
    grade = "B+"
elif score >= 83:
    grade = "B"
elif score >= 80:
    grade = "B-"
elif score >= 77:
    grade = "C+"
elif score >= 73:
    grade = "C"
elif score >= 70:
    grade = "C-"
elif score >= 67:
    grade = "D+"
elif score >= 63:
    grade = "D"
elif score >= 60:
    grade = "D-"
else:
    grade = "F"
print(f"Your score is {score}, your grade is {grade}.")

## 3.1.3条件表达式
age2 = 17
result = "adult" if age2 >= 18 else "minor"
print(result)
## 3.1.4复合判断
# exp1 入场
is_member: bool = False
customer_booked: bool = True
master_is_idle: bool = False
if is_member and customer_booked and master_is_idle:
    print("Welcome, Please sit down.")
else:
    print("Sorry, you cannot enter.")
# exp2 当前时间判断 如:壁纸软件需要判断当前时间渲染不同壁纸样式
# 5:30 - 8 早晨,8-12上午 12-17下午 17-19 傍晚 19-5:30 夜晚
current_time = datetime.now().time()
print(f"Now time is {current_time}")
if time(5, 30) <= current_time < time(8, 0):
    period = "Dawn"
elif time(8, 0) <= current_time < time(12, 0):
    period = "Forenoon"
elif time(12, 0) <= current_time < time(17, 0):
    period = "Afternoon"
elif time(17, 0) <= current_time < time(19, 0):
    period = "Dusk"
else:
    period = "Night"
print(f"use the {period} picture")
