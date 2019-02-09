# mydeco1.py


# 此示例示意装饰器的原理和语法
def mydeco(fn):
    def fx():
        print("++++++++++++++++++")
        fn()
        print("------------------")
    return fx


@mydeco
def myfunc():
    '''被装饰函数'''
    print("函数myfunc被调用!")

# myfunc = mydeco(myfunc)  # 上面的@mydeco 等同于此句

myfunc()
myfunc()
myfunc()
