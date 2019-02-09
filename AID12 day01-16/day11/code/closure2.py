# closure.py

# 用局部变量保存压岁钱(不附合逻辑)

def child_buy(obj, m):
    money = 1000  # 爸爸给函数的压岁钱
    if money > m:
        money -= m
        print('买', obj, '花了', m, '元,剩余',
              money,'元')
    else:
        print("买", obj, '失败')

child_buy("变形金刚", 200)
child_buy('漫画三国', 100)
child_buy('手机', 1300)






