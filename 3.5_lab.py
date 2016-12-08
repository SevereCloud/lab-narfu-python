
#Тестирование 
import random
import time


def mergesort(s):
    if len(s) > 1:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i = i + 1
            else:
                s[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            s[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            s[k] = right[j]
            j = j + 1
            k = k + 1

    return s


def insertionsort(s):
    for i in range(len(s)):
        ii = i
        while (s[ii] < s[ii - 1]) & (ii > 0):
            t = s[ii - 1]
            s[ii - 1] = s[ii]
            s[ii] = t
            ii -= 1

    return s


for n in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 100))

    t1 = time.clock()
    insertionsort(arr)
    t2 = time.clock()
    it = (t2 - t1) * 1000

    t1 = time.clock()
    mergesort(arr)
    t2 = time.clock()
    mt = (t2 - t1) * 1000

    print("{0:7}:".format(n) + "{0:10.1f}".format(it) + "{0:10.1f}".format(mt))
