# 练习:
#   写一个计算公式的解释执行器
#     已知有如下一些函数:
#         def myadd(x, y):
#             return x + y
#         def mysum(x, y):
#             return x - y
#         def mymul(x, y):
#             return x * y
#       ...
#     定一个带有一个参数的函数 get_func(s):
#         def get_func(s):
#             ...  # 此处自己实现
#     此函数的在传入字符串"加"或"+" 返回myadd函数;
#     此函数的在传入字符串"乘"或"*" 返回mysum函数, ...
#     在主函数中程序如下:
#         def main():
#             while True:
#                 s = input("请输入计算公式: ")  # 10 加 20
#                 L = s.split()  # L = ['10', '加', '20']
#                 a = int(L[0])
#                 b = int(L[2])
#                 fn = get_func(L[1])
#                 print("结果是:", fn(a, b))  # 结果是: 30





def myadd(x, y):
    return x + y
def mysub(x, y):
    return x - y
def mymul(x, y):
    return x * y

def get_func(s):
    if s == '加' or s == '+':
        return myadd
    elif s == '减' or s == '-':
        return mysub
    elif s in ('乘', '*'):
        return mymul

def main():
    while True:
        s = input("请输入计算公式: ")  # 10 加 20
        L = s.split()  # L = ['10', '加', '20']
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))  # 结果是: 30

main()