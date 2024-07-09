# Các phương thức xử lí chuỗi
my_list = [1,2,3,4,5,6]
# print(my_list[3:5])
## 1. Cắt chuỗi
my_str = "Hello Python!"
#print(my_str[6:8])
#print('my_str', my_str[-4:-1]) # hon
print(my_str[2:]) # ko điền stop
print(my_str[:5]) # mặc định start = 0
# Biến đổi chữ
# --> Chữ HOA hết
h = my_str.upper() # HELLO PYTHON!
print(h) #
print(h.lower()) # hello python !

a = "Hello, World!"
z = a.split(",")
print(z[1].lstrip())

txt = "Welcome to my world"
print(txt.replace("world", "home")) 
