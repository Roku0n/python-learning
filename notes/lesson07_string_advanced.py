##7 String Advanced
# 7.1 不可变性 Non-mutable
s = "hello"
s2 = s.replace("h", "H")
print(s)
print(s2)
print(id(s), id(s2))
# 切片语法 但不能反向赋值
print(s[1:3], s[::-1])
# s[0:2] = "LE" 'str' object does not support item assignment

# 7.2 查找与判断
text = "hello world"
# index必须在find之前使用 否则会报错.不存在的find会返回-1
print(text.find("world"), text.find("xyz"), text.index("world"))  # 6,-1,6
print(text.startswith("hello"), text.endswith("world"), text.count("o"))  # true,true,2

# 判断是否全是数字/全是字母/全是字母或数字/全是空白字符
c = "5"
print(
    c.isdigit(), c.isalpha(), "a".isalpha(), "a1".isalnum(), " ".isspace()
)  # True,False,True,True,True

# 7.3 变形和清洗类
raw = "  hello world   "
# strip去两端空白 左边空白 右边空白和指定字符
print(raw.strip(), raw.lstrip(), ",", raw.rstrip(), "xxhelloxxxx".strip("x"))
# 全大写/全小写/每个单词字母大写/首字母大写
print(
    "hello".upper(), "HELLO".lower(), "hello world".title(), "hello world".capitalize()
)
# 分离 split方法不传任何参数时按空格分割
print("a,b,c".split(","), "a  b   c".split())
# join:join是连字符的方法
alphabets = ["a", "b", "c"]
result = "-".join(alphabets)
print(result)

# 7.4 格式化
price = 1234.5678
print(f"{price:.2f}")  # 1234.57 保留两位小数
print(f"{price:,.2f}")  # 1,234.57 千分位,2位小数

name = "Alice"
print(f"{name!r}")  # 'Alice' 加引号
# 补零:将输出字符串撑到参数的位数,不足处用0补齐
print("7".zfill(3), "42".zfill(5))

# 7.5 编码
# python的str默认就是unicode码点序列
s = "안녕하세요"
b = s.encode("utf-8")
s2 = b.decode("utf-8")
print(s, b, s2, len(s), len(b))

# 7.6 类型转换
# str number
print(int(42), int(float(3)), str(42))
# 字母表偏移
print(ord("a"), ord("A"), chr(97))
a = "a"
shifted_a = chr(ord(a) + 3)
print(shifted_a)

# 7.7 性能问题
# 坏实现
result = ""
for i in range(5):
    result += str(i)  # 每次循环都创造一个新字符串对象,O(n^2)
# 好实现
parts = []
for i in range(5):
    parts.append(str(i))
result = "".join(parts)  # O(n)


# 题目1 回文判断
def is_palindrome(s: str) -> bool:
    reversed_s = s[::-1]
    return reversed_s == s


def is_palindrome_advance(s: str) -> bool:
    washed_s = s.replace(" ", "").lower()
    return washed_s == washed_s[::-1]


# 驼峰转蛇箱
def camel_to_snake(s: str) -> str:
    parts = []
    word_start = 0
    s2 = s.lower()
    for i in range(len(s)):
        if s[i].isupper():
            parts.append(s2[word_start:i])
            word_start = i
    parts.append(s2[word_start : len(s)])
    return "_".join(parts)


# 凯撒密码
ORD_A = ord("A")
ORD_Z = ord("Z")
ORD_LOWER_A = ord("a")
ORD_LOWER_Z = ord("z")


def caesar_cipher(s: str, shift: int) -> str:
    alphabets = []
    for char in s:
        ord_char = ord(char)
        if ORD_A <= ord_char <= ORD_Z:
            alphabets.append(chr(ORD_A + (ord_char - ORD_A + shift) % 26))
        elif ORD_LOWER_A <= ord_char <= ORD_LOWER_Z:
            alphabets.append(chr(ORD_LOWER_A + (ord_char - ORD_LOWER_A + shift) % 26))
        else:
            alphabets.append(char)
    return "".join(alphabets)
