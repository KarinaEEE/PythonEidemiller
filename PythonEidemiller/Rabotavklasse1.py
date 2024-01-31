from datetime import*
from random import*

# arve_nr=date.today()#datetime.now()
# tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
# summa=0

# tooded=["Piim","Leib","Kommid"]
# hinnad=[randint(120,150)/100,randint(100,150)/100,randint(50,1500)/100]
# for i in range(3):
#     toode=tooded[i]
#     hind=randint(50,150)/100
#     v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
#     if v=="jah":
#         mitu=int(input("Mitu?"))
#         tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#         summa+=mitu*hind
        
# tsekk+="Kokku maksta: "+str(summa)
# print(tsekk)

#1
# nimi=input("Mis on sinu nimi?")
# arv=int(input("Mitu korda soovid tervitatud saada? "))
# for kord in range(1, arv+1):
#     print(f"Ole tervitatud, {nimi},{kord}. korda.") ## f-означает формат
    

#2


# summa=0
# for i in range(10):
#     arv=int(input("Sisesta arv: "))
#     summa+=arv
# print(summa)

#2.1
# summa=0
# i=0
# while True:
#     i+=1
#     arv=int(input("Sisesta arv: "))
#     if i>10: break
#     if arv==777: break
#     summa+=arv
# print(summa)

#2.2
# summa=0
# i=0
# while True:
#     i+=1
#     arv=int(input("Sisesta arv: "))
#     if i>10: break
#     try:
#         arv=int(arv)
#         summa+=arv
#     except:
#         break
# if summa!=0:
#     print(summa)

#3
# k=0
# while True:
#     k+=1
#     print(f"{k}. ülesanne")
#     a=randint(1,50)
#     b=randint(1,50)
#     p=5
#     while True:
#          v=int(input(f"{a}+{b}= "))
#          p-=1
#          if v==a+b:
#              print("Õige vastus!")
#              break
#          elif p==0:
#              print(f"{a}+{b}={a+b}")
#              break
#     if k==2:
#         break
         

#4

# for i in range(1,11):
#     print(i)
# print()

# for i in range(1,11):
#     for k in range(1,11):
#         print(f"{i}*{k}={i*k}")
#     print()
        

#5

# n=int(input("Sisesta arv n:"))
# for i in range(n):
#     for k in range(n):
#         if i==k or i+k == n-1:
#             print("x", end=" ")
#         else:
#             print("0", end=" ")
#     print()


# #31.01
# print("*** ИГРЫ С ЧИСЛАМИ ***")
# print()
# # перед абс убранна скобка и добавлена в конец       
# while 1:
#     try:
#         a = abs(int(input("Введите целое число => ")))
#         break
#     except ValueError:
#         print("Это не целое число") 
         
# if a == 0:
#     print("Нет смысла ничего делать с нулём")
# else:
#     print("Определяем, сколько в числе чётных и сколько нечётных цифр")
#     print()
#     c=a
#     b=a
#     paaris = 0
#     paaritu = 0
#     while b > 0:
#         if b % 2 == 0:
#                 paaris += 1
#         else:
#                 paaritu += 1
#         b = b // 10
    
#     print("Чётных цифр: "+str(paaris))
#     print("Нечётных цифр: "+str(paaritu))
#     print()
    
#     print("*Переворачиваем* введённое число")
#     print()
#     b=0
#     while a > 0:
#         number = a % 10
#         a = a // 10
#         b = b * 10
#         b += number
#     print("*Перевёрнутое* число", b)
#     print()
#     print("Проверяем гипотезу Сиракуз")
#     print()
#     if c % 2 == 0:
#         print(f"{c} - чётное число. Делим на 2.")
#     else:
#         print(f"{c} - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
#     while c != 1:    
#         if c % 2 == 0:
#             c = c / 2
#         else:
#             c = (3*c + 1) / 2
#         print(c, end="\t")
#     print()
#     print("Гипотеза верна")
   
    