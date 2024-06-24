# Exception Handling trong Python

## 1. Giới Thiệu về Exception Handling

**Exception Handling** (xử lý ngoại lệ) là một kỹ thuật lập trình dùng để quản lý các lỗi hoặc tình huống bất ngờ xảy ra trong quá trình thực thi chương trình. Python cung cấp cơ chế mạnh mẽ để bắt và xử lý các ngoại lệ, giúp chương trình không bị dừng đột ngột và cho phép thực hiện các hành động thích hợp khi gặp lỗi.

## 2. Các Khái Niệm Cơ Bản

### Ngoại Lệ (Exception)

Ngoại lệ là một sự kiện xảy ra trong quá trình thực thi chương trình và làm gián đoạn dòng chảy bình thường của lệnh. Khi một ngoại lệ xảy ra, Python sẽ dừng chương trình và tìm cách xử lý ngoại lệ này.

### Các Loại Ngoại Lệ Thường Gặp

- `ZeroDivisionError`: Lỗi chia cho số 0.
- `IndexError`: Lỗi truy cập chỉ mục không hợp lệ trong danh sách.
- `KeyError`: Lỗi truy cập khóa không tồn tại trong từ điển.
- `FileNotFoundError`: Lỗi không tìm thấy tệp tin.
- `ValueError`: Lỗi giá trị không hợp lệ.

## 3. Cấu Trúc Try-Except

Cấu trúc try-except dùng để bắt và xử lý ngoại lệ.

```python
try:
    # Khối lệnh có thể gây ra ngoại lệ
    result = 10 / 0
except ZeroDivisionError:
    # Khối lệnh xử lý ngoại lệ
    print("Không thể chia cho số 0.")
```

### Ví Dụ

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho số 0.")
# Kết quả: Không thể chia cho số 0.
```

## 4. Cấu Trúc Try-Except-Else

Khối `else` được thực thi khi không có ngoại lệ xảy ra trong khối `try`.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Không thể chia cho số 0.")
else:
    print(f"Kết quả là: {result}")
# Kết quả: Kết quả là: 5.0
```

## 5. Cấu Trúc Try-Except-Finally

Khối `finally` luôn được thực thi dù có hay không có ngoại lệ xảy ra. Khối này thường dùng để giải phóng tài nguyên hoặc thực hiện các công việc dọn dẹp.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Không thể chia cho số 0.")
else:
    print(f"Kết quả là: {result}")
finally:
    print("Khối finally luôn được thực thi.")
# Kết quả:
# Kết quả là: 5.0
# Khối finally luôn được thực thi.
```

## 6. Nâng Cao: Bắt Nhiều Loại Ngoại Lệ

Bạn có thể bắt nhiều loại ngoại lệ bằng cách sử dụng nhiều khối `except`.

```python
try:
    # Một số thao tác có thể gây ra ngoại lệ
    result = 10 / 0
    number = int("not a number")
except ZeroDivisionError:
    print("Không thể chia cho số 0.")
except ValueError:
    print("Không thể chuyển đổi chuỗi thành số nguyên.")
```

### Ví Dụ

```python
try:
    number = int("not a number")
except ZeroDivisionError:
    print("Không thể chia cho số 0.")
except ValueError:
    print("Không thể chuyển đổi chuỗi thành số nguyên.")
# Kết quả: Không thể chuyển đổi chuỗi thành số nguyên.
```

## 7. Tự Định Nghĩa Ngoại Lệ

Bạn có thể tự định nghĩa các ngoại lệ riêng bằng cách kế thừa từ lớp `Exception`.

```python
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Đây là ngoại lệ tự định nghĩa.")
except MyCustomError as e:
    print(e)
# Kết quả: Đây là ngoại lệ tự định nghĩa.
```

## 8. Các Thực Hành Tốt Khi Xử Lý Ngoại Lệ

- **Cụ thể hóa ngoại lệ**: Luôn bắt các ngoại lệ cụ thể thay vì dùng `except` tổng quát để tránh bỏ qua các lỗi không mong muốn.
- **Dọn dẹp tài nguyên**: Sử dụng khối `finally` hoặc câu lệnh `with` để đảm bảo tài nguyên luôn được dọn dẹp.
- **Thông báo lỗi**: Cung cấp thông tin hữu ích về lỗi để dễ dàng gỡ lỗi và bảo trì.

### Ví Dụ Về Dọn Dẹp Tài Nguyên

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Không tìm thấy tệp tin.")
finally:
    file.close()
```

Hoặc sử dụng câu lệnh `with` để tự động dọn dẹp tài nguyên:

```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Không tìm thấy tệp tin.")
```

## 9. Kết Luận

Exception handling là một phần quan trọng trong lập trình, giúp bạn quản lý và xử lý các tình huống lỗi một cách hiệu quả. Bằng cách sử dụng các cấu trúc try-except, bạn có thể đảm bảo chương trình của mình hoạt động ổn định và dễ bảo trì. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách xử lý ngoại lệ trong Python.