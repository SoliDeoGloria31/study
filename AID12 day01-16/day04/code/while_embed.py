#   2. 写程序,打印1~20的整数,打印在一行内
#       1 2 3 4 5 6 7 8 ...... 19 20
#   将以上内容打印20行

j = 1
while j <= 10:
    # print('1 2 3 4 5 6 7 ... 19 20')
    i = 1
    while i <= 20:
        print(i, end=' ', flush=True)
        i += 1
    print()  # 换行print(sep=' ', end='\n', flush=False)
    j += 1




