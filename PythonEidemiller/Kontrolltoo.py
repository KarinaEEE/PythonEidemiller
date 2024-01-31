#Karina ja Erik LogITgv23
#1
# n = int(input("Введите число елок (от 1 до 9): "))


# if 1 <= n <= 9:
#     for _ in range(n):
#         print("     /V\ ","\n","   / V \ ","\n","  / V V \ ","\n"," /VV V VV\ ","\n", end="")
        
#     print()
# else:
#     print("Пожалуйста, введите число от 1 до 9.")




# #2
# R = int(input("Введите число R: "))
# n = 1
# for i in range(1, R + 1, 2):
#     n *= i
# print(f"Произведение всех не чётных чисел в диапазоне от 0 до {R} равно: {n}")

#3 
# import random
# n=random.randint(1, 10)
# positive_count = 0
# for _ in range(n):
#     num=random.randint(-10, 10)
#     if num > 0:
#         positive_count += 1
# print(f"Сгенерировано {n} чисел.")
# print(f"Количество положительных чисел: {positive_count}")

#4
# num=int(input("Введите натуральное число: "))
# even_count=0
# odd_count=0
# while num>0:
#     digit=num%10    
#     if digit%2==0:
#         even_count+=1    
#     else:
#         odd_count+=1   
#     num//=10
# print(f"Четные цифры: {even_count}")
# print(f"Нечетные цифры: {odd_count}")


#5 

# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))

# summa = 0

# for i in range(A, B + 1):
#     summa += i

# print(f"Сумма ряда чисел от {A} до {B} равна: {summa}")





