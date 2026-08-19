student = {
    "first_name": "Nguyen",
    "last_name": "Van A",
    "email": "nguyenvana@example.com",
    "gender": 'male',
    #"age": 18,
    "age": 30
}
print(student)

# Phương len()
print(len(student))

# Truy cập đến giá trị phần tử
print(student['email'])
# hoặc sử dụng phương thức get
print(student.get('gender'))

# In ra danh sách keys của từ điển
print(student.keys())
# in ra tất cả values của dict
print(student.values())
# in ra từng cặp khoá trị
print(student.items())

# Kiểm sự tồn tại của phần từ trong dic
if 'ages' in student:
    print('Có tồn tại')
else:
    print('ko tồn tại')

# Cập nhật giá trị của phần tử trong dict
student["age"] = 18
student.update({'gender': 'female'})
print(student)

# Thêm một phần từ mới vào dict
student['mobile'] = '0988000000'
print(student)

# Xoá phần từ trong dict


# Dùng vòng lặp với dict
for i in student:
    print(i, student[i])