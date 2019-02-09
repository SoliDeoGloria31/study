#   3. 写一个函数计算: 
#     1 + 2**2 + 3**3 + ... + n ** n的和
#     (n给个小点的数来进行测试)

# 方法1
# def mysum(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += x ** x
#     return s

# 方法2
# def mysum(n):
#     s = sum([x ** x for x in range(1, n + 1)])
#     return s

# 方法3
def mysum(n):
    return sum(map(lambda x: x**x, range(1, n+1)))

print(mysum(3))  # 32

