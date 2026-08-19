def ten_fun():
    print('hello func')
# gọi hàm
ten_fun()

## Hàm có return
def sum(a,b):
    return a + b


def tinhTien(sl, dongia):
    thanhtien = sl*dongia
    if(sl > 5):
        thanhtien = thanhtien - 1000
    print('Tong tien can thanh toan: ', thanhtien)

q= int(input('So luong can mua: '))
tinhTien(q, 5000)

