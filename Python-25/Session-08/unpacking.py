fruits = ("apple", "banana", "cherry")
print(fruits[0], fruits[1], fruits[2])
# Ngoài cách dựa vào index để lấy giá trị
# thì còn có cách khác --> dùng Unpack
(tao, chuoi, cheri) = fruits
# tao --> apple
# chuoi --> banana
# cheri --> cherry
print(tao, chuoi,cheri)

# Áp dụng cho bài lúc nảy
# Câu 5: Sử dụng unpacking để lấy ra tên của 5 bạn.

friends = ('Ti', 'Teo', 'Tun', 'Bi', 'Bo')
for f in friends:
    print(f)
# (ti, te, tu, *bb) = friends
# print([ti, te], [tu], bb)
# (mot, hai, ba, bon, nam) = friends
# print(mot, hai, ba, bon, nam)
# Chỉ in Teo
# (_, t, *_) = friends
# print('t',t)
# Chỉ in ra tên của bạn thứ 4.

# Câu 6: Phân rã với *
# (t,*nhom) = friends
# print('t',t)
# print('nhom',nhom)

group1 = ('Ti', 'Teo')
group2 = ('Tun', 'Bi', 'Bo')

#  Làm sao gộp 2 tuple trên thành 1
# Cách 1: Sử dụng toán tử cộng +
g = group1 + group2
print('g', g)
# Nhân bản với toán tử *
n = group1 * 2
print(n)