# x = int(input(' Nhap vao x: '))
# y = int(input(' Nhap vao y: '))
# print(x + y)

#z = 123 # int

# 123.0
# print(float(z))

# print( 3 > 2) # Đúng - True
# print( 1 < 0) # Sai --> False, boolean
# t = 1 < 0
# print(type(t))

x = 1
y = 2

# Muốn 2 câu lệnh sau chạy khi x > y 
# nếu x > y
#     thì chạy
#     print("cau lenh 1")
#     print("cau lenh 2")

# if x > y: # true
#     print("cau lenh 1")
#     print("cau lenh 2")
# else:
#     print("cau lenh 3")

# or là hoặc
#print(x > 1 or y < 0)
#      true or false = true


# and là và 
#print(x > 0 and y > 1)
#      True and  true = true

#print(x > 0 and y < 1)
# true and false =  false

# print(x == y) # False
# print(x != y) # 5 ko bang 2 dung ko


# - Neu dtb >= 9 thi hs Xuat Sac
# - Neu dtb >= 8 thi hs Gioi
# - Neu dtb >= 6.5 thi hs Kha
# - Con lại là Trung Bình

dtb = 4.5

if dtb >=9:
    print('Xuat sac')
elif dtb >= 8:
    print('GIoi')
elif dtb >= 6.5:
    print('Kha')
else:
    print('Trung Binh')