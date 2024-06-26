# Code lại Class HocSinh

class HocSinh:
    
    def __init__(self, ten, tuoi, gioi_tinh):
        self.ten = ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        
    def show(self):
        print("HocSinh: " + self.ten, self.tuoi, self.gioi_tinh)
  
# Lớp HocSinh như một khuôn đúc
# Đúc ra (khởi tạo) đối tượng học sinh cụ thể

hsA = HocSinh('NV A', 12, 'Nam')
hsA.show()

hsB = HocSinh('LT B', 18, 'Nữ')
hsB.show()