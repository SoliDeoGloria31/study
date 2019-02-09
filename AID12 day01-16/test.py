# -*- coding: utf-8 -*-

# def f(n):
#     a,b =1,1
#     while a <=n:
#         print(a,end=' ')
#         a,b=b,a+b
#     print()
#
# f(100)

# L = list(range(10))
# for x in L:
#     L.remove(x)
# print("L=", L)  # 请问是空列表吗？

# L=dict([(1, "壹"), (2, '二')])
# print(L)

# def myadd(x,y):
#     return x+y
#
# a = int(input('a= '))
# b = int(input('b= '))
# print('a+b= ',myadd(a,b))

# def myfun(a,b,c):
#     print('a=',a)
#     print('b=',b)
#     print('c=',c)
#
# d1={'c':33,'a':11,'b':22}
# myfun(c=d1['c'],a=d1['a'],b=d1['b'])
#
# print()
# myfun(**d1)

# myfun(1,2,3)
#
# L1 = [11,12,13]
# t2=(100,200,300)
# s3='ABC'
#
# myfun(*L1)
# myfun(*t2)
# myfun(*s3)


# L=[1,2,True,None,3.14]
#
# # def myfun(*args):
# #     for l in args[0:len(args)-2]:
# #         print(str(l),end='#')
# #     print(str(args[len(args)-1]))
# #
# # myfun(*L)
# print(*L,sep='#')


# L = [1,2,3,4]
# t = (1.1,2.2,3.3,4.4)
#
# def myfun(x):
#     x +=(5,)
#     print('x= ',x)
#
# myfun(L)
# print(L)
#
# myfun(t)
# print(t)

# L=[]
# def myfun(l):
#     while True:
#         x = int(input('x= '))
#         if x < 0:
#             break
#         l.append(x)
#
# myfun(L)
# print(L)
# myfun(L)
# print(L)


# def info(name, age=1, address='不详'):
#     print(name,'今年', age, '岁,家庭住址:', address)
#
# info("魏明择", 35, '北京市朝阳区')
# info("tarena", 15)
# info("小飞")

a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    # 此处有多少个局部变量?
    print("locals()返回:", locals())
    # 此处有多少个全局变量?
    print("globals() 返回:", globals())
    print(c)  # 100
    print(globals()['c'])  # 3


fn(100, 200)