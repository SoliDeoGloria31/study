# map2.py

# 生成一个可迭代对象,此可迭代对象可以生成
#   1**4, 2**3, 3**2, 4**1
# pow(x, y, z=None)  内建函数


for x in map(pow, [1, 2, 3, 4], [4, 3, 2, 1]):
    print(x)   # 1, 8, 9, 4

print('-----------')
for x in map(pow, [1,2,3,4],
                   [4, 3, 2, 1, 0],
                   range(5, 10)):
    print(x)  # 1, 2, 2, 4

