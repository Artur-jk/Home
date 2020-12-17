
def merge_list(*args):
    a = []
    for val in args:
        if(list == type(val) or type(val) == set or type(val) == tuple):
            a.extend(val)
        else:
            a.append(val)
    return a

print(merge_list([0,0], "nice", {5,4,1}, (12,9), None))


def remove_duplicates(list_of_lists):
     print([list(kek) for kek in {tuple(item) for item in list_of_lists}])

remove_duplicates([[10, 20],  [40],  [30, 56, 25], [10, 20],
[33], [40]])


def merge_list(list_to_merge):
    a = []
    for i in range(len(list_to_merge)):
        a.extend(list_to_merge[i])
    print(a)

merge_list([[1, 8, 3], [-5, 0], [4], [2, 3, 3]])


def multi_power(original, powers):
    a = list(map(lambda x, y: x**y, original, powers))
    print(a)

multi_power ((3, 2, 0, -2, -7),(1/3, 7, 10, -2, 3))
