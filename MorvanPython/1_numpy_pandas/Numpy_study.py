# -*- coding: utf-8 -*-
# 1
# import numpy as np
#
# array = np.array([[1, 2, 3], [2, 3, 4]])   # 列表转换为矩阵/数组
# print(array)
#
# print('number of dim:', array.ndim)  # 维度
# print('shape:', array.shape)         # 行数和列数
# print('size:', array.size)           # 元素个数

# 2

# import numpy as np
# a = np.array([[2, 23, 4], [2, 23, 4]], dtype=np.int)
# print(a)
#
# b = np.zeros((3, 4))
# print(b)
#
# c = np.ones((3, 4), dtype=np.int16)
# print(c)
#
# d = np.empty((3, 4))
# print(d)
#
# e = np.arange(10, 30, 2)
# print(e)
#
# f = np.arange(12).reshape((3,4))
# print(f)
#
# g = np.linspace(1,10,5).reshape((5,1))
# print(g)

# # 3
# import numpy as np
# # a = np.array([10, 20, 30, 40])
# # b = np.arange(4)
# # print(a, b)
# # c = a + b
# # print(c)
# # d = a - b
# # print(d)
# # e = b**2
# # print(e)
# # f = 10 * np.sin(a)
# # print(f)
# # print(b)
# # print(b < 3)
#
# # a = np.array([[1, 1], [0, 1]])
# # b = np.arange(4).reshape((2, 2))
# #
# # c = a * b
# # c_dot = np.dot(a, b)
# # c_dot_2 = a.dot(b)
# #
# # print(a)
# # print(b)
# # print(c)
# # print(c_dot)
# # print(c_dot_2)
#
# a = np.random.random((2, 4))
# print(a)
# print(np.sum(a))
# print(np.sum(a, axis=0))   # 每列求和
# print(np.sum(a, axis=1))   # 每行求和
# print(np.min(a))
# print(np.max(a))

# 4

# import numpy as np
#
# A = np.arange(2,14).reshape(3,4)
# print(A)
#
# print(np.argmin(A))   # 最小值的索引
# print(np.argmax(A))   # 最大值得索引
# print(np.mean(A))     # 求平均值，以下三行等价
# print(A.mean())
# print(np.average(A))
#
# print(np.median(A))   # 中位数
# print(np.cumsum(A))   # 累加，类似于斐波拉契数列
# print(np.diff(A))     # 差值
#
# print(np.nonzero(A))  # 找非零，以下为 行数、列数的数组
# # (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))
#
# print(np.sort(A))     # 排序
#
# print(np.transpose(A))  # 矩阵反向(转置)
# print(A.T)              # 与上行等价
#
# print(np.clip(A,5,9))   # Array指的是将要被执行用的矩阵，而后面的最小值最大值则用于让函数判断矩阵中元素是否有比最小值小的或者比最大值大的元素，并将这些指定的元素转换为最小值或者最大值。
# print(np.mean(A,axis=0))

# 5
#
# import numpy as np
#
# A = np.arange(3, 15).reshape((3, 4))
# print(A)
# print(A[2])      # 按行索引
# print(A[1][1])   # A的第2行第2列数字
# print(A[1, 1])   # 与上行等价
# print(A[:, 1])   # 第2列
#
# for column in A.T:  # 对A.T按行索引，等价于对A按列索引
#     print(column)
#
# for row in A:       # 对A按行索引
#     print(row)
#
# print(A.flatten())  # flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。而flat是一个迭代器，本身是一个object属性
# for item in A.flat:
#     print(item)

# 6

# import numpy as np
#
# A = np.array([1, 1, 1])
# B = np.array([2, 2, 2])
#
# print(np.vstack((A, B)))   # vertical stack 上下合并
#
# C = np.vstack((A, B))      # vertical stack   上下合并
# D = np.hstack((A, B))      # horizontal stack 左右合并
# print(D)
# print(A.shape, D.shape)
#
# print(A.reshape(3, 1))
#
# C = np.concatenate((A, B, B, A), axis=0)
# print(C)
# D = np.concatenate((A, B, B, A), axis=1)
# print(D)

# 7

# import numpy as np
#
# A = np.arange(12).reshape(3, 4)
# print(A)
#
# print(np.split(A, 2, axis=1))  # 对每行分割，每行分为2段，等量分割
# # [array([[0, 1],
# #        [4, 5],
# #        [8, 9]]), array([[ 2,  3],
# #        [ 6,  7],
# #        [10, 11]])]
#
# print(np.array_split(A, 3, axis=1))  # 对每行分割，每行分为3段，不等量分割
# # [array([[0, 1],
# #        [4, 5],
# #        [8, 9]]), array([[ 2],
# #        [ 6],
# #        [10]]), array([[ 3],
# #        [ 7],
# #        [11]])]
#
# print(np.vsplit(A,3))
# print(np.hsplit(A,2))

# 8

import numpy as np
a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b is a)

