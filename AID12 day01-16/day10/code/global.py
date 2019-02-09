v = 100
def f1():
    global v  # 全局声明语句
    v = 200  # 要想让此语句来修改全局变量v怎么办？

f1()
print(v)  # 200