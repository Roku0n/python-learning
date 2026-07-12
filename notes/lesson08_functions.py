# 8 Functions
import copy
# 8.1 Function Definition
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# 8.2 default arguments
def greet2(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet2("Bob")) 
print(greet2("Charlie", "Hi"))
# but default arguments must not be mutable types like list or dict.
def add_item(item,my_list=[]):
    my_list.append(item)
    return my_list
print(add_item("a"))
print(add_item("b")) #the list will be created only once, the second call will use the same list created in the first call. 
# so use None as default value in mutable types of arguments.
def add_item2(item, my_list = None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
## 8.3 *args
def comprod(*nums):
    total = 1
    for num in nums:
        total *= num
    print(type(nums)) #all args will be packaged as a TUPLE
    return total

print(comprod(1,2,3,4,5,6,7))

## 8.3 kwargs 
#kwargs is a dict and the keys must be strings.
def print_info(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items() :
        print(f"{key}:{value}")
print_info(name="Alice", age=30, city="NYC")
### 8.4 sequence of arguments
#normal arguments -> *args -> default arguments -> **kwargs
def full_example(a, b, *args,c =0, **kwargs):
    print(f"a={a}, b={b}, c={c},args={args},kwargs={kwargs}")
full_example(1, 2, 3, 4, c=99, d=5, e=6)
##8.5 Python Dont have function overload 
#def foo(x):
#    print(f"foo with one argument: {x}")
def foo(x, y):
    print(f"foo with two arguments: {x}, {y}")
foo(1, 2)  # This will call the second foo function

# practice describe_pets
def describe_pet(name, animal_type = "dog",**extra_info):
    describe = f"the pets name is {name}. It is a/an {animal_type}. "
    extra_list = []
    for key,value in extra_info.items():
        extra_list.append(f"Its {key} is {value}.")
    describe += " ".join(extra_list)
    print(describe)
## logger
def call_logger(func, *args,**kwargs):
    """
    调用func，并打印出：
    1. 调用时传入的所有位置参数和关键字参数
    2. 函数的返回值
    然后返回func的执行结果
    """
    print(f" Calling {func.__name__} with args={args}, kwargs={kwargs}")
    result = func(*args,**kwargs)
    print(f"the result is {result}")
    return result        

def add(a, b):
    return a + b

def greet3(name, greeting="Hello"):
    return f"{greeting}, {name}!"

call_logger(add, 3, 5)
call_logger(greet3, "Alice", greeting="Hi")

## Config Meger
def merge_config(overrides = None, base_config :dict ={"debug": False, "options":{"retries":3,"timeout":10}}):
    """
    把overrides合并进base_config，返回合并后的新配置。
    overrides是一个dict，可能包含顶层key，也可能包含options里的嵌套key。
    """
    if overrides is None :
        return base_config 
    config = copy.deepcopy(base_config)
    if overrides.get("debug") is not None :
        config["debug"] = overrides["debug"]
    if overrides.get("options") is not None:
        if overrides["options"].get("retries") is not None:
            config["options"]["retries"] = overrides["options"]["retries"]
        if overrides["options"].get("timeout") is not None:
            config["options"]["timeout"] = overrides["options"]["timeout"]
    return config

config1 = merge_config()
print(config1)  # {'debug': False, 'options': {'retries': 3, 'timeout': 10}}

config2 = merge_config({"debug": True})
print(config2)  # {'debug': True, 'options': {'retries': 3, 'timeout': 10}}

config3 = merge_config({"options": {"timeout": 30}})
print(config3)  # {'debug': False, 'options': {'retries': 3, 'timeout': 30}}

# 关键验证：改config1，看config3会不会被牵连（如果实现有问题，这里会暴露）
config1["debug"] = True
config1["options"]["retries"] = 999
print(config3) 
