#Cách  định nghĩa 1 lớp Class trong Python
class HocSinh:
    name='Tên'
    age=12
    school_name='shool name'
    # Tạo một method
    def showInfo(self):
        print(self.name, self.age, self.school_name)
        
    def updateName(self, newName):
        self.name = newName # gán lại giá trị mới cho thuộc tính name
        

#name, age, school_name --> gọi là attribute(Thuộc tính)
# Tên, 12, shool name --> State, trạng thái hiện tại của đối tượng

# Làm sao để khởi tạo đối tượng (Object) Học Sinh A từ lớp HocSinh

hsA = HocSinh() # Cú pháp để khởi tạo một đối tượng hsA từ class HocSinh
print(hsA.name)
# Thay đổi lại thể hiện của của đối tượng A, trạng thái riêng của hsA
# hsA.name = 'Nguyễn Văn A' # gán lại thuộc name = giá trị mới
# hsA.age = 10
# hsA.school_name = 'Lê Văn Tám'
hsA.updateName('nguyen van A')
print(hsA.name)
hsA.showInfo() # gọi phương thức


# hsB = HocSinh()

# hsB.name = 'Nguyễn văn B'


# hsN = HocSinh()

# hsN.name = 'Minh Nhật'


# Bài tập áp dụng
# Câu 1: Con chó Alaska, và Poodle --> Dog
# Tạo tạo các Object riêng cho từng loại chó từ lớp Dog trên
# Gợi ý: Dog sẽ có những attributes nào ?

# Cau 2: Tạo 2 method có tên là
# - getInfo: Lấy và in ra thông tin của đối tượng
# - updateInfo: Cập nhật thông tin tất cả attributes của đối tượng