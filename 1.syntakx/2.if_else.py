# *** логические операторы НЕ (NOT), И (END), ИЛИ (OR)

x = True 
y = False

# оператор НЕ 
# print(not x)

# оператор И - возвращает True только если значение 
# обеих переменных равны True 

res = x and y

# res = False and False


# операатор ИЛИ  - возвращает False только если значени обеих 
# переменных  равны  False 

res = False or False 

# print(res)


# *** условные операторы ***

    #if False: 
     #   c = "hello!"
      #  print(c)

# a = -1

# if a > 0:
#     print("больше 0")
# elif a == 0:
#     print("равно 0")    
# else:
#     print("меньше 0")

b = "В"

if b == "А":
    c = "равно А"
elif b == "Б":
    c = "равно Б"
elif b == "В":
    c = "равно В"
else: 
    c = "это я не знаю"

# print(c)

# *** условная задача "термостат"

# текущая температруа 
cur_temp = 11 
# целвая значения температура (установленная через ручку регулятора)
tur_temp_1 = 27
tur_temp_2 = 10
# дополнительное условие - "зависимость от присутствия людей"
z = False

# логика теромстат 
if z == True and cur_temp < tur_temp_1:
    print(f"Включено нагрева{tur_temp_1}")
elif z == False and cur_temp < tur_temp_2:
    print(f"Включено нагрева{tur_temp_2}")    
else: 
    print("Нагревание выключено")
