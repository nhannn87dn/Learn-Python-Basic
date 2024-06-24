a = 2

def my_function():
    x = 5
    print('Tôi là x: ', x, a)
 # kết thúc khối
   
my_function()
# print('x bên ngoài', x)

# Kết luận: 
# - Khai báo biến bên trong khối 
# --> ngoài ko sử dụng được
# - Khai báo biến ngoài khối --> trong khối dùng được

# Biến toàn cục với từ khóa global

def main():
    global z
    z = 12
    print('z trong khối ', z)
    
main() # gọi hàm
print('z ngoài khối', z)
# Khi mà python thực thi
# python sẽ đưa biến z lên đầu file
# ==> biến khai báo bên ngoài khối