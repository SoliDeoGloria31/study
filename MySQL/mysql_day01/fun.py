# -*- coding: utf-8 -*-

# fun.py
# 按照一定概率产生福
# 爱国福 30%，敬业福 10%，和谐福 30%，友善福 20%，富强福 10%
# 0 ~ 99 随机数

import random

f1, f2, f3, f4, f5 = 0, 0, 0, 0, 0


def gen_fu():
    global f1, f2, f3, f4, f5
    num = random.randint(0, 99)       # 产生[0,99] 100个整数
    if 0 <= num <= 29:                # 爱国福 30%
        f1 += 1
    elif 30 <= num <= 39:             # 敬业福 10%
        f2 += 1
    elif 40 <= num <= 69:             # 和谐福 30%
        f3 += 1
    elif 70 <= num <= 89:             # 友善福 20%
        f4 += 1
    else:                             # 富强福 10%
        f5 += 1


for i in range(10000000):
    # print('%d' % i)
    gen_fu()                          # 产生福

total = f1 + f2 + f3 + f4 + f5
print('爱国福:%f' % (f1 / total))
print('敬业福:%f' % (f2 / total))
print('和谐福:%f' % (f3 / total))
print('友善福:%f' % (f4 / total))
print('富强福:%f' % (f5 / total))
