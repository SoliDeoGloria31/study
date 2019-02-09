#   2. 完全数: 
#      1 + 2 + 3 = 6 (6为完全数)
#      1, 2, 3都为6的因数(能被一个数x整除的数为y,则y为x的因数)
#      1 x 6 = 6
#      2 x 3 = 6
#      完全数是指除自身以外的所有因数之和相加等于自身的数
#       求4~5个完全数,并打印
#      答案:
#        6
#        28
#        496
#        ...

def is_perfect_number(x):
    '''此函数判断x是否为完全数，如果是返回True,否则返回False'''
    L = []  # 创建一个列表，用来存放x所有的因数
    for i in range(1, x):
        if x % i == 0:  # 整除了，i则一定是x的因数
            L.append(i)
    if sum(L) == x:  # 是完全数
        return True
    return False

def main():
    i = 2
    while True:
        # 如果i是完全数，则打印i的值
        if is_perfect_number(i):
            print(i)

        i += 1
    
main()
