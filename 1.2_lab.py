s = 0
while s==0:
    n = input("Кол-во чисел ")
    max = 0

    for i in range(n):
        a = input("Число ")
        if a > max:
            max = a

    print("max: " + str(max))    

print(quit())
