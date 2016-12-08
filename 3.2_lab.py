
#Сортировка слиянием
def mergesort(array):
    """Сортировка листа  слиянием"""
    print("Splitting ", array)
    if len(array) > 1:
        mid = int(len(array)/2)
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging ", array)
    return array


L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print(mergesort(L))

input()
