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

# исходный список
x = [1,2,3,4,5,6]

# представления 
y = x 

# y[2] = 100

#  копия 
z = x.copy()

z[2] = 100

#print("3f"x: {x}; z: {z}")
 
# срезы списка

my_list = [10, 20, 30, 40, 50,  60, 70]

# прямой срез 

slice_f = my_list[1:4] # с 1 индекса до 4-го не включительно

slice_f = my_list[2:] # со второго индекса до конца списка 

slice_f = my_list[::2] # с самого начала до конца списка с шагом = 2

slice_f = my_list[1:6:2] # с 1 индекса до 6 не включительно с шагом 2 

# обратный срез 

slice_b = my_list[-1::-1] # с -1 индекса до конца с шагом = -1 (в обратном направлене)

slice_b = my_list[-3:-6:-1]

# print(slice_b)



# *** Кортеж (tuple) ***

# неизменяемая коллекция (immutable коллекция)
my_tuple = (10, 20, 30)

# чтение данных
el = my_tuple [-1]

# можно делать срез кортежи
el = my_tuple [-1: -3: -1]

# нельзя удалять знаение 
# del my_tuple[0]

# нельзя менять значения 
# my_tuple[1] = 100

# нельзя добавлять элемент
# my_tuple.

# print(el)



# *** Словарь (ditctionary) ***

# создание словаря 
# {ключ:значенe} {пара "ключ-значение"}
my_dict = {1:100, 2:200, 3:777}
my_dict_2 = {"a":10, "b":"hello", "c":[1,2,3], 10:1000}

# чтение данных 
item = my_dict_2[10]
item = my_dict_2["a"]

# пример применения словаря в качестве альтерантивы условным оператором 
condition = "key_1"
d = {"key_1":100, "key_2":200}

# изменение значения 
my_dict_2["b"] = "python"

# удаление элемента 
del my_dict_2[10]

# Добавление элементов
my_dict_2["newKey"] = 777

# пролема со чтением значением
# val = my_dict_2['key_2']

# решение этой проблемы
#val = my_dict_2.get('newKey')
val = my_dict_2.get('key_2', 0)

# print(val)

# Обновление данных

d_1 = {"a":10, "b":20, "c":30, "d":40}

u_d_1 = {"b":200, "d":1000}
u_d_2 = {"b":777, "e":888}

#d_1.update(u_d_1)
d_1.update(u_d_2)

print(d_1)



















































































































































