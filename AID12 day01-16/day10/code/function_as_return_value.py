# function_as_return_value.py

def get_function():
    s = input("请输入您要做的操作: ")
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 4, 6, 8, 10]
f = get_function()   # ??? f绑定什么?
print("f绑定:", f)
print(f(L))









