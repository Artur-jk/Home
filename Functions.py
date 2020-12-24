from calendar import calendar

import numpy as npy


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


# def f13():
# s1 = []
# a = int(input("Размер "))
# d = int(input("Число "))
# for i in range(a):
# s1.append(d)
# return s1


# print(f13())


def f14():
    s1 = [1, 2, 4, 3, 4, 5, 4]
    for elem in s1:
        if elem == 4:
            s1.remove(elem)
    return s1


print(f14())


def f15(num):
    num = [int(x) for x in str(num)]
    max_i = num.index(max(num))
    min_i = num.index(min(num))

    num[max_i], num[min_i] = num[min_i], num[max_i]

    return num


print(f15(45321))


def f16():
    a = [64321]
    for i in range(len(a)):
        if a[i] > i:
            print("True")
        else:
            print("False")


f16()


def f17():
    ar = [9, 8, 5, 5, 8, 9]
    for i in range(len(ar) // 2):
        if ar[i] != ar[-i - 1]:
            print("False")
    else:
        print("True")


f17()


def f18(*args):
    a = 'in the hole in the ground there lived a hobbit '
    for word in a.split():
        for char in word:
            if char in args:
                a = a.replace(word, '')
    # return [w for w in a.split() if not any(c in args for c in w)]
    return a

print(f18('t', 'h', 'r'))


def f19():
    a = "12300280"
    for i in a.split('.'):
        if (0 <= int(i) < 256):
            print(True)
        else:
            print(False)


f19()


def f20(a):
    ab = ''
    for i in a:
        if i.isdigit():
            ab += i
    print(ab)


f20("ab = 2 + 278")


def f21(*args):
    a = [i for i in args if i % 2 == 0]
    print(sum(a) // len(a))
    b = [i for i in args if i % 2 != 0]
    print(sum(b) // len(b))


f21(6, 1, 2, 1)


def f22():
    a = [1, 2, 0, 0, 4, 0]
    b = []
    for i in range(len(a)):
        if a[i] != 0:
            b.append(i)
    print(b)


f22()


def f23(a):
    b = [1, 2, 8, 0, 4, 0]
    print(min(b, key=lambda x: abs(x - a)))


f23(7.5)


def f24(a):
    b = ['и', 'е','а']
    a2 = ''
    for i in a:
        a2 += i
        if (i  in b):
            a2 += 'c' + i
    print(a2)

f24('Привет, как дела ')

def f25():
    a = [1,2,-5,1,4,2]
    mx = a[0] + a[1], a[2]
    ar = 0
    for i in range(len(a)-1):
        if a[i-1]+ a[i] + a[i+1] :
            mx = a[i-1]+ a[i] + a[i+1]
            ar = i

    return a[ar-1:ar+2]
print(f25())

def f26():
    a = [1,2,0,1,1]
    for i in range(len(a)):
        n = 0
        for elem in a:
            if elem == a[i-1]:
                n+=1
                if n >= 2:
                    return True
print(f26())

def f27():
    a = [1,4,5,7,8,3,20,13,30,27,29]
    b = []

    maxa = max(a)
    print(maxa)
    ab = maxa * 0.1
    for i in a:
        if (maxa - ab)  <= i <= maxa:
            b.append(i)
    return b

print(f27())

#def f28( a, b):


def f29():
    a = [1,2,4]
    b = [1,1,4]
    a.sort()
    b.sort()
    if a == b:
        return True
    else: return  False

print(f29())


def f30():
    a = [4 ,0, 5, 0, 3, 0, 0, 5]
    counter = 0
    for i in a:
        if 0 in a:
            a.remove(0)
            counter += 1
    for i in range(counter):
        a.append(0)
    return a
print(f30())


def f31(a):
    return a[::2]

print(f31([1,2,8,8,5,10,11,0,-1]))

def f32(a):
    mx = a.index(max(a))
    a.remove(a[mx])
    mx_s = a.index(max(a))
    return [mx, mx_s]

print(f32([1,2,8,8,5,10,11,0,-1]))

def f33(a):
    return sorted(a)[-1] - sorted(a)[-2]

print(f33([0,6,1,-1,4,1,-1,0]))

def f34(a):
    if (a >= 1) & (a <= 12):
        return ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'][a - 1]
    else:
        return 'Учи названия месяцев'
print(f34(2))

def f35(a):
    if 0 < a <= 3: return 'Зима'
    elif 4 <= a <= 6 : return 'Весна'
    elif 7 <= a <= 9: return 'Лето'
    else: return 'Осень'
print(f35(2))

def f36(key, elem):
    return dict(zip(key,elem))
print(f36([1,2,3,4] ,['a', 'b', 'c', 'd']))

def f37(a):
    new = dict()
    for i, j in a.items():
        new.setdefault(j, []).append(i)
    return str(new).replace("[", "(").replace("]", ")")
print(f37({1: 'a', 2: 'a', 3: 'a', 4: 'd'}))

def f38(a):
    return dict(map(reversed, a.items()))
print(f38({1: 'a', 2: 'b', 3: 'c', 4: 'd'}))


#def f39():

def f40(n):
    n = int(input('Введите число N: '))
    dictt = {}
    var = {dictt.setdefault(i + 1, (i+ 1) ** 2) for i in range(n)}
    return dictt
print(f40(6))

def f41(n,m):
    return npy.random.randint(26, size=(n, m))
print(f41(2, 3))


def f43(arr_mat):
    return tuple(max(i) for i in arr_mat)

print(f43([[2,5,7,6],
 [8,8,13,5],
 [9,11,4,8],
 [8,6,12,5]]))