# x = 5
# y = 2
# result = x + y
# print(result)

# a = 10
# b = 5
# result2 = a + b
# print(result2)

# i = 7
# j = 5
# result3 = i + j
# print(result3)

# def tinh_tong(a,b):
#     result = a + b
#     print(result)
    
# tinh_tong(5, 2)
# tinh_tong(10, 5)
# tinh_tong(7, 5)

# có 3 kiểu hàm trong python
# Kiểu 1 - hàm ko có tham số
# def sayHello():
#     print("Hello Python!")

# # gọi hàm
# sayHello()
# Kiểu 2: Hàm có tham số

# name ở trong () --> đối số
# def sayHello(name):
#     print("Hello ", name)
    
# sayHello("Jane")
# sayHello("Nhan")

# Kiểu 3: Hàm có return

# def sum(a,b):
#     # Dùng return khi mà
#     # mình cần tính toán
#     # cuối cùng trả về một kết quả
#     return a + b

# kq = sum(2,5) # 7
# print(kq)

# Nếu khách hàng là VIP và hóa đơn mua hàng > 500$ thì được discount 10%
# Nếu khách hàng là GOLD và hóa đơn mua hàng > 500$ thì được discount 7%
# Nếu khách hàng là SILVER và hóa đơn mua hàng > 500$ thì được discount 5%
# Còn lại thì được discount 2%
# --------------
# Tính discount của khách hàng nguyễn văn A,
# Được biết hạng là GOLD, đã có hóa đơn mua hàng 600$

def getDiscount(level, totalOrder):
    if level == 'VIP' and totalOrder > 500:
        discount = 10
        return discount
    elif level == 'GOLD' and totalOrder > 500:
        discount = 7
        return discount
    elif level == 'SILVER' and totalOrder > 500:
        discount = 5
        return discount
    else:
        discount = 2
        return discount
    
discount_A = getDiscount('GOLD', 600)
print(discount_A)

# first_name
# last_name

# Yêu cầu: hiển thị tên đầy đủ: full_name

# def getFullname(first_name, last_name):
#     full_name = first_name + " " + last_name
#     return full_name

# print(getFullname('jane', 'Nguyen'))

# hàm có đặt tên, tên là sum
# def sum(a,b):
#     return a +b

x = lambda a, b : a + b
print(x(5, 2))