class Xe:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def getColor(self):
        print(self.color) 
        
    def update_brand(self, brand):
        self.brand = brand
    
# Xe oto
class Car(Xe): # Lớp car, kế thừa từ lớp Xe
    def info(self):
        print(self.brand, self.color)
        
 # Xe Đạp      
class Bike(Xe):
    def info(self):
        print(self.brand, self.color)


xeTaxi = Car('Toyota', 'Black')
xeTaxi.info()
# kế thừa phương thức từ lớp cha (lớp Xe)
xeTaxi.getColor()