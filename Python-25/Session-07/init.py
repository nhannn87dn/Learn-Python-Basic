class HocSinh:
    def __init__(self,name, age, school_name):
        self.name = name
        self.age = age
        self.school_name = school_name
    def getInfo(self):
        print(self.name, self.age, self.school_name)
# Khởi tạo học sinh A từ class HocSinh
hsA = HocSinh('Ng van A', 12, 'Lê Quý Đôn')
# hs A có được thông tin riêng ngay khi khởi tạo
hsB = HocSinh('Ng van B', 10, 'Trần Hưng Đạo')

hsB.getInfo()