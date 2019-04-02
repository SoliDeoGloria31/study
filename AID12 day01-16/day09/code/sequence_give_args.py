

# 此示例示意序列传参
def myfun1(a, b, c):
    '''这是一个函数传参的示例'''
    print("a的值是:", a)
    print("b的值是:", b)
    print("c的值是:", c)

L1 = [11, 22, 33]
t2 = (100, 200, 300)
s3 = "ABC"

myfun1(L1[0], L1[1], L1[2])  # L1[0](将11)---> a, L1[1]--->b, ...
myfun1(*L1)  # 等同于myfunc(L1[0], L1[1], L1[2])
myfun1(*t2)
myfun1(*s3)


