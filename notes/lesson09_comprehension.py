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

lables = ["Yes" if "l" in w else "No" for w in words]
print(lables)
