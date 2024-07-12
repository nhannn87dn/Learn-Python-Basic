# Sets và Exception Handling trong Python


## 1. Giới Thiệu về Set

**Set** là một cấu trúc dữ liệu trong Python giống như một danh sách (list) hoặc từ điển (dictionary), nhưng có một số tính chất đặc biệt:

- Các phần tử trong set là duy nhất, tức là không có phần tử trùng lặp.
- Set không có thứ tự, tức là các phần tử trong set không có chỉ số.
- Set có thể chứa các loại dữ liệu khác nhau nhưng các phần tử phải là kiểu dữ liệu không thay đổi (immutable) như số, chuỗi, tuple.

## 2. Tạo Set

### Tạo Set Rỗng
```python
my_set = set()
```

### Tạo Set Với Các Phần Tử
```python
my_set = {1, 2, 3, "hello", 4.5}
print(my_set)
# Kết quả có thể khác nhau do set không có thứ tự, ví dụ: {1, 2, 3, 'hello', 4.5}
```

## 3. Thao Tác với Set

### Thêm Phần Tử Vào Set
Bạn có thể sử dụng phương thức `add()` để thêm một phần tử vào set.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Kết quả: {1, 2, 3, 4}
```

### Thêm Nhiều Phần Tử Vào Set
Bạn có thể sử dụng phương thức `update()` để thêm nhiều phần tử vào set.

```python
my_set.update([5, 6, 7])
print(my_set)
# Kết quả: {1, 2, 3, 4, 5, 6, 7}
```

### Xóa Phần Tử Khỏi Set
Bạn có thể sử dụng phương thức `remove()` hoặc `discard()` để xóa một phần tử khỏi set.

```python
my_set.remove(4)
print(my_set)
# Kết quả: {1, 2, 3, 5, 6, 7}

# Sử dụng discard() không gây lỗi nếu phần tử không tồn tại
my_set.discard(10)
print(my_set)
# Kết quả: {1, 2, 3, 5, 6, 7}
```

### Xóa Phần Tử Ngẫu Nhiên và Trả Về Phần Tử Đó
Bạn có thể sử dụng phương thức `pop()` để xóa và trả về một phần tử ngẫu nhiên trong set.

```python
popped_element = my_set.pop()
print(popped_element)
print(my_set)
# Kết quả: (phần tử ngẫu nhiên sẽ bị xóa)
```

### Xóa Tất Cả Các Phần Tử Trong Set
Bạn có thể sử dụng phương thức `clear()` để xóa tất cả các phần tử trong set.

```python
my_set.clear()
print(my_set)
# Kết quả: set()
```

## 4. Các Phép Toán Trên Set

### Phép Hợp (Union)
Bạn có thể sử dụng toán tử `|` hoặc phương thức `union()` để lấy hợp của hai set.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)
# Kết quả: {1, 2, 3, 4, 5}

union_set = set1.union(set2)
print(union_set)
# Kết quả: {1, 2, 3, 4, 5}
```

### Phép Giao (Intersection)
Bạn có thể sử dụng toán tử `&` hoặc phương thức `intersection()` để lấy giao của hai set.

```python
intersection_set = set1 & set2
print(intersection_set)
# Kết quả: {3}

intersection_set = set1.intersection(set2)
print(intersection_set)
# Kết quả: {3}
```

### Phép Hiệu (Difference)
Bạn có thể sử dụng toán tử `-` hoặc phương thức `difference()` để lấy hiệu của hai set.

```python
difference_set = set1 - set2
print(difference_set)
# Kết quả: {1, 2}

difference_set = set1.difference(set2)
print(difference_set)
# Kết quả: {1, 2}
```

### Phép Hiệu Đối Xứng (Symmetric Difference)
Bạn có thể sử dụng toán tử `^` hoặc phương thức `symmetric_difference()` để lấy hiệu đối xứng của hai set.

```python
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)
# Kết quả: {1, 2, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)
# Kết quả: {1, 2, 4, 5}
```

## 5. Kiểm Tra Thành Phần Trong Set

Bạn có thể kiểm tra xem một phần tử có tồn tại trong set hay không bằng toán tử `in`.

```python
if 2 in set1:
    print("2 exists in set1")
# Kết quả: 2 exists in set1

if 10 not in set1:
    print("10 does not exist in set1")
# Kết quả: 10 does not exist in set1
```

## 6. Các Phương Thức Khác của Set

### Đếm Số Phần Tử Trong Set
Bạn có thể sử dụng hàm `len()` để đếm số phần tử trong set.

```python
print(len(set1))
# Kết quả: 3
```

### Sao Chép Set
Bạn có thể sử dụng phương thức `copy()` để sao chép một set.

```python
set_copy = set1.copy()
print(set_copy)
# Kết quả: {1, 2, 3}
```

## 7. Kết Luận

Set là một cấu trúc dữ liệu mạnh mẽ và linh hoạt trong Python, cho phép bạn lưu trữ các phần tử duy nhất và thực hiện các phép toán tập hợp một cách dễ dàng. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách sử dụng set trong Python.

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