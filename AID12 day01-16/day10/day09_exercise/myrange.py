#   3. 写一个myrange()函数,参数可以传1~3个,实际意义同range函数
#     规则相同,此函数返回符合range(...) 函数规则的列表
#     如:
#       L = myrange(4)
#       print(L)  # [0, 1, 2, 3]
#       L = myrange(4, 6)
#       print(L)  # [4, 5]
#       L = myrange(1, 10, 3)
#       print(L)  # [1, 4, 7]


def myrange(start, stop=None, step=None):
    if stop is None:  # if not stop:
        stop = start
        start = 0
    if step is None:
        step = 1
    # 开始，结束和步长都已确定
    # return [x for x in range(start, stop, step)]
    if step > 0:  # 正向
        L = []
        while start < stop:
            L.append(start)
            start += step
        return L
    elif step < 0:
        L = []
        while start > stop:
            L.append(start)
            start += step
        return L

L = myrange(4)
print(L)  # [0, 1, 2, 3]
L = myrange(4, 6)
print(L)  # [4, 5]
L = myrange(1, 10, 3)
print(L)  # [1, 4, 7]

L2 = myrange(10, 0, -2)
print(L2)


