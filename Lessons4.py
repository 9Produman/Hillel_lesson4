tuple_a = (1, 2, 3, 4, 5)
tuple_b = (4, 5, 6, 7, 8)
tuple_c = (4, 5, 6, 7, 8, 9, 10, 11)

tuple_d = tuple_a + tuple_b + tuple_c




list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_f = [9, 3, 4, 1, 8, 6, 5, 2, 0, 7]


list_c = list_a + list_b # Задача 1


list_c = [x for y in zip(list_a, list_b) for x in y] # Задача 2


list_с_a = [x for x in list_a if not x % 2] # Задача 3
list_с_b = [x for x in list_b if x % 2]
print(list_с_b)

res = map(sum, zip(a,b))


list_c.reverse()
print(list_c)