
#   3. 改写之前的学生信息管理程序:
#     用两个函数来封装功能的代码块
#        函数1:  input_student()   # 返回学生信息字典的列表
#        函数2:  output_student(L)  # 打印学生信息的表格
    
def input_student():
    L = []  # 创建一个列表,准备存放学生数据的字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果用户输入空字符串就结束输入
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        d = {}  # 一定要每次都创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)   # 把d加入列表中L
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        name = d['name']
        age = str(d['age'])  # 转为字符串
        score = str(d['score'])  # 转为字符串
        print("|%s|%s|%s|" % (name.center(15), 
                            age.center(10),
                            score.center(10)))
    print("+---------------+----------+----------+")

def delete_student(L):
    name = input("请输入要删除学生的姓名: ")
    i = 0  # i 代表列表的索引
    while i < len(L):
        d = L[i]  # d绑定字典
        if d['name'] == name:
            del L[i]
            print("删除", name, "成功!")
            break
    else:
        print("删除失败!")

def modify_student_score(L):
    pass

def show_menu():
    '''显示菜单'''
    print("+--------------------------+")
    print("| 1) 添加学生信息          |")
    print("| 2) 显示学生信息          |")
    print("| 3) 删除学生信息          |")
    print("| 4) 修改学生成绩          |")
    print("| q) 退出                  |")
    print("+--------------------------+")

def main():
    infos = []  # 此列表用于保存学生数据
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            delete_student(infos)
        elif s == '4':
            modify_student_score(infos)
        elif s == 'q':
            break

main()
   