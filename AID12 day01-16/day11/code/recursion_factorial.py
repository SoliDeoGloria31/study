# recursion_factorial.py
#      1   (如果n为0)
#    /
# n! 
#    \  n * (n-1)!  (如果n不为零时)

def myfac(n):
    if n == 0:  # 0! 为 1
        return 1
    else:
        return n * myfac(n-1)  # n! = n * (n-1)!

print(myfac(5))  # 120