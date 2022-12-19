# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве

firstPointX = int(input("Введите координату x первой точки:"))
firstPointY = int(input("Введите координату y первой точки:"))
secondPointX = int(input("Введите координату x второй точки:"))
secondPointY = int(input("Введите координату y второй точки:"))

distance = ((secondPointX - firstPointX)**2 + (secondPointY - firstPointY)**2)**(1/2)
print(f"Расстояние между точками = {distance}")