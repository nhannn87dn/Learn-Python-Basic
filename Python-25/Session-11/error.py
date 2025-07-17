# # print(4 >= 4)
# # print(10/0)
# # 
# def sayHello(name):
#     print('Hello ', name)

# try:
#     sayHello()
# # nếu có lỗi xảy ra --> nhảy sang except
# except:
#     print('Có lỗi xảy ra') # xử lý lỗi thân thiện


def divide(x, y):
    return x / y

try:
    result = divide(6,2)
except ZeroDivisionError:
    print("Không thể chia cho 0")
else:
    print("Kết quả là: ", result)
finally:
    print("Đã thực hiện xong lệnh")