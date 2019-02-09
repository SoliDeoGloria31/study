# 面积 = 圆周率 * 半径**2
# 半径 = math.sqrt(面积/圆周率)


# 练习:
#   1. 输入一个圆的半径,打印出这个圆的面积
import math  # 导入math模块
r = float(input("请输入圆的半径: "))
area = math.pi * r ** 2
print("半径为:", r, '的圆的面积是:', area)

#   2. 输入一个圆的面积,打印出这个圆的半径
area2 = float(input("请输入圆的面积: "))
r2 = math.sqrt(area2 / math.pi)
print('面积为: ', area2, '的圆的半径是:', r2)


