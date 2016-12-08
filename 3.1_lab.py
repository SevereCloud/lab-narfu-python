# Сортировка вставками

def insertionsort (array):
    for i in range(len(array)):
        m = i
        while (array[m] < array[m-1]) & (m > 0):
            tmp = array[m-1]
            array[m-1] = array[m]
            array[m] = tmp
            m -= 1
    return array


L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print(insertionsort(L))


print(quit())
