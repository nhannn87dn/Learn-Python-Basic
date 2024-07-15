person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Đếm số lượng phần tử của Dict
# print(len(person))
# # Truy cập vào một phần tử trong Dict
# print(person["name"])
# # Hoặc sử dụng get
# print(person.get("name"))
# # Trả về danh sách keys của từ điển
# print(person.keys())

# Kiểm tra sự tồn tại của một Key trong Từ điển
# if "email" in person:
#     print("Có tồn tại")
# else:
#     print("Ko tồn tại")

# Thay đổi giá trị của một key trong Dict
# person["city"] = "LosAngeles"
# print(person)

# Thêm một phần tử mới vào Dict
# person['email'] = 'jonh@gmail.com'
# print(person)
# Xóa một phần tử dựa vào key của nó
person.pop("name") # Xóa phần từ có key là name
del person["city"] # hoặc dùng del
del person # xóa luôn từ điển, từ điển sẽ không tồn tại
person.clear() # nó chỉ xóa tất cả phần tử bên trong

