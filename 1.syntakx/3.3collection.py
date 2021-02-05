# *** Список (list) ***

# Cоздание пустого списка 
my_list = []
my_list_2 = list()

# добавление объекта (в конце списка)
my_list.append(100)
my_list.append(77)
my_list.append("A")
my_list.append([1,2,3])

# обращение к элементам списка
# замена значения н
my_list[0] = 5
my_list[-2] = 'B'

# чтение значений 
element_value = my_list[1]

#  удаление значений

# del my_list[-1]

# my_list.remove(5)

# a = my_list.pop(0)

# создание заполненого листа

my_list_2 = [10, 20, 30, 'A', 'hello', True, 3.14, [1,2,3]]

# "длинна" спсика - колличество элементов

# print(len(my_list_2))


# создание списка из строки

s = "Hello, world!"
listFromStr = list(s)

# print(listFromStr)


# методы списка 

x = [1,2,3,4,5,6]

y = x 

# y[2] = 100

z = x.copy()

z[2] = 100

print(f"x: {x}; z: {z}")