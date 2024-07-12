# List và Tuple trong Python

## 1. Giới Thiệu về List và Tuple

**List** và **Tuple** là hai kiểu dữ liệu cơ bản trong Python dùng để lưu trữ các tập hợp giá trị. Chúng có một số điểm tương đồng nhưng cũng có những khác biệt quan trọng.

## 2. List

List (danh sách) là một cấu trúc dữ liệu có thể thay đổi, có thể chứa các phần tử có kiểu dữ liệu khác nhau. Các phần tử trong list được đánh chỉ số, bắt đầu từ 0.

### Tạo List
```python
# Tạo một list rỗng
my_list = []

# Tạo một list với các phần tử
my_list = [1, 2, 3, "hello", 4.5, True]

# In list
print(my_list)  # Kết quả: [1, 2, 3, "hello", 4.5, True]
```

### Truy Cập Phần Tử trong List
```python
# Truy cập phần tử qua chỉ số
print(my_list[0])  # Kết quả: 1
print(my_list[3])  # Kết quả: hello

# Truy cập phần tử từ cuối danh sách
print(my_list[-1])  # Kết quả: True
print(my_list[-2])  # Kết quả: 4.5
```

### Thay Đổi Giá Trị của Phần Tử trong List
```python
# Thay đổi giá trị của phần tử
my_list[1] = "Python"
print(my_list)  # Kết quả: [1, "Python", 3, "hello", 4.5, True]
```

### Thêm Phần Tử vào List
```python
# Thêm phần tử vào cuối danh sách
my_list.append("new item")
print(my_list)  # Kết quả: [1, "Python", 3, "hello", 4.5, True, "new item"]

# Thêm phần tử tại vị trí cụ thể
my_list.insert(1, "inserted item")
print(my_list)  # Kết quả: [1, "inserted item", "Python", 3, "hello", 4.5, True, "new item"]
```

### Xóa Phần Tử khỏi List
```python
# Xóa phần tử theo giá trị
my_list.remove("hello")
print(my_list)  # Kết quả: [1, "inserted item", "Python", 3, 4.5, True, "new item"]

# Xóa phần tử theo chỉ số
del my_list[2]
print(my_list)  # Kết quả: [1, "inserted item", 3, 4.5, True, "new item"]

# Xóa phần tử cuối cùng và trả về giá trị của nó
last_item = my_list.pop()
print(last_item)  # Kết quả: new item
print(my_list)    # Kết quả: [1, "inserted item", 3, 4.5, True]
```

### Duyệt Qua Các Phần Tử trong List
```python
# Duyệt qua các phần tử trong list
for item in my_list:
    print(item)
# Kết quả:
# 1
# inserted item
# 3
# 4.5
# True
```

## 3. Tuple

Tuple (bộ dữ liệu) là một cấu trúc dữ liệu không thể thay đổi, tức là sau khi được tạo ra, các phần tử trong tuple không thể bị thay đổi, thêm, hoặc xóa. Các phần tử trong tuple cũng được đánh chỉ số, bắt đầu từ 0.

### Tạo Tuple
```python
# Tạo một tuple rỗng
my_tuple = ()

# Tạo một tuple với các phần tử
my_tuple = (1, 2, 3, "hello", 4.5, True)

# In tuple
print(my_tuple)  # Kết quả: (1, 2, 3, "hello", 4.5, True)
```

### Truy Cập Phần Tử trong Tuple
```python
# Truy cập phần tử qua chỉ số
print(my_tuple[0])  # Kết quả: 1
print(my_tuple[3])  # Kết quả: hello

# Truy cập phần tử từ cuối danh sách
print(my_tuple[-1])  # Kết quả: True
print(my_tuple[-2])  # Kết quả: 4.5
```

### Duyệt Qua Các Phần Tử trong Tuple
```python
# Duyệt qua các phần tử trong tuple
for item in my_tuple:
    print(item)
# Kết quả:
# 1
# 2
# 3
# hello
# 4.5
# True
```

## 4. So Sánh List và Tuple

- **Khả năng thay đổi**: List có thể thay đổi (mutable) trong khi Tuple không thể thay đổi (immutable).
- **Hiệu suất**: Tuple thường nhanh hơn List vì không thể thay đổi.
- **Sử dụng**: List thường được sử dụng khi cần một tập hợp các phần tử có thể thay đổi, trong khi Tuple được sử dụng cho các tập hợp không thay đổi và đảm bảo tính toàn vẹn dữ liệu.

## 5. Kết Luận

List và Tuple là hai kiểu dữ liệu quan trọng trong Python, mỗi loại có đặc điểm và ứng dụng riêng. List có thể thay đổi và linh hoạt, trong khi Tuple không thể thay đổi và có hiệu suất cao hơn. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách sử dụng List và Tuple trong Python.