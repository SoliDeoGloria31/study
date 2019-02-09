# 3. 不能先声明局部变量，再用global声明为全局变量，此做法不
#    附合规则


v = 100
def fx():
    v = 200
    global v
    v += 300
    print("v=", v)  # ??
fx()
print(v)  # ????