myProfile = {
    "firstName": 'Nguyễn',
    "lastName": 'Nhân',
    "email": 'nhannn@softech.vn',
    "age": 38,
    "isTeacher": True,
    "myList": [1,2,3,4,5]
}

for k in myProfile:
    print('k', k, myProfile[k])


# myProfile["age"] = 18
# myProfile.update({"isTeacher": False})
# myProfile["isTeacher"] =False

# them phan tu vao
#myProfile['mobile'] = '0988777666'

#myProfile.pop('myList')
#del myProfile
# myProfile.clear()

# print(myProfile)


# if "mobile" in myProfile:
#     print('Ton tai')

#print(len(myProfile))

# Truy cập vào các phần tử trong Dict
# print(myProfile['email'])
# print(myProfile.get('email'))

#print(myProfile.items())

# Câu 1: Hãy định nghĩa 1 dict: thể hiện các thông tin
# - Tên của mình
# - Trường của mình
# - Tên lớp của mình
# - Tuổi của mình
# Yêu cầu in ra: "Tôi tên là xxx, tôi học trường yyy, lớp zzz. Năm nay tôi www tuổi"

# Câu 2: Từ biến dict đã tạo ở câu 1. 
# - hãy thay đổi giá trị lớp thành: "12B",và tuổi thành: 8
# - Thêm phần tử: weight: 30
# - In ra dict, để kiểm tra sự thay đổi


# Câu 3: in danh sách các giá trị của dict ở câu 1