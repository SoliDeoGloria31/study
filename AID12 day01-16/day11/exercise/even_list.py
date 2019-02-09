#   1. 用filter 生成能够提供偶数可迭代对象,生成1 ~ 20 的偶数,
#      将这些偶数存于列表中,再打印这个列表(不包含20)

flt = filter(lambda x: x % 2 == 0, range(1, 20))
L = list(flt) 
print(L)  # [2, 4, 6, 8 ...]

L2 = [x for x in flt]
print("L2=", L2)  # 空列表