# function_as_args2.py

def goodbye(L):
    for x in L:
        print("再见:", x)

def operator(fn, L):
    fn(L)

operator(goodbye, ['Tom', 'Jerry', 'Spike'])