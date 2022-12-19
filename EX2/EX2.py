# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input("Введите x: "))
y = bool(input("Введите y: "))
z = bool(input("Введите z: "))

firstFunc = not(x or y or z)
secondFunc = not x and not y and not z

if firstFunc == secondFunc:
    output = True
else:
    output = False

print(output)