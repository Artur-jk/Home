def f1(a, b):
    return a + b, a * b


print(f1(4, 10))


def f2(a, b):
    import math
    d = math.sqrt(a + math.sqrt(b))
    return d


print(f2(12, 50))


def f3():
    return [num for num in range(1000, 4251) if num % 5 == 0 and num % 3 != 0]


print(f3())


def f4(n):
    if n in range(3, 7):
        n -= 13
    elif n in range(8, 42):
        n -= 50
    elif n <= 0 or n > 2000:
        n * 4
    else:
        n = 0
    return n


print(f4(6))


def f5(n):
    return n * 9 / 5 + 32


print(f5(0))


def f6(sum, pr):
    return sum * (1 + 0.01 * pr) ** 5


print(f6(200000, 5))


def f7(week, month, year):
    return week * 7, month * 30, year * 365


print(f7(0, 4, 3))


def f8(num):
    abs = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            abs.append(d)
            num //= d
        else:
            d += 1
            if num > 1:
                abs.append(num)
                return abs


print(f8(40))


def f9(num):
    return [i for i in range(1, num + 1) if num % i == 0]


print(f9(36))


def f10(x1, y1, x2, y2):
    import math
    return math.sqrt(math.sqrt(y2 - y1) + math.sqrt(x2 - x1))


print(f10(0, 0, 1, 1))


def f11(num):
    return [i ** 2 for i in range(1, num)]


print(f11(50))


def f12(num):
    return sum(i for i in num[2:5 + 1])


print(f12(num=[1, 5, -1, 9, 0, 2]))
