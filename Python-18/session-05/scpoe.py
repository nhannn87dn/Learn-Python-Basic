# Phạm vi sử dụng biến

x = 3 # nó nằm ngoài khối

def sum():
    global y # có ý nghĩa, đăng ký y là biến toàn cục
    y = 5 # y bên trong khối
    print('x',x) # Bên trong khối
    
sum() # gọi hàm

# In ra y bên ngoài khối
print('y', y) # Bên ngoài


# KL1: Biến ở ngoài khối --> trong khối dùng được
# KL2: Biến ở trong khối --> ngoài khối ko dùng được
# KL3: Biến ở trong khối --> ngoài khối dùng được 
#                            Nếu được khai báo global
