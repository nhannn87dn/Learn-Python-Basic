# Định nghĩa một Class (Lớp) XeOto và mô tả 
# những đặc tính của lớp này.

# - Khởi tạo một đối tượng từ Lớp trên
# - In ra thông tin của đối tượng

# Gợi ý: Xeoto thì có xe ben, ủi, container, xe taxi, bus
# Các loại xe trên: có đặt tính gì chung.

class Oto:
    def __init__(self, banh, mau, hang_xe, dung_tich):
        self.banh = banh
        self.mau = mau
        self.hang_xe = hang_xe
        self.dung_tich = dung_tich
        
    def show_info(self):
        print(self.banh, self.mau, self.hang_xe)
        
# Khởi tạo đối tượng từ Lớp Oto
xeUi = Oto(1, 'Vang', "Busan", 2.5)
xeUi.show_info()
xeContainer = Oto(16, "Đỏ", "Truck", 8)
xeContainer.show_info()