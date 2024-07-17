my_set = {"banana", "orange"}
# Truy cập vào phần tử trong set
# for i in my_set:
#     print(i)
    
# Check xem set có bao nhiêu phần tử
#print(len(my_set))
# check sự tồn tại của một phần tử trong Set
# if "kiwi" in my_set:
#     print("Có tồn tại")
# else:
#     print("Ko tồn tại")

# Thêm mới một phần tử vào set
# my_set.add("kiwi")
# my_set.add("lemon")
# print(my_set)

# Xóa phần tử ra khởi set
# my_set.remove("orange")
# print(my_set)

set_one = {"cam", "xoai"}
set_two = {"tao", "man", "nho"}
# Gộp 2 set lại với nhau ?
set_one.update(set_two) # ==> gộp set_two vào set_one
print('set_one',set_one)
set_three = set_one.union(set_two)
print('set_three',set_three)