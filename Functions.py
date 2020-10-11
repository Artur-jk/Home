def f1(a, b):
    d = (a + b, a * b)
    return tuple(d)
print(f1(4, 10))

def f2(a, b):
    import math
    d = math.sqrt(a + math.sqrt(b))
    return d
print(f2(12, 50))

def f3():
    return [num for num in range(1000, 4250) if num%5 == 0 and num%3 !=0]
print(f3())

