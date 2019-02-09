# 练习:
#   用全局变量记录一个函数fx调用的次数,部分代码如下:
#   count = 0
#   def fx(name):
#       print("你好", name)
#       .... # 此处自己实现
#   fx('小张')
#   fx('小李')
#   print("fx函数共被调用", count, '次')  # 2


count = 0
def fx(name):
    print("你好", name)
    global count
    count += 1
fx('小张')
fx('小李')
print("fx函数共被调用", count, '次')  # 2
