# nonlocal.py


v = 100

def f1():
    v = 200
    print("f1.v=", v)
    # 此外嵌入另一个函数
    def f2():
        nonlocal v  # 声明v为外部嵌套函数作用域的变量
        v = 300
        print("f2.v=", v)
    f2()
    print("f1执行后f1.v=", v)

f1()

