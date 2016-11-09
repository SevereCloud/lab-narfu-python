# Нахождение НОД

# Зацикливаем программу
s = 0
while s == 0:
    a = input("1 number ")
    b = input("2 number ")

    q = 1

    while q != 0:
        q = a % b
        a = b
        b = q

    print(a)
