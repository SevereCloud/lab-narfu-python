# Поиск наибольшего числа

# Зацикливаем программу
s = 0
while s == 0:
    #Спрашиваем кол-во чисел
    n = input("quantity: ")
    max = 0

    #Запрашиваем числа n раз
    for i in range(n):
        a = input("number: ")
        if a > max:
            max = a

    print("max: " + str(max))

print(quit())
