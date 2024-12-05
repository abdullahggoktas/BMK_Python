# for => list
# while => koşullu

sayilar = [1,2,3,4,6,8,91,21]
isimler = ["Ali","Ahmet","Zeynep"]
adsoyad = "Ali Yılmaz"

# for x in sayilar:
#     print(x)
    
# for x in sayilar:
#     print("Merhaba BMK")

# for isim in isimler:
#     print(isim)   

# for i in adsoyad:
#     print(i)


my_dict = {"41":"Kocaeli","53":"Rize","35":"İzmir"}

# for x in my_dict:
#     print(my_dict[x])

for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)

for x,y in my_dict.items():
    print(x,y)