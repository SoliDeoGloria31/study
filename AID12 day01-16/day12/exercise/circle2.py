# 面积 = 圆周率 * 半径**2
# 半径 = math.sqrt(面积/圆周率)


# 练习:
#   1. 输入一个圆的半径,打印出这个圆的面积
import math as m

r = float(input("请输入圆的半径: "))
area = m.pi * r ** 2
print("半径为:", r, '的圆的面积是:', area)

#   2. 输入一个圆的面积,打印出这个圆的半径
area2 = float(input("请输入圆的面积: "))
r2 = m.sqrt(area2 / m.pi)
print('面积为: ', area2, '的圆的半径是:', r2)


