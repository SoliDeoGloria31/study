# death_loop.py

# 任意输入一些整数,当输入负数时结束输入,当输入完成后,打印您
# 输入的这些数的和
# 如:
#   请输入: 1
#   请输入: 2
#   请输入: 3
#   请输入: 4
#   请输入: -1
# 打印:
#   您刚才输入的这些数的和是: 10

s = 0  # 此变量用来记录累加和

while True:
    x = int(input("请输入: "))
    if x < 0:
        break  # 终止当前循环
    s += x

print("您刚才输入的这些数的和是:", s)