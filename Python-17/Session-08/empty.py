# 1. Mở file empty.txt ra, với chế độ ghi đè ==> w
# 1. Mở file empty.txt ra, với chế độ ghi bổ sung ==> a
file = open("Python-17/Session-08/empty.txt", "a")
# 2. Ghi nội dung vào file
# content = "Learn Python 2 \nLearn Python 3"
# file.write(content)


# '''
# - phương thức write ghi đè nội dung vào file
# - Sử dụng \n để xuống dòng, \t để thụt vào 1 tab
# '''

# Đối với nội dung ở dạng list
# my_list = ["line 1", "line 2"]
# file.writelines(my_list)

# Ghi nối nội dung vào phía sau nội dung đã có sẵn
my_str = "noi dung ghi them vao cuoi"
file.write(my_str)

# in nội ra terminal
print(my_str)

# Đóng file lại
file.close()

