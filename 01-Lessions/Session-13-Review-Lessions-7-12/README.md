# Review Lessions 7 - 12

## Bài 5 - Ôn về Hàm và Module

1. Định nghĩa một hàm sayHello:

- Nếu gọi sayHello("Tuấn") thì in ra: "Xin chào, Tuấn"
- Nếu gọi sayHello("Đức") thì in ra: "Xin chào, Đức"

---

2. Định nghĩa một hàm nhận vào 3 tham số `x`,`y`và `phep_tinh`

- x và y: là 2 số nguyên
- `phep_tinh`: có các giá trị: 'cong', 'tru', 'nhan', 'chia'. Mặc định là 'cong'

Yêu cầu tính và in ra kết quả:

- Khi 2 số là 5, 2.
- Khi 2 số là 10, 5 với `phep_tinh` là 'nhan'

---

3. Siêu thị mega có chương trình ưu đãi giảm giá cho thành viên VIP và GOLD khi có hóa đơn mua hàng trên 2 triệu. Thệ lệ chương trình:

- Nếu khách hàng là VIP thì giảm 10%
- Nếu khách hàng là GOLD thì giảm 7%
- Nếu khách hàng là MEMBER thì giảm 0%

Tính và in ra kết quả mức giảm giá của khách hàng:

- Nguyễn Văn A. Hạng VIP, có đơn hàng 5 triệu
- Nguyễn Văn B. Hạng GOLD, có đơn hàng 2.5 triệu
- Nguyễn Văn C. Hạng VIP, có đơn hàng 1.5 triệu

--

## Bài 8 - List và Tuple

1. Cho một list như sau:

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

```

- In ra một list gồm 2 phần từ "cherry", "orange"
- In ra giá trị của từng phần tử trong phần list đã cho nói trên.
- Xóa "kiwi" và in ra list sau khi đã xóa.
- Bổ sung vào list trên một phần tử mới "pear" và in ra list.

2. Cho một tuple như sau:

```python
tup_fruits = (1, "banana", "cherry", 2, 7)
```

- Thay đổi giá trị phần tử "banana" thành "kiwi"
- Thêm vào tuple trên một phần từ mới "True"
- Tính tổng các phần tử là số trong Tuple nói trên

---

## Bài 9 - String

1. Cho một một biến `email` bằng giá trị nhập từ người dùng

- Kiểm tra Nếu không có chứa kí tự `@` thì in ra là: "Email không hợp lệ"
- Còn lại là: "Email đã hợp lệ"

2. Cho 2 biến như sau:

```python
title = "Sách học Python cơ bản"
price = 125.234
```

Yêu cầu in ra: "Sách học Python cơ bản có giá 125.2$"
