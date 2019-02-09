#   1. 写程序算出1~20的阶乘的和,即:
#     1!+2!+3!+4!+......+19!+20!

def myfac(x):
    if x == 0:
        return 1
    return x * myfac(x-1)

# 方法1
# s = 0
# for x in range(1, 21):
#     s += myfac(x)
# print('和是:', s)

# 方法2
print("和是:", sum(map(myfac, range(1, 21))))

