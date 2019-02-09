#   1. 写一个函数mysum(n) ，此函数用来计算
#      1 + 2 + 3 + 4 + ... + n 的和
#      (要求: 不允许调用sum)
#     如:
#       print(mysum(100))  # 5050
#       print(mysum(4))  # 10


# def mysum(n):
#     s = 0
#     for x in range(1, n + 1):
#         s += x
#     return s

def mysum(n):
    return sum(range(1, n + 1))

print(mysum(100))  # 5050
print(sum(range(1, 101)))
print(mysum(4))  # 10
