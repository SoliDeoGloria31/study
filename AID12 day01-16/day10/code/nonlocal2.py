# nonlocal.py


# 3. 当有两层或两层以上函数嵌套时,访问nonlocal变量只对最近
#    一层变量进行操作

v = 100

def f1():
    v = 200
    print("f1.v=", v)
    # 此外嵌入另一个函数
    def f2():
        v = 300
        # 再嵌入另一个函数
        def f3():
            nonlocal v
            v = 400
        f3()
        print("f2.v=", v)  # 400
    f2()
    print("f1执行后f1.v=", v)

f1()

