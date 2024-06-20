# Dữ liệu từ Điển trong Python

## 1. Giới Thiệu về Từ Điển

**Từ điển** (dictionary) là một cấu trúc dữ liệu lưu trữ các cặp khóa-giá trị (key-value pairs). Trong từ điển, mỗi khóa là duy nhất và ánh xạ tới một giá trị. Từ điển rất hữu ích khi bạn cần truy xuất dữ liệu dựa trên một khóa cụ thể.

## 2. Tạo Từ Điển

Có nhiều cách để tạo từ điển trong Python:

### Tạo Từ Điển Rỗng
```python
my_dict = {}
```

### Tạo Từ Điển Với Các Cặp Khóa-Giá Trị
```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)
# Kết quả: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

## 3. Truy Cập Giá Trị trong Từ Điển

Bạn có thể truy cập giá trị trong từ điển bằng cách sử dụng khóa tương ứng:

```python
name = my_dict["name"]
print(name)  # Kết quả: Alice

age = my_dict.get("age")
print(age)  # Kết quả: 30
```

## 4. Thêm, Sửa, và Xóa Phần Tử trong Từ Điển

### Thêm hoặc Sửa Phần Tử
```python
# Thêm phần tử mới
my_dict["email"] = "alice@example.com"
print(my_dict)
# Kết quả: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}

# Sửa giá trị của phần tử hiện tại
my_dict["age"] = 31
print(my_dict)
# Kết quả: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}
```

### Xóa Phần Tử
```python
# Xóa phần tử bằng khóa
del my_dict["city"]
print(my_dict)
# Kết quả: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Xóa phần tử và trả về giá trị của nó
email = my_dict.pop("email")
print(email)  # Kết quả: alice@example.com
print(my_dict)
# Kết quả: {'name': 'Alice', 'age': 31}
```

### Xóa Tất Cả Phần Tử
```python
my_dict.clear()
print(my_dict)  # Kết quả: {}
```

## 5. Duyệt Qua Các Phần Tử trong Từ Điển

Bạn có thể duyệt qua các phần tử trong từ điển bằng cách sử dụng các phương thức `keys()`, `values()`, và `items()`.

### Duyệt Qua Các Khóa
```python
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

for key in my_dict.keys():
    print(key)
# Kết quả:
# name
# age
# city
```

### Duyệt Qua Các Giá Trị
```python
for value in my_dict.values():
    print(value)
# Kết quả:
# Alice
# 30
# New York
```

### Duyệt Qua Các Cặp Khóa-Giá Trị
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Kết quả:
# name: Alice
# age: 30
# city: New York
```

## 6. Kiểm Tra Sự Tồn Tại của Khóa

Bạn có thể kiểm tra xem một khóa có tồn tại trong từ điển hay không bằng cách sử dụng toán tử `in`.

```python
if "name" in my_dict:
    print("Key 'name' exists in the dictionary.")
# Kết quả: Key 'name' exists in the dictionary.

if "email" not in my_dict:
    print("Key 'email' does not exist in the dictionary.")
# Kết quả: Key 'email' does not exist in the dictionary.
```

## 7. Sao Chép Từ Điển

Bạn có thể sao chép một từ điển bằng cách sử dụng phương thức `copy()`.

```python
new_dict = my_dict.copy()
print(new_dict)
# Kết quả: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

## 8. Gộp Hai Từ Điển

Bạn có thể gộp hai từ điển lại với nhau bằng cách sử dụng phương thức `update()`.

```python
dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "email": "alice@example.com"}

dict1.update(dict2)
print(dict1)
# Kết quả: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}
```

## 9. Từ Điển Lồng Nhau

Từ điển có thể chứa các từ điển khác, tạo ra cấu trúc dữ liệu phức tạp.

```python
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

print(nested_dict)
# Kết quả: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}
```

## 10. Kết Luận

Từ điển là một cấu trúc dữ liệu mạnh mẽ và linh hoạt trong Python, cho phép bạn lưu trữ và truy xuất dữ liệu một cách hiệu quả bằng cách sử dụng các cặp khóa-giá trị. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách sử dụng từ điển trong Python.