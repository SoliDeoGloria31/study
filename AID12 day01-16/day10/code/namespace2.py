# namespace2.py


# 此示例示意python的作用域
v = 100
def fun1():
    # v = 200
    print('fun1.v=', v)  # ???
    def fun2():
        # v = 300
        print('fun2.v=', v)  # ???
    fun2()

fun1()
print("全局的v=", v)  # 100


