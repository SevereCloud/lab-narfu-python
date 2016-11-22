#Сортировка слиянием
def mergesort(s):
    print("Splitting ",s)
    if len(s)>1:
        mid = len(s)/2
        lefthalf = s[:mid]
        righthalf = s[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                s[k]=lefthalf[i]
                i=i+1
            else:
                s[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            s[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            s[k]=righthalf[j]
            j=j+1
            k=k+1
	
    print("Merging ",s)
    return s


L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print(mergesort(L))

input()
