#   3. 从凌晨0:0:0 计时，到现在已经过了 63320 秒
#      请问现在是几时，几分，几秒,写程序打印出来
#     (提示: 用地板除和求余实现)


s = 63320  # 秒

hour = s // 60 // 60  # 小时
minute = s // 60 % 60   # 求分钟   s % 3600 // 60
second = s % 60  # 求秒

print(hour, ':', minute, ':', second)

