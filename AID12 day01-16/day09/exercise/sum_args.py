# 练习:
#   写一个函数 mysum 可以传入任意个数字实参,返回所有实参的和
#     def mysum(*args):
#         ...
    
#     print(mysum(1, 2, 3, 4))  # 10
#     print(mysum(1, 3, 5, 7, 9))  # 25


# 方法1
# def mysum(*args):
#     s = 0
#     for x in args:
#         s += x
#     return s

# 方法2
def mysum(*args):
    return sum(args)

print(mysum(1, 2, 3, 4))  # 10
print(mysum(1, 3, 5, 7, 9))  # 25

