# a = "Hello, World!"
# print(a.upper())
# b= "HELLO, WORLD!"
# print(b.lower())
# c = 'hello world!'
# print(c.title())

# tách chuỗi
# str  = "python-nodejs"
# print(str.split('-'))

# strv2 = " Học python    "
# print(len(strv2))
# # Để bỏ kí tự trắng trước và sau chuỗi
# print(strv2.strip())
# print(len(strv2.strip()))

# txt = "Welcome to my world"
# # thay thế từ world thành house
# print(txt.replace('world', 'house'))

# Câu 4: Có chuỗi: "chao mung Tuan den voi Aptech"
# - Lấy ra từ "Tuan" sau đó in ra tên viết HOA
# - Thay thế Aptech thành Softech sau đó in ra chuỗi

myName = 'Nhân'
myAge = 38
str = "Tôi là {} năm nay tôi {} tuổi"
print(str.format(myName, myAge))

# Đặt 1 x biến bằng Tên của mình
# Một biến y = Trường học của mình
# In: Tôi là {}, tôi học trường {}

quantity = 2
price = 50
txt = "Mua {0} cái bánh hết {1} đô la. Em tôi ăn hết {0} cái bánh"
print(txt.format(quantity, price))
# dùng chỉ lệnh
mark = 8
subject  = "English"
# Tôi thi môn English được 8 điểm.
txt  = f"Tôi thi môn {subject} được {mark} điểm."
print(txt)