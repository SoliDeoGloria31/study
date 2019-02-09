# 练习:
#   执行以下程序,看执行结果是什么?为什么?
#   L = [1, 2, 3]
#   v = 100
#   def f1():
#       L.append(4)
#       v = 200
#   f1()
#   print(L)  # ???
#   print(v)  # ???

#   def f2():
#       L += [5]
#       v += 1
#   f2()  # 此处会怎么样?为什么?
  



L = [1, 2, 3]
v = 100
def f1():
    L.append(4)
    v = 200
f1()
print(L)  # ???
print(v)  # ???

def f2():
    L.extend([5])
    # L += [5]  # 出错
    v += 1  # 出错
f2()  # 此处会怎么样?为什么?

print(L)
print(v)

