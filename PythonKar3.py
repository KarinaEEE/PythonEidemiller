


# from random import *

#a=randint(-100,100)
#if a%2==0:
#    print(a,"-paaris arv")
#if a>0:
#    print(a,"suurem kui 0")
#else:
#    print(a,"väiksem kui 0 või võrdne 0-ga")

##<,>100 ei soobi,0-59-"2",60-75-"3",76-90-"4"91-100-"5"
#if a<0 or a>100:
#    print("Viga!")
#elif a>=0 and a<60:
#    print("Hinne 2")
#elif a>=60 and a<75:
#    print("Hinne 3")
#elif a>=76 and a<91:
#    print("Hinne 4")
#else:    #a>=91 and a<100: тоже самое
#    print("Hinne 5")

#nimi=input("Mis on sinu nimi?") #upper()-"JUKU, lover()-"juku",capitalize()-"Juku"
#if nimi=="Juku":
#    print("Lähme kinno")
#    vanus=int(input("Kui vana sa oled?"))
#    if vanus<0 or vanus>100:
#        vastus="Aju"
#    elif vanus<6:
#        vastus="Tasuta pilet"
#    elif vanus<14:
#        vastus="Lastepilet"
#    elif vanus<65:
#        vastus="Täispilet"
#    elif vanus<=100:
#        vastus="Sooduspilet"
#    print("On vaja Jukule osta",vastus)

#else:
#    print("Minge koju!")


#nimi1=input("Kes minu pinginaaber?:") # ise proovinud
#if nimi=="Erik":

#nimi2=input("Kes minu pinginaaber?:")
#if nimi=="Karina":

#print(f"Täna on {nimi1} ja {nimi2} pinginaabrid!")

#n1=input("Esimene nimi")
#n2=input("Teine nimi")
#if n1.capitalize()=="Mark" and n2.capitalize()=="Erik" or n1.capitalize()=="Erik" and n2.capitalize()=="Mark":
#    print("Pingenaabrid")
#else:
#    print("Nad ei ole naabrid")
#if n1.capitalize() in ["Mark","Erik"] and n2.capitalize() in ["Mark","Erik"]:
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")



#pikkus = float(input("Põranda pikkus: "))
#laius = float(input("Põranda laius: "))
#pindala = pikkus * laius
#print("Toa põranda pindala on:",pindala)
#soov_remondi = input("Kas soovid teha remonti? (jah/ei): ").lower()
#if soov_remondi == "jah":
    
#    hind = float(input("Kui palju maksab ruutmeeter? "))
    
    
#    summa = pindala * hind
#    print("Põranda vahetamise hind on",summa)
#else:
#    print("Aitäh. Head päeva!")

#alghind=input("Kirjuta alghind:")  # ise proovinud
# Alghind>700:
#     protsent=30
#     summa= (protsent / 100) * alghind
#print("30% soodustuse hind on",summa)
#else:
#    print("Alghind peab olema suurem kui 700 eurot")

# alghind=randint(0,100000)/100
# if alghind>700:
#     #soodustus=alhgind*0.3
#     #alghind-=soodustus
#     alghind*=0.7
# print("Uus hind on ",alghind)

#17.01 v klasse


try:
    pikkus=int(input("Pikkus: ")) 
except:
    print("On vaja int formaat kasutada!")
    