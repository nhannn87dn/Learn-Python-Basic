# Bài 8 List và Tuple

# 1. Cách định 1 nghĩa 1 list ?

my_list = [] # list rỗng chưa có phần tử nào

my_list = [1, 2,3, 'string', True, False, True]

'''
Đặc điểm của List gì ?
- Các phần tử sắp theo thứ tự
- Các phần tử có thể thay đổi được sau khi khai báo. Thêm mới, xóa, sửa
- Cho phép trùng lặp phần tử
'''

#my_list[0] = 2

# 2. Cách định nghĩa một tuple

my_tuple = (1, 2, 3, 'string', True, False, True)

'''
Đặc điểm của Tuple gì ?
- Các phần tử sắp theo thứ tự (index, bắt đầu là 0)
- Các phần tử không thể thay đổi sau khi định nghĩa
- Cho phép trùng lặp phần tử
'''

#2.1 Thay đổi phần tử của tuple

#my_tuple[0] = 1 # ko làm được
# Nhưng bạn có thể chuyển nó thành list để xử lý

convert_list = list(my_tuple) # Biến tuple thành list
convert_list[0] = 2 # thay đổi 
my_list = tuple(convert_list) # Chuyển list ngược lại thành tuple


# 3. Cách định nghĩa một Dictionaries

my_dic = {
    "name": "Ngoc Nhan",
    "age": 36,
    "age": 38
}

'''
- Các phần tử có thứ tự cố định
- Các phần tử có thể thay đổi được
- Không cho phép trùng lặp phần tử
'''


# 4. Cách định nghĩa 1 Sets

my_set = {1, 2,'string', True}

'''
 - Các phần tử không có thứ tự sắp xếp
 - Các phần tử không thể thay đổi sau khi định nghĩa
 - Không cho phép trùng lặp
 - Vị trí các phần tử của set sẽ thay đổi khi mỗi lần print
'''

print(my_set)

# 5. Bắt lỗi, xỷ lý ngoại lệ

# x = 1
# y = 0
# result = x/y
# print(result)
    
# try:
#     x = 1
#     y = 0
#     result = x/y
#     print(result)
# except: # tất cả các lỗi đều rơi vào except
#     # Nếu xảy ra lỗi thì nó rơi vào except để tùy chỉnh thông lỗi
#     print('Có lỗi xảy ra')    
    

try:
    x = 4
    y = 2
    result = x/y
   
except ZeroDivisionError: # Nếu gặp lỗi chia cho 0 thì nó mới rơi vào đây
    print('Lỗi chia một số cho 0')    
except: # lỗi khác
    print('Có lỗi xảy ra')
else: # nó chạy khi ko có lỗi nào xảy ra
    print(result)
finally:
    # dù lỗi, hay ko lỗi thì nó vẫn chạy qua đây
    print('Kết thúc chương trình')