# 练习:
#   写一个程序,输入你的出生日期(年月日)
#     1) 算出你已经出生了多少天?
#     2) 算出你出生那天是星期几?

import time

y = int(input("请输入出生的年: "))
m = int(input("请输入出生的月: "))
d = int(input("请输入出生的日: "))

t = (y, m, d, 0, 0, 0, 0, 0, 0)
# 先得到出生时,计算机计时秒数, 得到当前时间秒数
birth_time_sec = time.mktime(t)
life_sec = time.time() - birth_time_sec  # 活了多少秒
life_days = life_sec / 60/ 60 // 24
print("您已出生", life_days, '天')

birth_tuple = time.localtime(birth_time_sec)

weeks = {
    0: '星期一',
    1: '星期二',
    2: '星期三',
    3: '星期四',
    4: '星期五',
    5: '星期六',
    6: '星期日'
}
print("您出生那天是:", weeks[birth_tuple[6]])
# print(birth_tuple[6])  # 星期几?