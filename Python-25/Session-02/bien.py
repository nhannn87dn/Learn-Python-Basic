#code ở trong file này
#print('hello Nhat')
#1. Cách khai báo biến
name = 'Nhân'; # giá trị kiểu chuỗi (chữ) str = string
age = 38; # 38 là giá trị kiểu số (integer - int)
#2. Làm sao để kiểm tra giá trị của biến ?
print(name); # in ra giá trị biến name
#3. Làm sao biết được biến có kiểu gì liệu gì ?
print(type(name)); #sử dụng hàm type() --> str = string
#4. Bài tập nhỏ ?
# 4.1 Đặt một biến bằng tên của mình và in ra.
# 4.2 Đặt một biến bằng tuổi của mình và in ra.
# 4.3 Đặt một biến bằng Tên trường mình học và in ra.
school_name = 'Lê Độ'
print(school_name)
# 68abc = 'abc' sai quy tắc
# break = 123; sử dụng từ khóa python --> sai
my_variable_name = "John"
print(my_variable_name)
MyVariableName = "John 2"
print(MyVariableName)
myVariableName = "John"
print(myVariableName)

#5. Có thể gán nhiều giá trị cho nhiều biến cùng lúc
x, y = 1, 2;
# Tương đương
'''
x = 1
y = 2
'''
print('x', x)
print('y', y)

#6. Gán nhiều biến cùng 1 giá trị
i = j = 'orange';
print('i', i)
isTeacher = True; #bool = boolean