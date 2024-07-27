
class HocSinh:
    
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    
    def __str__(self):
        return f"HocSinh(name='{self.name}', age={self.age})"
        
    '''
    Một cái hàm mà định nghĩa trong một class
    thì gọi nó là method (phương thức)
    '''
    def show_name(self):
        print(self.name)
        
    def show_all(self):
        print(self.name, self.age, self.gender, self.address)
        
    def update_name(self, new_name):
        self.name = new_name
           
# name, age, gender, address ==> trạng thái của đối tượng
# HocSinh --> tên tự đặt lớp

# hsA = HocSinh() # Khởi tạo đối tượng hsA từ lớp HocSinh
# hsB = HocSinh() # Khởi tạo đối tượng hsB từ lớp HocSinh

# Truy cập vào trạng thái của đối tượng
#print(hsA.age)
#print(hsB.age)
# Thay đổi thông tin trạng thái cho đối tượng
# hsB.age = 22
# hsB.name = 'nguyen van B'

# #print(hsB.name, hsB.age)
# hsB.show_name()
# hsB.update_name('Trần Văn B')
# hsB.show_name()
# hsC = HocSinh()
# hsC.name = 'ten C'
# hsC.age = 12
# hsC.gender = 'female'
# hsC.show_name()

# Cách khởi tạo mới khi có dùng __init__
#__init__(self, name, age, gender, address)
hsA = HocSinh("hsA",12, 'male','123THD')
hsA.show_name()
hsA.show_all()

hsB = HocSinh('hsB',20, 'female', '38yenbai')
hsB.show_all()

hsC = HocSinh('hsC',19, 'male', '12TP')
print(hsC)