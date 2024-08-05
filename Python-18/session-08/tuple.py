this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
empty_tuple = () #  tuple rỗng
print(type(this_tuple))

# 1. Truy cập vào phần tử của tuple
print(this_tuple[1])

# Ko thể thay đổi giá trị của phần tử trong tuple
#this_tuple[1] = "kiwi" # ko thể
# TUY NHIÊN bạn có thể ĐI VÒNG bằng cách chuyển tuple thành list

#vd: Muốn đổi banana thành kiwi
# b1: chuyển tuple thành list
my_list = list(this_tuple) # ép kiểu thành list
# b2: thay đổi phần tử: thêm, thay giá trị, xóa
my_list[1] = "kiwi" # Nếu là list thì thay đổi đc giá trị phần tử
# b3: chuyển list thành tuple ngược lại
this_tuple = tuple(my_list)
# b4: có được tuple như ý muốn
print(this_tuple)

# Phân rả tuple

fruits = ("apple", "banana", "cherry")
# (tao, chuoi, cheri) = fruits # xổ ngược
# Chỉ lấy 1 phần tử thôi
(_, _, cheri) = fruits # bỏ qua với dấu _
print('cheri', cheri)
# Chỉ lấy apple, các phần tử còn lại dồn vào một biến
(tao, *new_fruits) = fruits # dấu * dồn các phần tử còn lại vào 1 biến
print('tao', tao)
print('new_fruits', new_fruits) # list chứa các phần tử còn lại 

# Lặp qua phần tử với for
for f in fruits:
    print(f)