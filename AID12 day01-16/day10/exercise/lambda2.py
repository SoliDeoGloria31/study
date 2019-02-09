#   2. 写一个lambda 表达式来创建函数，此函数返回两个形参变量的最
#   　　大值
#     def mymax(x, y):
#         ...
#     mymax = lambda ......
#     print(mymax(100, 200))  # 200
#     print(mymax("100", "20"))  # 20  <-- 注意这是字符串



# def mymax(x, y):
#     if x > y:
#         return x
#     return y

# def mymax(x, y):
#     return x if x > y else y

mymax = lambda x, y: x if x > y else y
print(mymax(100, 200))  # 200
print(mymax("100", "20"))  # 20  <-- 注意这是字符串

