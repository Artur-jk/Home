def pow():
    a = int(input())
    b = int(input())
    while(a + b == 0):
        a1 = a
        b1 = b
    return a**2 + b**2

#print(pow())


def calc():
    a = int(input())
    b = int(input())
    op = input()
    if op == '+':
        return  a + b
    elif op == '-':
        return a -b
    elif op == '/':
        return a/b
    elif op == '*':
        return a * b
    elif op == 'mod':
        return a % b
    elif op == 'pow':
        return a ** b
    elif op == 'div':
        return a // b

#print(calc())

def search():
    c = int(input())
    for i in range(c):
        words = input()
    
print(search())



