# Cách định nghĩa 1 function

# Hàm void, hàm thủ thục, chỉ thực thi lệnh
# mà không return
def tinh_tong():
    print("lệnh 1")
    print("lệnh 2")
    
#tinh_tong() # Gọi hàm --> thực thi hàm

# Loại thứ 2: Hàm có tham số
def tinhTong(a,b): # a, b --> gọi là đối số, arguments
    print('a + b = ', a + b)

# Gọi hàm:
#tinhTong(2,3) # 2,3 --> được gọi tham số. (Parameters)

def sayHello(name):
    print('Hello ' + name)
    
sayHello('Tuấn')
sayHello('Khoa')
sayHello('Thái An')

# Vd3: hàm có chứa tham số mặc định
# đối số mặc định, thường để cuối cùng
def phep_tinh(x, y, type='+'):
    if type == '+':
        print(x + y)
    elif type == '-':
        print(x - y)
    elif type == '*':
        print(x * y)
    else:
        print('Phép tính không xác định')

phep_tinh(5, 6) # ko truyền type, thì type mặc định là +

def sayName(name, age = 18):
    print('Hello ', name, age)

#sayName( 12, 'Khoa')

#vd 4: hàm có return

def cal(a,b):
    return a + b # trả về kết quả

result = cal(2,3) # gọi hàm
# result là một biến, để hứng kết 
# quả của hàm có return
print('result', result)
