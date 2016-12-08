
"""
Поиск числа фибаначи
"""

# Зацикливаем программу
while True:
    N = int(input('number: '))
    F = 0
    F1 = 0
    F2 = 1
    for i in range(N):
        F = F1 + F2
        F2 = F1
        F1 = F
    print(F)
