tu_dien = {} # từ điển rỗng chưa có phần tử nào

profile = {
    "name": "ngoc Nhan",
    "age": 36,
    "color": "skyblue",
    "isTeacher": True,
    "address": {
        "street": "38 yen bai",
        "city": "da nang",
        "country": "viet nam"
    }
}
'''
name, age, color = là các key (keywords)
phần sau dấu : là giá trị 
'''

# Truy cập phần tử trong từ điển
#print(profile['color'])
#print(profile.get('color'))

# Ko cho trùng lặp key
#print(profile)

# Thay đổi giá trị của một phần tử trong từ điển
#profile["color"] = 'green' # gán lại giá trị mới cho key color
#print(profile)

# hoăc
# profile.update({"color": "green"})
# print(profile)

# Thêm mới một phần tử chưa có vào từ điển
profile['email'] = 'nhan@gmail.com'
print(profile)

# Đếm số lượng phần tử của tử điển
#print(len(profile))

# Lấy danh sách các keys của từ điển
#print(profile.keys())

# Lấy danh sách các values của từ điển
#print(profile.values())

# Lấy từng phần tử của từ điển
# print(profile.items())

# Kiểm một key có tồn tại trong từ điển không
# if "email" in profile:
#     print('Có tồn tại')
# else:
#     print('Ko tồn tại')

# Xóa một phần tử trong từ điển
# del profile["isTeacher"]
# print(profile)

# Lặp qua các phần tử của từ điển với for loop
# Trả về key trong mỗi lần lặp

for k in profile:
    print(k,profile[k])
    