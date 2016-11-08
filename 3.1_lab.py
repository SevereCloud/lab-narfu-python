def insertionsort (s):
        for i in range(len(s)):
                ii=i
                while (s[ii]<s[ii-1])&(ii>0):
                        t = s[ii-1]
                        s[ii-1] = s[ii]
                        s[ii] = t
                        ii -= 1

        return s


L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print(insertionsort(L))


print(quit())
