# Cú pháp Định nghĩa Class (Lớp)
class HocSinh:
    # Khai báo các thuộc tính ở trong khối
    ten = 'Nguyễn văn A'
    tuoi = 12
    gioi_tinh = 'Nam'
    
    # định nghĩa các phương thức (method) cho Lớp
    def di_chuyen():
        print('Xe đạp')
    # có tham số self
    def show(self):
        print(self.ten, self.tuoi)
    # có tham số self và các tham  số khác
    def updated(self, name, tuoi):
        self.ten = name
        self.tuoi = tuoi
        
    # KL: self phải được đặt đầu tiên trong danh sách
    # các tham số của phương thức
    
# Quy tắc đặt tên Class
# Kí tự đầu tiên viết HOA --> PascalCase

# Khởi tạo đối tượng từ Class
hoc_sinh_A = HocSinh()
# HocSinh()  --> khởi tạo đối tượng
# hoc_sinh_A --> instance (object) đối tượng được tạo ra

# Truy xuất đến các thuộc tính của đối tượng (object)
# print('hoc_sinh_A.ten',hoc_sinh_A.ten)
# print('hoc_sinh_A.tuoi',hoc_sinh_A.tuoi)
# Tạo ra hơn 1 đối tượng từ một Lớp
hoc_sinh_B = HocSinh()
hoc_sinh_B.ten = 'Phan chu B' # gán lại giá trị mới cho ten
hoc_sinh_B.tuoi = 22 # gán lại giá trị mới cho tuoi
# print('hoc_sinh_B.ten',hoc_sinh_B.ten)
# print('hoc_sinh_B.tuoi',hoc_sinh_B.tuoi)

# Thực thi phương bên trong Class
hoc_sinh_B.show() # không cần truyền tham số seft
# Lí do, Class tự hiểu là chính nó rồi

hoc_sinh_B.updated('Le Tuan', 19) # thay đổi
hoc_sinh_B.show() # in ra lại