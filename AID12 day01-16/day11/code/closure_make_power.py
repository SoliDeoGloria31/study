# closure_make_power.py

# 此示例示意闭包的应用

# 写一个求x的平方的函数
# def pow2(x):
#     return x**2
# 写一个求x的立方的函数
# def pow3(x):
#     return x**3

# 写一个求x的102次方的函数
# def pow102(x):
#     return x**102

# 写一个求x的150次方的函数
# def pow150(x):
#     return x**150

# 用闭包实现上述功能
def make_power(y):
    def fn(x):
        return x ** y  # y为外部嵌套函数的变量
    return fn

pow2 = make_power(2)
print('5的平方是:', pow2(5))
print('6的平方是:', pow2(6))
pow3 = make_power(3)
print('7的立方是:', pow3(7))
# ....
pow150 = make_power(150)
print(pow150(2))

