class Vehicle: #Phương tiện giao thông
    def __init__(self, brand, color):
        self.brand = brand # thương hiệu
        self.color = color # màu
    # method drive (lái)
    def drive(self):
        print("Chiếc xe màu ", self.color, " hãng ", self.brand, " đang chạy.")

class Car(Vehicle): #Xe o tô kế thừa từ lớp Vehicle
    pass

oto = Car('Toyota', 'Black')
oto.drive()

class Bike(Vehicle): #Xe dep kế thừa từ lớp Vehicle
    pass
xedap = Bike('Thống Nhất', 'Hồng')
xedap.drive()