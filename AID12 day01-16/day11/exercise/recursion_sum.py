# 练习:
#   写一个递归求和函数:
#     def mysum(n):
#          ...
#     此函数求 1 + 2 + 3 + 4 + ..... + n 的和

#     print(mysum(100))  # 5050


def mysum(n):
    if n == 1:
        return 1
    # 其它情况
    return n + mysum(n-1)


print(mysum(100))  # 5050

