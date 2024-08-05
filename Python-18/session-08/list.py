# Cách định nghĩa 1 list
empty_list = [] # list rỗng không có phần nào
my_list = ["banana", "kiwi","apple", "apple", 18, True]
'''
- Các phần tử trong list được đánh chỉ số index từ trái qua phải
bắt đầu bằng giá trị 0.
banana --> index = 0
kiwi --> index =  1
...
'''
# 1. Làm thế nào để truy cập vào phần tử của list
# Vd1: Làm sao để in ra: kiwi ?  ==> Dựa vào index của phần tử
print(my_list[1]) # truy xuất phần tử có index = 1
print(my_list[-1]) # lấy theo chiều từ phải sang trái, bắt đầu = -1
# Vd2: Lấy ra nhiều phần tử một lúc
# Cú pháp list[start:end]
print(my_list[0:2]) # ==> list mới chứa các phần tử đã lấy

# 2. Thay đổi giá trị của phần tử trong list
# Vd3: Thay đổi apple thành orange
my_list[2] = "orange" # gán lại giá trị mới cho phần tử có index = 2
print("after changing => ", my_list)
#3. Kiểm tra sự tồn tại của một phần tử trong list
if "watermelon" in my_list: # Nếu kiwi có trong list
    print("Có chứa") # thì in ra là có
else:
    print("ko có")
    
# 4. Thêm mới phần tử vào List
# sử dụng append() thêm vào cuối list
# my_list.append("watermelons")
# print(my_list)
# Sử dụng insert() để chèn vào vị trị cụ thể trong list
# my_list.insert(3, "watermelon")
# print(my_list)

# 5 Gộp 2 list lại với nhau
fruits_one = ["apple", "banana", "kiwi"]
fruits_two = ["mango", "pineapple", "papaya"]
print("before",fruits_one)
# Gộp fruits_two vào fruits_one
fruits_one.extend(fruits_two)
print("after",fruits_one)

# 6.Làm sao xóa phần tử trong list
# vd: Xóa papaya khỏi fruits_two
fruits_two.remove("papaya")
print("after remove",fruits_two)

# 7. Xóa tất cả phần tử trong list
fruits_two.clear() # xóa hết phần tử, trả lại một list [] rỗng
print("after clear",fruits_two)
# 8. Xóa luôn một list
del fruits_two # xóa mất list, list sẽ ko tồn tại nữa
#print(fruits_two)

# 9. Sử dụng vòng lặp với list
mylist = ["apple", "banana", "kiwi"]
# In ra từng phần tử của list
for i in mylist:
    print(i) # i là đại diện cho phần tử đang lặp qua.