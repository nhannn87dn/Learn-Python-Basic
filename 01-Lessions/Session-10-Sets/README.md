# Set trong Python

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