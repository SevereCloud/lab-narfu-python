import random

def insertionsort (s):
        for i in range(len(s)):
                ii=i
                while (s[ii]<s[ii-1])&(ii>0):
                        t = s[ii-1]
                        s[ii-1] = s[ii]
                        s[ii] = t
                        ii -= 1

        return s

def mergesort (s):
    if len(s)>1:
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]

        mergesort(left)
        mergesort(right)

        i=0 #номер в левом
        j=0 #номер в правом
        k=0 #номер элемента в масиве
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                s[k]=left[i]
                i=i+1
            else:
                s[k]=right[j]
                j=j+1
            k=k+1

        while i<len(left):
            s[k]=left[i]
            i=i+1
            k=k+1

        while j<len(right):
            s[k]=right[j]
            j=j+1
            k=k+1
	
    return s

def rand (n):
    arr = []

    for i in range(0, n): arr.append(random.randint(0, 1000))
    	
    return arr


s = 0
while s==0:
    L = rand(input("Кол-во элементов "))

    print("Список "+str(L))

    print("merge",mergesort(L))
    print("insertion",insertionsort(L))

    assert insertionsort(L) == mergesort(L)
