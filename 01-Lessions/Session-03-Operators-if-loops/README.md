# Buổi 3: Luồng điều khiển và Vòng lặp


Chắc chắn rồi! Dưới đây là bài giảng về các toán tử so sánh, toán tử logic, câu lệnh `if` và biến thể, cũng như các vòng lặp trong Python, kèm theo các ví dụ minh họa.

## Toán tử So sánh

Toán tử so sánh được sử dụng để so sánh hai giá trị và trả về giá trị Boolean (`True` hoặc `False`).

### Các Toán tử So sánh:

1. **Bằng nhau (`==`)**: Kiểm tra hai giá trị có bằng nhau hay không.
2. **Khác nhau (`!=`)**: Kiểm tra hai giá trị có khác nhau hay không.
3. **Lớn hơn (`>`)**: Kiểm tra giá trị bên trái có lớn hơn giá trị bên phải hay không.
4. **Lớn hơn hoặc bằng (`>=`)**: Kiểm tra giá trị bên trái có lớn hơn hoặc bằng giá trị bên phải hay không.
5. **Nhỏ hơn (`<`)**: Kiểm tra giá trị bên trái có nhỏ hơn giá trị bên phải hay không.
6. **Nhỏ hơn hoặc bằng (`<=`)**: Kiểm tra giá trị bên trái có nhỏ hơn hoặc bằng giá trị bên phải hay không.

### Ví dụ:

```python
a = 10
b = 5

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a >= b)  # Output: True
print(a < b)   # Output: False
print(a <= b)  # Output: False
```

## Toán tử Logic

Toán tử logic được sử dụng để kết hợp các biểu thức điều kiện và trả về giá trị Boolean.

### Các Toán tử Logic:

1. **Và (`and`)**: Trả về `True` nếu cả hai biểu thức đều `True`.
2. **Hoặc (`or`)**: Trả về `True` nếu ít nhất một trong hai biểu thức là `True`.
3. **Không (`not`)**: Đảo ngược giá trị Boolean của biểu thức.

### Ví dụ

```python
x = True
y = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
```

## Câu lệnh `if` và Biến thể

Câu lệnh điều kiện `if` được sử dụng để thực thi một khối mã nếu điều kiện cho trước là `True`.

### Cấu trúc Câu lệnh `if`

```python
if điều_kiện:
    # Mã được thực thi nếu điều_kiện là True
```

### Cấu trúc Câu lệnh `if-else`

```python
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```

### Cấu trúc Câu lệnh `if-elif-else`

```python
if điều_kiện_1:
    # Mã được thực thi nếu điều_kiện_1 là True
elif điều_kiện_2:
    # Mã được thực thi nếu điều_kiện_2 là True
else:
    # Mã được thực thi nếu không có điều_kiện nào đúng
```

### Ví dụ

```python
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are an adult.")
```
