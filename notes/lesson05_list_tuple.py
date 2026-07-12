# 5 列表与元组
# 5.1 list
fruits = ["apple", "banana", "cherry"]
# 取元素
print(fruits[0])
print(fruits[-1])  # 负数下标:即从右往左的第几个.
# 增加/压入
fruits.append("Durian")
print(fruits)
# 插入
fruits.insert(1, "blueburry")
print(fruits)
# 按值删除
fruits.remove("banana")
# 弹出
print(fruits.pop())  # 默认弹出最后一个元素
# 取长度
print(len(fruits))
# 混装列表
mix = [0, 1, 2.718281828, "Hello", True]
print(mix)

# 5.2 slice
# 切片的语法是[start(>=),end(<),step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:])  # 源列表拷贝
print(numbers[2:5])  # 2,3,4
print(numbers[:3])  # 0,1,2
print(numbers[7:])  # 7,8,9
print(numbers[::2])  # 0,2,4,6,8
print(numbers[::-1])  # 反转list

# 5.3 不可变列表 -tuple(元组) 元组声明赋值用小括号而不是中括号
totalRed = (255, 255, 0)
print(totalRed[0], totalRed[2])
#totalRed[1] = 233

# 5.4 列表排序
nums = [5, 2, 8, 1, 9]
# 如果nums = nums2 那么是引用拷贝,改动nums2时nums一样会改.
nums2 = nums.copy()
# 排序,改变源列表,返回None
nums2.sort()
print(nums2)
nums2.sort(reverse=True) #降序排序
print(nums2)
print(sorted(nums))#sorted函数返回是排序后的新列表.源列表不会更改
#聚合函数
print(max(nums), min(nums), sum(nums))
#判断存在与否
print(3 in nums)

# 找出最高分和最低分
# 用切片取出前3个
# 把整个列表倒序打印一遍（用[::-1]）
scores = [88, 92, 75, 100, 63, 59]
print(f"the max is {max(scores)}, the min is {min(scores)},前三个是{scores[:3]},\n 反转是{scores[::-1]}")
