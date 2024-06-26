class Car:
    def __init__(self, brand, color, seats):
        self.brand = brand
        self.color = color
        self.seats = seats

class ContainerCar(Car): # Kế thừa Car
    def __init__(self, brand, color, seats):
         # khởi tạo phương thức CHA
        super().__init__(brand, color, seats)
        # thuộc tính riêng của container
        self.container = True
        
    def show(self):
        print(self.brand, self.color, self.seats, self.container)
    
    
CA = ContainerCar('Truck','Black', 2)
CA.show()