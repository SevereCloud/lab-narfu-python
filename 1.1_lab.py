s=0
while s==0:
    n = input('Число фиб: ')
    f = 0
    f1 = 0 
    f2 = 1 

    for i in range(n): 
        f = f1+f2 
        f2 = f1 
        f1 = f 

    print (f)

print(quit())
