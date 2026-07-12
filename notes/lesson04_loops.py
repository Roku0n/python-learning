# 4 for与while循环
# 4.01 for循环
# for循环本质是迭代器驱动的遍历操作,和传统for(int i = 0,i<array.length(),i++)完全不同
for i in range(5):
    print(i)
## range((起点>=),终点<,(步长)):生成自然数. 左闭右开的区间在python哪哪都是.
# 4.02 字符串遍历
chaebols = ["Samsung", "Hyundai", "LG", "SK"]
for company in chaebols:
    print(company)
# 需要下标时
for index, company in enumerate(chaebols):
    print(index, company)
# 逐字符遍历
for char in "Giannis Antetokounmpo":
    print(char)
# 4.03 while循环
count = 0
while count < 5:
    print(count)
    count += 1  ##python没有++和--运算符
# break和continue关键字和其他语法一样.
for i in range(1, 101):
    if i % 3 == 0:
        continue
    else:
        print(i)
