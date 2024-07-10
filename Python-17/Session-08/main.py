# Đọc nội dùng từ file test.txt rồi hiển thị ra
'''
- Tham số đầu tiên là đường dẫn (path) đến tập tin
cần đọc.
- Tham số thứ 2: Tùy chọn, mặc định rt
'''
# Bước 1. Mở tập tin
file = open("Python-17/Session-08/test.txt", "rt")
# Bước 2: Đọc tập tin

#content = file.read() # Đọc tất cả nội dung

#content = file.read(3) # Lấy 3 kí tự đầu tiên
# line1 = file.readline() # Đọc từ đầu dòng, đến cuối dòng,
# line2 = file.readline() 
# print(line1,line2)

# Lấy 3 dòng đầu tiên
# line = 1
# while line <= 3:
#     content_line = file.readline()
#     print(content_line)
#     line = line + 1

# for line in range(1,4):
#     content_line = file.readline()
#     print('vị trí',file.tell())
#     print(content_line)
   
lines = file.readlines() # Đọc tất cả các dòng trong file
print(lines)
   
# Bước 3: Đóng file lại 
file.close()

'''
Tại vì sao phải đóng file lại ?

'''