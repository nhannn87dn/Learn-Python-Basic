thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[:2])

# cách để thay đổi giá trị  phần tử của tuple
# convert nó thành list
l= list(thistuple)
print(type(l), l)
l[2] = 'kiwi'
print(l)
# sau khi cập nhật xong --> convert list hành tuple lại
t = tuple(l)
print(t, type(t))

# BÀI TẬP ÁP DỤNG
# Câu 1: Hãy định nghĩa một tuple với 5 phần tử 
# là tên của 5 bạn học của mình
# Sau đó in ra tên của bạn thứ 3 trong tuple trên.
friends = ('Ti', 'Teo', 'Tun', 'Bi', 'Bo')
# Câu 2: In ra tên bạn từ thứ 2 đến cuối tuple

# Câu 3: In ra tên bạn từ cuối --> bạn thứ 3.
print(friends[-1:-4:-1])

# Câu 4: Đổi tên bạn thứ 3 thành: Xì trum
