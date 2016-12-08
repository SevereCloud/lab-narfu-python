
# Поиск наибольшего числа

# Зацикливаем программу
while True:
    #Спрашиваем кол-во чисел
    N = input("quantity: ")
    MAX = 0
    #Запрашиваем числа n раз
    for i in range(N):
        a = input("number: ")
        if a > MAX:
            MAX = a

    print("max: " + str(MAX))

print(quit())
