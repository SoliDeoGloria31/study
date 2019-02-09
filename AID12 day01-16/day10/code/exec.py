# exec.py

s = '''
myadd = lambda x, y: x + y

print("20 + 30 =", myadd(20, 30))  # 50
print("1 + 2 =", myadd(1, 2))  # 3
'''

exec(s)