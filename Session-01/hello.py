class Vehicle:
    def __init__(self, brand, color):
            self.brand = brand
            self.color = color
    def drive(self):
           print(f"The {self.color} {self.brand} is driving.") 

class Car(Vehicle):
      def honk(self): 
            print("Beep beep!") 

class Bike(Vehicle):
         def ring_bell(self):
               print("Ring ring!")
