# 练习:
#   试写一个生成器函数 myfilter,要求此函数与系统内建的filter
#   函数功能完全一致
#     如:
#         def myfilter(fn, iterable):
#             ....
        
#         for y in myfilter(lambda x: x%2==0, range(10)):
#             print(y)




def myfilter(fn, iterable):
    for x in iterable:
        if fn(x):
            yield x

for y in myfilter(lambda x: x%2==0, range(10)):
    print(y)