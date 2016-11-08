import random

def mergesort (s):
    if len(s)>1:
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0
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

def insertionsort (s):
        for i in range(len(s)):
                ii=i
                while (s[ii]<s[ii-1])&(ii>0):
                        t = s[ii-1]
                        s[ii-1] = s[ii]
                        s[ii] = t
                        ii -= 1

        return s

def rand (n):
    arr = []
    for i in range(0, n): arr.append(random.randint(0, 100))
    	
    return arr





if __name__ == '__main__':
    import timeit
    for i in [10,1000,2000,3000,4000,5000,10000]:
        print "{0:7}".format(i)+":" + "{0:10.1f}".format((timeit.timeit("insertionsort(rand(i))", setup = "from __main__ import insertionsort; from __main__ import rand; i = "+str(i),number = 1)) * 1000) + "{0:10.1f}".format((timeit.timeit("mergesort(rand(i))", setup = "from __main__ import mergesort; from __main__ import rand; i = "+str(i),number = 1)) * 1000)
        #print str(i) + ": " + str(round((timeit.timeit("insertionsort(rand(i))", setup = "from __main__ import insertionsort; from __main__ import rand; i = "+str(i),number = 1)) * 1000, 1)) +" "+ str(round((timeit.timeit("mergesort(rand(i))", setup = "from __main__ import mergesort; from __main__ import rand; i = "+str(i),number = 1)) * 1000, 1))
   
