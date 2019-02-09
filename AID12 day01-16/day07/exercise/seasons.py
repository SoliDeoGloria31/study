# 练习:
#   写程序,实现以下要求:
#   1. 将如下数据形成一个字典seasons
#     '键'         '值'
#      1  -----> '春季有1,2,3月'
#      2  -----> '夏季有4,5,6月'
#      3  -----> '秋季有7,8,9月'
#      4  -----> '冬季有10,11,12月'

#     让用户输入一个整数代表这个季度,打印这个季度的信息,如果用户
#     输入的信息不在字典内,则打印"信息不存在"

# 方法1
# seasons = {
#     1: '春季有1,2,3月',
#     2: '夏季有4,5,6月',
#     3: '秋季有7,8,9月',
#     4: '冬季有10,11,12月'
# }
# 方法2
seasons = {}
seasons[1] = '春季有1,2,3月'
seasons[2] = '夏季有4,5,6月'
seasons[3] = '秋季有7,8,9月'
seasons[4] = '冬季有10,11,12月'

# print(seasons)
x = int(input('请输入季度(1~4):'))
if x in seasons:
    print(seasons[x])
else:
    print("信息不存在")




