# Định 1 hàm (function)
def sayHello():
    print('lệnh 1')
    print('lệnh 2')

# Gọi hàm (chạy hàm này)
#sayHello()

def tinhTong(k, v):
    result = k + v
    print(result)

# Tại vì sao lại cần đến hàm ?
# x = 5
# y = 2
# result = x + y
# print(result)
#tinhTong(5,2)

### Ở một ví trị khác
# j = 8
# i = 10
# total = i + j
# print(total)
#tinhTong(8,10)

# 3. Quy tắc đặt tên hàm ?
# Bằng với quy tắc đặt tên biến

'''
snakeCase: get_element_by_id
PascalCase: GetElementById
camelCase: getElementById
'''
#4 Các cách sử dụng hàm khác nhau
# 4.1 Hàm ko có tham số
# Là một hàm mà chỉ thực hiện khối lệnh
# Không có dữ liệu đầu vào, đầu ra
def welcome():
    #khối lệnh
    print('Chào mừng bạn !')

# gọi hàm ko có tham số
#welcome()

# 4.1 hàm có tham số
# Là một hàm nhận dữ liệu đầu vào và
# thực thi khối lệnh
def xinChao(name):
    print('Xin chào ' + name)
# name: được gọ là tham số đầu vào (parameter)
#xinChao('Tuấn') # name = Tuấn (argument = Đối số)
#xinChao('Minh') # name = Minh

# hàm có nhiều tham số
def cal(x, y, z): # mỗi tham số cách nhau = dấu phẩy
    print(x + y + z)
# Gọi hàm có nhiều tham số
#cal(1,2,3) #

# Hàm có tham số mặc định 
# Tham số mặc định luôn đặt cuối cùng
def calMulti(x, y, pt='+'): # tham số mặc định là pt
    if(pt == '*'):
        print(x * y)
    elif (pt == '/'):
        print(x / y)
    elif (pt == '-'):
        print(x - y)
    else:
        print(x + y)
# Cách gọi hàm có tham số mặc định
#calMulti(2,6) #  1. 8
#calMulti(8,4, '/') # 2. 2

# 5. hàm có return
def calV2(x, y, z):
    return x + y + z

# Gọi hàm có return
print(calV2(2,3,4))
kq = calV2(2,3,4) # = x + y + z
print(kq)




