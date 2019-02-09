# 练习:
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据为字符串的反序:
#      'moT'   'yrreJ'   'skipS'     'ekyT'
#   排序的结果为:
#      ['Spike', 'Tyke', 'Tom', 'Jerry']
#   请问如何用sorted进行排序



def reverse_str(s):
    '''s绑定需要排序的可迭代对象提供的元素'''
    r = s[::-1]  # 把转原字符串
    print("要排序的元素:", s, '排序的依据是:', r)
    return r

names = ['Tom', 'Jerry', 'Spike', 'Tyke']

L = sorted(names, key=reverse_str)

print(L)  #  ['Spike', 'Tyke', 'Tom', 'Jerry']






