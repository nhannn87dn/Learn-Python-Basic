#TH1: Đặt biến ngoài khối, trong khối dùng được không ?
# Kết luận: Được
# x = "awesome"
# def myfunc():
#     print("Python is " + x)     
# myfunc()

#TH2: Khai báo trong khối, ngoài khối dùng được không ?
# Kết luận: Không được
# def myfunc():
#     x = "aw" # Trong khối
#     print("Python is " + x)     
# myfunc()
# print('this is ', x) # ngoài khối

#TH3: Biến toàn cục
## Biến toàn cục trong khối, ngoài khối dùng được
def myfunc():
    global x # định nghĩa biến toàn cục
    x = "aw" # Trong khối
    print("Python is " + x)     
myfunc()
print('this is ', x) # ngoài khối