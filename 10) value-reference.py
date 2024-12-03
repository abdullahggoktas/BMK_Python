# value types=değer tipleri
# x = 10
# y = 20
# x = y #x=20
# y = 30
# print(x, y)

# reference

a = ["elma","armut"]
b = ["portakal","mandalina"]

#a = ["portakal","mandalina"]

a = b   # adres kopyaladınız.

a[0] = "üzüm"
# print(a, b)

# liste koplayama
listeA = [10,20]
listeB = listeA.copy()    # 1.yöntem #listeB=[10,20]


listeB[0] = 30

print(listeA,listeB)
