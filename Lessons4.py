tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)


#1
tuple_d = tuple_a + tuple_b + tuple_c


#2
res = []
for item in tuple_d:
    count = tuple_d.count(item)
    if count < 2:
        continue
    res.append((item, count))

print(tuple(res))


#3
res = []
elements = []
for element in tuple_d:
    count = tuple_d.count(element)
    if count < 2 and element in elements:
        continue
    elements.append(element)
    indexes = []
    for index, item in enumerate(tuple_d):
        if item == element:
            indexes.append(index)
    res.append((element, tuple(indexes)))

print(tuple(res))



list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]

# Задача 1
list_c = list_a + list_b


# Задача 2
list_c = [x for y in zip(list_a, list_b) for x in y]
print(list_c)


# Задача 3
list_с_a = [x for x in list_a if not x % 2]
list_с_b = [x for x in list_b if x % 2]


# Задача 4
list_d = list_c[::-1]
print(list_d)


# Задача 5
res = [x+y for x, y in zip(list_c, list_d)]
print(res)


# Задача 6
res1 = sorted(list_f)
res2 = sorted(list_f,key=None,reverse=True)
print(res1)
print(res2)


# Задача 7
temp_res = []
for index, item in enumerate(list_c):
    count = list_c.count(item)
    if count > 1 and list_c.index(item) == index:
        test2 = ()
        for index1, item1 in enumerate(list_d, 0):
            if item1 == item:
                test2 = test2 + (index, )
        temp_res = temp_res + (item, test2)
print('Tuple_Task #3_1\n', 'res=', temp_res)


