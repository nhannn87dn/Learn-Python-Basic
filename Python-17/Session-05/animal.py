class DongVat:
    def __init__(self, name, move, food, gender):
        self.name = name
        self.move = move
        self.food = food
        self.gender = gender
    # phương thức để hiển thông tin trạng thái của Lớp
    def show(self):
        print(self.name, self.move, self.food, self.gender)
        
# Khởi tạo đối tượng Chó
Dog =DongVat('Bob Dog', '4 chân', 'Xương', 'Boy')
Dog.show()
# Khởi tạo đối tượng Mèo
Cat = DongVat('Cat Meo', '4 chân', 'Cá', 'Girl')
Cat.show()
# Khởi tạo đối tượng Gà
Chicken = DongVat('Chicken', '2 chân', 'Lúa', 'Gà mái')
Chicken.show()
