#   2. 用filter函数,将1~100之间所有的素数prime 放入到列表中,
#      再打印这个列表


# 写一个函数,is_prime(x), 判断如果x是素数返回True, 否则返回False
def is_prime(x):
    if x < 2:  # 小于2的数没有素数
        return False
    # 大于等于2的数.如果能被2, 3, 4, ... x -1 整数,就不是素数
    for i in range(2, x):
        if x % i == 0:
            return False  # x不是素数
    # 走到此处,则x一定为素数
    return True

# 方法1
L1 = list(filter(is_prime, range(100)))
print("L1=", L1)

L2 = [x for x in filter(is_prime, range(100))]
print("L2=", L2)

L3 = [x for x in range(100) if is_prime(x)]
print("L3=", L3)






