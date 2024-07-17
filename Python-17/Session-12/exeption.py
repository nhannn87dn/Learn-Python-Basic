# print(4=>4)
# print("hello world")
# try:
#     result = 4/0
#     print(result)
# except ZeroDivisionError:
#     print("Không thể chia cho zero")
#     #ghi log, lưu những lỗi đó ra thành một file
# except:
#     print("Lỗi không xác định")
    
    
# print("Hello world")

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("Không thể chia cho 0")
#     else:
#         print("Kết quả là: ", result)
#     finally:
#         print("Đã thực hiện xong lệnh")
        
# divide(5,0)

'''
Tạo một biến x = giá trị nhập từ người dùng
Nếu x > 0 thì in ra là số dương
Nếu x < 0 là số âm
Còn lại là 0
'''

try:
    x = input("Nhập vào x: ")
    print(x, type(x))

    if x > 0:
        print('so Duong')
    elif x < 0:
        print('So Am')
    else:
        print('So zero')
except TypeError:
    print('Vui lòng nhập vào một giá trị dạng số')
 
    
print("Next Step")