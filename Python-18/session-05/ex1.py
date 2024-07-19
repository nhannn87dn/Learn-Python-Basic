# Task 1: Định nghĩa 1 hàm ko có tham số. 
# Thực hiện việc in ra câu: "Hello python !"

def helloPython():
    print("hello Python")

helloPython()

# Task 2: Định nghĩa hàm có tham số.
# Mà khi gọi:
#  - sayHi("Tuấn") --> in ra: "Chào Tuấn"
#  - sayHi("Long") --> in ra: "Chào Long"

# def sayHi(name):
#     print("Chào ", name)
    
# sayHi("Tuấn")

# Task 3: Viết một hàm trả về tổng 2 số a,b
# - Tính và in ra tổng của 2, 3
# - Tính và in ra tổng của 5, 10
# - Đầu vào: 2 số
# - Xử lý: Tính tổng
# - Đầu ra: trả về tổng

def tinh_tong(a,b):
    tong = a + b
    return tong
# gọi hàm
r =tinh_tong(2,3)
print(r)
