
#print(" @..@")
#print("(----)")
#print("(\\__/)")
#print("^^\"\"^^")

#import math



#N = float(input("Введите длину участка (в метрах): "))
#M = float(input("Введите ширину участка (в метрах): "))

#diagonal_length = math.sqrt(N**2 + M**2)


#print(f"Длина диагонали участка: {diagonal_length} метров")


# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# number1 = int(input("Sisesta esimene täisarv: "))
# number2 = int(input("Sisesta teine täisarv: "))
# number3 = int(input("Sisesta kolmas täisarv: "))
# number4 = int(input("Sisesta neljas täisarv: "))
# number5 = int(input("Sisesta viies täisarv: "))

# keskmine = (number1 + number2 + number3 + number4 + number5) / 5

# print(f"Aritmeetiline keskmine on: {keskmine}")

# a = int(input("Sisesta esimese külje pikkus: "))
# b = int(input("Sisesta teise külje pikkus: "))
# c = int(input("Sisesta kolmanda külje pikkus: "))

# ümbermõõt = a + b + c

# print(f"Kolmnurga ümbermõõt on: {ümbermõõt}")



# pizza_hind = 12.90
# jaotrah_protsent = 10
# jaotrah_summa = (jaotrah_protsent / 100) * pizza_hind
# kokku_summa = pizza_hind + jaotrah_summa
# inimeste_arv = 2
# igauks_maksmise_summa = kokku_summa / inimeste_arv
# print(f"Igaüks peab maksma: {igauks_maksmise_summa:.2f}€")

#домашнее задание 16.01


#6

# pikkus = float(input("Sisesta oma pikkus meetrites: "))

# # Määra piirid lühikese, keskmise ja pika jaoks (need võivad olla kohandatavad)
# lühike_piir = 1.60
# pikk_piir = 1.80

# # Tee otsus pikkuse põhjal
# if pikkus < lühike_piir:
#     print("Sa oled lühike.")
# elif lühike_piir <= pikkus <= pikk_piir:
#     print("Sa oled keskmise pikkusega.")
# else:
#     print("Sa oled pikk.")

#7

# pikkus = float(input("Введите свой рост в метрах: "))
# sugu = input("Введите свой пол (м/ж): ")

# # Определить границы для низкого, среднего и высокого роста
# lühike_piir = 1.60
# keskmine_piir_mehed = 1.70
# pikk_piir = 1.80

# # Принять решение на основе роста и пола
# if sugu == "м":
#     print("Низкий") if pikkus < lühike_piir else print("Среднего роста") if lühike_piir <= pikkus <= keskmine_piir_mehed else print("Высокий")
# elif sugu == "ж":
#     print("Низкая") if pikkus < lühike_piir else print("Среднего роста") if lühike_piir <= pikkus <= pikk_piir else print("Высокая")
# else:
#     print("Неверно указан пол, введите 'м' или 'ж

#8

# import random

# tooted = ["piim", "sai", "leib", "jogurt", "juust"]
# hinnad = {"piim": 1.20, "sai": 2.50, "leib": 1.80, "jogurt": 0.90, "juust": 3.50}

# kogusumma = 0

# for toode in tooted:
#     kogus = int(input(f"Mitu tükki {toode} soovite osta? "))
#     summa_toode = kogus * hinnad[toode]
#     kogusumma += summa_toode
#     if kogus > 0:
#         print(f"{toode}: {kogus} tk x {hinnad[toode]:.2f}€ = {summa_toode:.2f}€")

# print(f"\nKogusumma: {kogusumma:.2f}€")

#9

# # Пользователь вводит длины сторон квадрата
# сторона = float(input("Введите длину стороны квадрата: "))

# # Определить, может ли это быть квадратом
# if сторона > 0:
#     print("Это квадрат.")
# else:
#     print("Это не может быть квадратом, потому что длина стороны должна быть положительным числом.")

#10

# # Пользователь вводит два числа
# ч1 = float(input("Введите первое число: "))
# ч2 = float(input("Введите второе число: "))

# # Пользователь выбирает знак операции
# операция = input("Выберите операцию (+, -, *, /): ")

# # Выполняется выбор операции в зависимости от ввода пользователя
# if операция == "+":
#     результат = ч1 + ч2
# elif операция == "-":
#     результат = ч1 - ч2
# elif операция == "*":
#     результат = ч1 * ч2
# elif операция == "/":
#     # Проверяем, что второе число не равно нулю
#     if ч2 != 0:
#         результат = ч1 / ч2
#     else:
#         print("На ноль делить нельзя.")
#         результат = None  # Помечаем, что результата нет

# # Выводим результат, если он существует
# if результат is not None:
#     print(f"Результат: {результат}")

