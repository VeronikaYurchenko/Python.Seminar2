#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры/

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print("Количество элементов: ", get_numbers(numbers))

x = int(input("Введите позицию первого элемента: "))
y = int(input("Введите позицию второго элемента: "))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)