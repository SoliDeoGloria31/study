

def fx():
    def fy():
        print("hello")
    return fy

fn = fx()
fn()  # ???

def fa():
    L = [1, 2, 3, 4]
    return L
L2 = fa()
print(L2)

