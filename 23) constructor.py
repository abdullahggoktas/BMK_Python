# Class
class Product:
    # method
    # attribute, property 
    def __init__(self, name, price, isActive): #constructor
        self.name = name
        self.price = price
        self.isActive = isActive

# Instance
p1 = Product("iPhone 15", 50000, True)
p2 = Product("iPhone 15 Pro", 60000, True)
p3 = Product("Samsung S24", 70000, True)

urunler = [p1, p2, p3]

for urun in urunler:
    if urun.isActive:
        print(f"ürün adı: {urun.name} ürün fiyat: {urun.price}")