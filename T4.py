import math

def function1(arg, summ, absolut, root):
    if sum and not absolut and not root:
        return sum(arg)

    elif absolut and not summ and not root:
        return [abs(i) for i in arg]

    elif root and not summ and not absolut:
        return [math.sqrt(i) for i in arg]

    elif summ and root and not absolut:
        return sum(math.sqrt(i) for i in arg)

    elif summ and root and absolut:
        return sum(math.sqrt(abs(i)) for i in arg)

    else:
        return arg


print(function1([1, -4, 9], True, True, True))