loai_ve = input("Chọn loại vé cần mua: ")
# nguoi_lon: Người lớn
# tre_em: Trẻ em
# cao_tuoi: Cao tuổi
sl_ve = int(input("Nhập số lượng vé: "))


if loai_ve == 'nguoi_lon':
    price = 100
elif loai_ve == 'cao_tuoi':
    price = 80
else:
    price = 70 # còn lại loại vé trẻ em
    
# Tính giảm giá dựa vào số lượng
if sl_ve >= 5:
    discount = 10
elif sl_ve >= 10:
    discount  = 20
else:
    discount = 0

# Tính thành tiên
thanh_tien = (sl_ve * price) - (sl_ve * price) * discount / 100
print("Loại vé: ", loai_ve)
print("Đơn giá: ",price)
print("Thành tiền: ",thanh_tien)
print("Chiết khấu: ",discount)