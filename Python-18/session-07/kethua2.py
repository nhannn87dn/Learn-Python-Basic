class DongVat:
    def __init__(self, ten, chan, di_chuyen):
        self.ten = ten
        self.chan = chan
        self.di_chuyen = di_chuyen
    
    def getName(self):
        print("getName", self.getName)
    
    def move(self):
        print("Bằng 2 Chân")
    
class Chim(DongVat):
    
    def __init__(self,ten, chan, di_chuyen):
        super().__init__(ten, chan, di_chuyen)
    
    def getInfo(self):
        print(super().ten) # truy cập vào ten của CHA
    
    def move(self):
        print("Bay 2 cánh")

class Meo(DongVat):
    def move(self):
        print("Đi 4 cánh")
        
chimBocau = Chim("Bồ câu", 2, "Bay")
chimBocau.getName()
chimBocau.move()