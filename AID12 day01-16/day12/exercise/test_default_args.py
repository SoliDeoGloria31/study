L = [1, 2, 3]
def f(n=0, lst=None):
    if lst is None:
        lst = []  # 创建一个新的空列表
    lst.append(n)
    print(lst)

f(4, L)  # [1, 2, 3, 4]
f(5, L)  # [1, 2, 3, 4, 5]
f(100)  # [100]
f(200)  # [200]