#11

# # Kasutaja sisestab sünnipäeva
# sunnipaev = input("Sisesta oma sünnipäev (näidis: 01-01-2001): ")

# # Eralda aasta osa sünnipäevast
# aasta = int(sunnipaev.split("-")[0])

# # Kontrolli, kas aasta on juubel
# if (aasta % 5 == 0) and (aasta % 100 != 0 or aasta % 400 == 0):
#     print("Palju õnne, see on juubeliaasta!")
# else:
#     print("See ei ole juubeliaasta.")

#12

# # Kasutaja sisestab toote hinna
# toote_hind = float(input("Sisesta toote hind (€): "))

# # Määra allahindluse määr vastavalt hinna vahemikule
# if toote_hind <= 10:
#     allahindlus_protsent = 10
# else:
#     allahindlus_protsent = 20

# # Arvuta allahindluse summa ja lõplik hind
# allahindlus_summa = (allahindlus_protsent / 100) * toote_hind
# loplik_hind = toote_hind - allahindlus_summa

# # Kuva lõplik hind
# print(f"Toote lõplik hind on: {loplik_hind:.2f}€")

#13

# # Запросить пол кандидата
# пол = input("Введите ваш пол (м/ж): ")

# # Если кандидат - мужчина
# if пол.lower() == 'м':
#     # Запросить возраст кандидата
#     возраст = int(input("Введите свой возраст: "))

#     # Проверить, находится ли возраст в диапазоне 16-18
#     if 16 <= возраст <= 18:
#         print("Вы подходите для участия в команде.")
#     else:
#         print("Ваш возраст не подходит для участия в команде.")
# else:
#     print("Команда только для мужчин.")

#14

# # Запросить количество людей и вместительность автобуса
# количество_людей = int(input("Введите количество людей: "))
# вместительность_автобуса = int(input("Введите вместительность автобуса (количество мест в автобусе): "))

# # Рассчитать количество автобусов и количество людей в последнем автобусе
# количество_автобусов = количество_людей // вместительность_автобуса
# людей_в_последнем_автобусе = количество_людей % вместительность_автобуса

# # При необходимости добавить один автобус, если в последнем автобусе остались люди
# if людей_в_последнем_автобусе > 0:
#     количество_автобусов += 1

# # Вывести результат
# print(f"Необходимое количество автобусов: {количество_автобусов}")
# print(f"Людей в последнем автобусе: {людей_в_последнем_автобусе}")

# while True:
#     try:
#         pikkus=int(input("Pikkus: "))
#         laius=int(input("Laius: "))
#         if pikkus>0 and Laius>0:
#             print("Pindala:",pikkus*laius)
#             print("Pikkus ja laius on sisetanud ja pindala on leitud")
#         else:
#             print("On vaja andmed suurem kui 0")
#         break
#     except:
#         print("On vaja int formaat kasutada!")
        
# print("Töö lõpp")
       

# 10 практических заданий по теме Циклы

#1

# mitu=0
# for k in range(1,16):
#     n=float(input("Sisesta"+str(k),". arv "))
#     if int(n)==float(n):
#         mitu+=1
# print("Täisarvude kogus: ", mitu)


#2

# # Запрос числа 
# A = int(input("Введите число A: "))


# сумма = 0


# i = 1
# while i <= A:
#     сумма += i
#     i += 1


# print(f"Сумма всех натуральных чисел от 1 до {A} равна {сумма}")

# A = int(input("Sisestage arv A: "))
# summa = 0
# i = 1
# while i <= A:
#     summa += i
#     i += 1
# print(f"Kõigi looduslike arvude summa vahemikus 1 kuni {A} on {summa}")

 #3

# произведение = 1
# for _ in range(8):
#     число = float(input("Введите число: "))
#     if число > 0:
#         произведение *= число
# print(f"Произведение положительных чисел равно {произведение}")


# произведение = 1
# количество_введенных_чисел = 0

# while количество_введенных_чисел < 8:
#     число = float(input("Введите число: "))
#     if число > 0:
#         произведение *= число
#         количество_введенных_чисел += 1

# print(f"Произведение положительных чисел равно {произведение}")

#4

# for число in range(10, 21):
#     print(число ** 2)

# число = 10
# while число <= 20:
#     print(число ** 2)
#     число += 1



#16

# suurus=9

# for i in range(1, suurus+1):
#     for k in range(1, suurus+1):
#         print(i if i == k else 0, end=" ")
        
#     print()
        

# suurus=9

# i=1

# while i<= suurus:
#     k = 1
#     while k<= suurus:
#         print( i if i == k else 0, end=" ")
#         k +=1
#         i +=1
#     print()








