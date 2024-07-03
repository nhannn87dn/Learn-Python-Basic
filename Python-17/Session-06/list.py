# Kiểu dữ liệu List
#----------------------------
# 1. Cách định nghĩa
my_list = [] # Hợp lệ, nó một list trống rỗng
# - List có thể chứa các kiểu dữ liệu khác nhau
# - Phần tử trong list có thể trùng lặp
# - Mỗi phần tử được đánh số, bắt đầu là 0 gọi là index
my_list = [1, 2, 'three', 2, True, False]
#----------------------------
# TH2: Truy cập vào phần tử của List
print(my_list[2]) # dựa vào index để lấy
print(my_list[-2]) # => True. Thì nó lấy từ phải qua trái.

# Tách list
# Lấy ra phần từ index số 2, 3
print(my_list[2:4]) 

# TH3: Thay đổi giá trị của phần tử trong List
my_list[3] = 4 # thay đổi giá trị mới cho phần tử, 
#có index = 3

print('new my_list ==> ',my_list)

# TH4: Kiểm tra xem trong List có tồn tại 1 phần tử
# nào đó không ?

if 'three' in my_list:
    print('yes')

# TH: THêm mới một phần từ vào List
profile = ['Nhan', 36]
# Thêm vào email nữa thì làm sao ?
profile.append('nhan@softech.vn')

print('profile',profile)

# Chèn 1 phần tử vào vị trí bất kỳ trong list
profile.insert(1, '0988777666')

print('profile',profile)

# Gộp 2 list lại với nhau
gio_a = ['cam', 'xoai']
gio_b = ['Tao', 'Dua hau']
gio_a.extend(gio_b) # list b, sẽ được nối thêm vào a
print(gio_a)

# TH 5: Xóa một phần tử trong List
gio_b.remove('Tao') # Xóa phần tử Táo
print('gio_b',gio_b)

# TH6: Duyệt phần tử của List với vòng lặp
mylist = ["apple", "banana", "kiwi"]
for x in mylist:
    print(x)
