# b1. Định nghĩa hàm
# Hàm ko có tham số
def ten_ham():
    print('lệnh 1')
    print('lệnh 2')
    #...n khối lệnh
    
#b2: Gọi hàm
#ten_ham() 
# thì các câu lệnh bên trong khối hàm
# sẽ được thực thi
# x = 2
# y = 3
# result_1 = x + y

# a = 5
# b = 6
# result_2 = a + b

# Hàm có tham số
def tinh_tong(a, b): # a, b gọi là đối số
    result = a + b
    print(result)
    
# Tính tổng 2 số 2, 3
# tinh_tong(2,3) # 2, 3 gọi là tham số
# tinh_tong(5,6)

# Hàm có tham số mặc định
# def sayHello(name = "Chưa có tên"):
#     print("Hello " + name)
    
# sayHello("Tuấn")
# sayHello()
# x và y bắt buộc truyền
# phep_tinh: tùy chọn (truyền hoặc ko cần truyền)
# tham số tùy chọn, nó phải nằm sau tham số bắt buộc
def tinh_toan( x, y, phep_tinh='cong'):
    if phep_tinh == 'cong':
        print(x + y)
    elif phep_tinh == 'nhan':
        print(x * y)
        
tinh_toan(2,5, 'nhan')

# Hàm có return

def sum(a,b):
    # trả về một kết quả xử lý
    return a + b

# đổi với hàm có return
# khi gọi thì đặt một biến để hứng kết quả
result = sum(2,3)
print(result)

# Tổng kết lại về hàm
# 1. hàm ko có tham số
# 2. hàm có tham số
# 3. hàm có tham số tùy chọn
# 4. hàm có return
