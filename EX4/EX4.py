# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти (1-4): "))

if quarter == 1:
    print("Диапазон значений: x[0; +infinity), y[0; +infinity)")
elif quarter == 2:
    print("Диапазон значений: x(-infinity; 0], y[0; +infinity)")
elif quarter == 3:
    print("Диапазон значений: x(-infinity; 0], y(-infinity; 0]")
elif quarter == 4:
    print("Диапазон значений: x[0; +infinity), y(-infinity; 0]")
else:
    print("Ошибка")
