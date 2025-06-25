# Cách định nghĩa 1 hàm
def xin_chao():
    print('Xin chao')
    print('Toi la Python')
    
# Cách sử dụng hàm --> gọi hàm, thực thi hàm
#xin_chao()
# Khi gọi hàm thì hàm sẽ thực thi các câu lệnh bên trong khối
# hàm như trên được gọi là hàm ko có tham số.

def sayHello(name):
    print('Xin chào '+ name)
# name --> được gọi làm tham số (parameter)
# Cách gọi hàm có tham số
# sayHello('Bình') # Bình, Anh ---> gọi là đối số
# sayHello('Anh')

# Bài tập nhỏ
# Câu 1: Viết một hàm thực hiện in ra: "Học python cơ bản"
# Câu 2: Viết một hàm có tên là playTV, với giá trị đầu vào là
# channel. Thực hiện việc in ra.
# - Đang xem: VTV1
# - Đang xem: VTV2

# Câu 3: Viết một hàm tính tổng 2 số với giá trị đầu vào (tham số)
# a và b. In ra tổng của a và b.
def tinhTong(a, b):
    print(a + b)
#tinhTong(2,4)
# Khi đó mình hiểu
# 2 ==> a
# 4 ==> b
# tinhTong(2,8)

# Hàm có tham số tùy chọn (ko bắt buộc truyền khi gọi hàm)
#Ví dụ: Hàm có tham số với giá trị mặc định
def sayGoodBye(name = 'EveryBody'):
    print('Tạm biệt ', name)
# sayGoodBye()# ko cần truyền đối số
# sayGoodBye('Bình')
# sayGoodBye('bảo anh')
# Khi hàm có nhiều tham số, thì tham số mặc định luôn phải
# để cuối cùng của danh sách
def tinhToan(a,b, phep_tinh = '+'):
    if phep_tinh == '*':
        print(a * b)
    elif phep_tinh == '/':
        print(a /b)
    else:
        print( a + b)
        
# tinhToan(2,4)# kq:
# tinhToan(2,4, '*')

# hàm có return
def sum(a,b):
    return a + b # return là trả lại, trả lại một kết quả gì đó
kq = sum(2,4) #kq
print('kq', kq)
print(sum(52,4)  + 4)

# bài tập áp dụng:
# Câu 1: Cho 2 giá trị x và y nhập từ người dùng.
# Viết hàm tính Tổng x và y số và in ra.
# Nếu nhập x = 2, y = 4. Kết quả mong muốn: = 6

def calSum(i,j):
    print(i + j)

#x = int(input('x: '))
#y = int(input('y: '))
#calSum(x, y)

# Câu 2: Viết một hàm kiểm tra 1 số z có phải là số dương không.
# Cho biết z là giá trị nhập từ người dùng.
# Nếu là z là số dương: In ra "z là số dương"
# Nếu z là số âm: In ra "z là số âm"
# Còn lại: In ra "z không hợp lệ"

def checkNumber(n):
    if n > 0:
        print('n la so duong')
    elif n < 0:
        print('n la so am')
    else:
        print('n la ko hop le')
# lấy giá trị nhập từ người dùng
z = int(input('n: '))
# viêt hàm để kiểm tra z
checkNumber(z)