# 9 Comprehension

# use for loop to build a new list from range
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)
## 9.1 list comprehension
#[expression for item in iterable if condition]
squares2 = [x ** 2 for x in range(10)]
print(squares2)
# use for loop and if condition to build a new list from range
evens = []
for x in range(20):
    if x % 2 == 0:
        evens.append(x)

evens2 = [x for x in range(20) if x%2 == 0]
print(evens2)

#2-dimension read
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#flat = [] 
#for row in matrix:
#    for i in row:
#        flat.append(i)
flat = (i for row in matrix for i in row)

#expression can be if or function/method result
words = ['hello', 'world','python']
upper_words = [word.upper() for word in words]
print(upper_words)

lengths = [len(w) for w in words]
print(lengths)
#if-else structure in comprehension
lables = ["Yes" if "l" in w else "No" for w in words]
print(lables)

#dict/set comprehension
square_dict = {x : x**2 for x in range(5)}
unique_length = {len(w) for w in ["a", "bb", "ccc", "dd"]}
'''
1.用列表推导式，从range(1, 101)中筛选出所有3或5的倍数（提示：用or组合两个条件）
2.给定words = ["apple", "Banana", "cherry", "Date"]，用列表推导式生成一个新列表，首字母大写的单词保留原样，首字母小写的单词整体转成大写（提示：用.isupper()判断首字母，配合表达式部分的if...else）
3.给定嵌套列表matrix = [[1,2,3],[4,5,6],[7,8,9]]，用字典推导式生成{行号: 该行总和}的字典，比如结果应该是{0: 6, 1: 15, 2: 24}（提示：需要用到enumerate()
'''
multiples = [x for x in range(1, 101) if x%3 ==0 or x%5 ==0]

words = ["apple", "Banana", "cherry", "Date"]
new_words = [w if w[0].isupper() else w.upper() for w in words]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
indexs_sums_dict = {i:sum(row) for i,row in enumerate(matrix)}