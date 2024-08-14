# Review Lesions 7 - 11

Dưới đây là bảng so sánh giữa `list`, `tuple`, `set`, và `dict` trong Python:

| Đặc điểm          | List                        | Tuple                       | Set                            | Dict                          |
| ----------------- | --------------------------- | --------------------------- | ------------------------------ | ----------------------------- |
| Khả năng thay đổi | Có thể thay đổi             | Không thể thay đổi          | Có thể thay đổi                | Có thể thay đổi               |
| Thứ tự            | Có thứ tự                   | Có thứ tự                   | Không có thứ tự                | Có thứ tự (từ Python 3.7)     |
| Phần tử trùng lặp | Cho phép                    | Cho phép                    | Không cho phép                 | Khóa không cho phép trùng lặp |
| Cú pháp           | `[1, 2, 3]`                 | `(1, 2, 3)`                 | `{1, 2, 3}`                    | `{'a': 1, 'b': 2}`            |
| Truy cập          | Chỉ số                      | Chỉ số                      | Không thể truy cập bằng chỉ số | Khóa                          |
| Tốc độ            | Chậm hơn tuple cho truy cập | Nhanh hơn list cho truy cập | Nhanh cho phép toán tập hợp    | Nhanh cho truy cập bằng khóa  |

### Chi tiết thêm:

- **List**: Có thể thay đổi, cho phép trùng lặp, lý tưởng cho các thao tác cần thay đổi dữ liệu.
- **Tuple**: Không thể thay đổi, cho phép trùng lặp, dùng cho dữ liệu cố định.
- **Set**: Không có thứ tự, không cho phép trùng lặp, lý tưởng cho phép toán tập hợp, loại bỏ phần tử trùng lặp.
- **Dict**: Lưu trữ cặp khóa-giá trị, nhanh cho truy cập dữ liệu qua khóa, không cho phép trùng lặp khóa.

---

## Bài 7 - OOPs

Lập trình hướng đối tượng

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

Yêu cầu:

- in ra: "Sách học Python cơ bản có giá 125.2$"
- Thay thế "Python" thành "Scratch" và in ra title
- Kiểm tra xem title có bắt đầu bằng "Sách" không, in ra kết quả kiểm tra

---

## Bài 10 - Dictionaries

1. Tạo một từ điển student chứa các thông tin sau

```python
ten: "Nguyen Van A"
tuoi: 20
lop: "CNTT"
```

2. Thêm một phần tử mới vào từ điển student với khóa là `email` và giá trị là "nguyenvana@example.com"

3. Cập nhật giá trị của khóa tuổi thành 21

4. Xóa phần tử có khóa lớp khỏi từ điển.

5. Duyệt qua tất cả các phần tử trong từ điển và in ra theo định dạng: "Khóa: Giá trị".

---

## Bài 11 - Sets và Exception Handling

Tạo một Sets gồm 5 số nguyên từ 2 giá trị nhập từ người dùng `start` và `stop`

- Nếu người dùng nhập vào kí tự là chữ: In ra báo lỗi
- In ra từng giá trị của Sets vừa tạo trên
