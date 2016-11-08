#Делим числа на части
#1 a*c
#2 b*d
#3 (a+b)
#4 3-2-1
#5 сложение 1 4 и 2

def multipli(x,y):
        if len(str(x)) == 1 or len(str(y)) == 1:
                return x*y
        else:
                n = max(len(str(x)),len(str(y)))
                nby2 = n / 2
                
                #Разделяем число на части
                a = x / 10**(nby2)
                b = x % 10**(nby2)
                c = y / 10**(nby2)
                d = y % 10**(nby2)
                #print(a,b,c,d)
                
                ac = multipli(a,c) #Первая часть
                bd = multipli(b,d) #Вторая часть
                ad_bc = multipli(a+b,c+d) - bd - ac #3 и 4 часть
                print(ac,bd,ad_bc)

                result = ac * 10**(2*nby2) + (ad_bc * 10**nby2) + bd #5 шаг

                return result


s = 0
while s==0:
        s1=int(input("Введите первое число \n"))
        s2=int(input("Введите второе число \n"))
        print(multipli(s1,s2))


print(quit())
