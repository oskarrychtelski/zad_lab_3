#zad1
# A=[1-x for x in range(1,11)]
# print(A)
# B=[4**i for i in range(8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

#zad2
# lista1=[12,231,6,5678,231,123,78,123,12,1]
# liczby=[x for x in lista1 if x%2==0]
# print(liczby)

#zad3
# slownik={"baklazan":"szt.", "pomidor":"kg.", "ziemniaki":"kg.", "cebula":"kg.", "czekolada":"szt."}
# lista=[zakup for zakup, jednostka in slownik.items() if jednostka=="szt."]
# print(lista)

#zad4
# def trojkat(a,b,c):
#     if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         return "jest to trojkat prostokatny"
#     else:
#         return "nie jest to trojkat prostokatny"
#
# print(trojkat(3,4,5))

#zad5
# def trapez(a=0,b=0,wysokosc=0):
#     return ((a+b)*wysokosc)/2
# print (trapez(1,2,3))

#zad.6
# def ciag(a1=1,b=4,ile=10):
#     suma=1
#     for x in range(a1,a1+ile-1):
#         suma*=x*b
#     print(suma)
#zad.7
# def ciag(* liczba, b=1):
#     suma=1
#     for x in liczba:
#         suma*=x*b
#     print(suma)

#zad.8
# def zakupy(** cena):
#     suma = 0
#     ilosc = 0
#     for produkt in cena:
#         ilosc+=1
#         suma+=cena[produkt]
#     print("liczba produktow to: ", ilosc)
#     print("Zsumowana cena produktow wynosi: ", suma)
# zakupy(czekolada=5.5, chlebek=3.9, mango=7)
