#   1 . 输入一个整数，代表正方形的宽和高，打印相应的正方形
#       用for语句实现
#     如:
#       请输入: 5
#     打印:
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5
#       1 2 3 4 5

w = int(input('请输入: '))
for _ in range(w):  #  外重循环控制行数
    # 内重循环打印一行
    for x in range(1, w + 1):
        print(x, end=' ')
    print()  # 换行


