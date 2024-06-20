# Buổi 2: Biến trong Python

Trong buổi học này, chúng ta sẽ tìm hiểu về cú pháp cơ bản của Python, cách làm việc với biến và kiểu dữ liệu, và thực hiện các phép toán số học. Điều này sẽ giúp bạn hiểu rõ hơn về cách sử dụng Python để thực hiện các tác vụ cơ bản trong lập trình.


Chắc chắn rồi! Dưới đây là bài giảng về biến và kiểu dữ liệu của biến trong Python, kèm theo các ví dụ minh họa.

## Biến trong Python

### Định nghĩa Biến

Biến là tên được sử dụng để lưu trữ giá trị trong bộ nhớ của máy tính. Khi khai báo một biến, bạn có thể gán một giá trị cho biến đó.

### Cú pháp Khai báo Biến

```python
variable_name = value
```

- `variable_name`: Tên biến, phải tuân theo quy tắc đặt tên biến (bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`, không chứa khoảng trắng và không trùng với từ khóa của Python).
- `value`: Giá trị bạn muốn gán cho biến.

### Ví dụ Khai báo Biến

```python
name = "Alice"
age = 30
height = 1.75
is_student = True
```

## Kiểu Dữ liệu của Biến

Python có nhiều kiểu dữ liệu khác nhau để biểu diễn các loại thông tin khác nhau. Dưới đây là các kiểu dữ liệu cơ bản trong Python, kèm theo ví dụ.

### 1. Kiểu Dữ liệu Số (Numeric Types)

#### a. Số nguyên (int)

Là các số nguyên, không có phần thập phân.

```python
x = 10
y = -5
```

#### b. Số thực (float)

Là các số có phần thập phân.

```python
pi = 3.14
e = 2.718
```

#### c. Số phức (complex)

Là các số có phần thực và phần ảo.

```python
z = 1 + 2j
```

### 2. Kiểu Dữ liệu Chuỗi (String)

Là các dãy ký tự, thường được đặt trong dấu nháy đơn hoặc nháy kép.

```python
greeting = "Hello, world!"
name = 'Alice'
```

Chú ý: Chuỗi trong Python là bất biến (immutable), tức là không thể thay đổi sau khi đã tạo ra.

### 3. Kiểu Dữ liệu Boolean

Chỉ có hai giá trị: `True` và `False`.

```python
is_raining = False
is_sunny = True
```

### 4. Kiểu Dữ liệu Danh sách (List)

Là một dãy các giá trị có thể thay đổi (mutable), được đặt trong cặp dấu ngoặc vuông `[]`.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
```

### 5. Kiểu Dữ liệu Bộ (Tuple)

Là một dãy các giá trị không thể thay đổi (immutable), được đặt trong cặp dấu ngoặc đơn `()`.

```python
coordinates = (10.0, 20.0)
colors = ("red", "green", "blue")
```

### 6. Kiểu Dữ liệu Tập hợp (Set)

Là một tập hợp các giá trị duy nhất, không thứ tự, được đặt trong cặp dấu ngoặc nhọn `{}`.

```python
unique_numbers = {1, 2, 3, 4, 5}
unique_fruits = {"apple", "banana", "cherry"}
```

### 7. Kiểu Dữ liệu Từ điển (Dictionary)

Là một tập hợp các cặp khóa-giá trị, được đặt trong cặp dấu ngoặc nhọn `{}`.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
```

## Kiểm tra Kiểu Dữ liệu của Biến

Bạn có thể sử dụng hàm `type()` để kiểm tra kiểu dữ liệu của một biến.

### Ví dụ

```python
x = 10
print(type(x))  # Output: <class 'int'>

pi = 3.14
print(type(pi))  # Output: <class 'float'>

name = "Alice"
print(type(name))  # Output: <class 'str'>

is_student = True
print(type(is_student))  # Output: <class 'bool'>

fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>

coordinates = (10.0, 20.0)
print(type(coordinates))  # Output: <class 'tuple'>

unique_fruits = {"apple", "banana", "cherry"}
print(type(unique_fruits))  # Output: <class 'set'>

person = {"name": "Alice", "age": 30, "city": "New York"}
print(type(person))  #

```

---

## Toán tử Số học trong Python

Toán tử số học là những ký hiệu được sử dụng để thực hiện các phép toán cơ bản như cộng, trừ, nhân, chia, v.v. Dưới đây là danh sách các toán tử số học cơ bản trong Python:

1. **Cộng (+)**
2. **Trừ (-)**
3. **Nhân (*)**
4. **Chia (/)**
5. **Chia lấy phần nguyên (//)**
6. **Lấy phần dư (%)**
7. **Lũy thừa (**)**

### 1. Toán tử Cộng (+)

Phép cộng hai số.

#### Ví dụ:

```python
a = 10
b = 5
result = a + b
print(result)  # Output: 15
```

### 2. Toán tử Trừ (-)

Phép trừ hai số.

#### Ví dụ:

```python
a = 10
b = 5
result = a - b
print(result)  # Output: 5
```

### 3. Toán tử Nhân (*)

Phép nhân hai số.

#### Ví dụ:

```python
a = 10
b = 5
result = a * b
print(result)  # Output: 50
```

### 4. Toán tử Chia (/)

Phép chia hai số, kết quả là số thực.

#### Ví dụ:

```python
a = 10
b = 4
result = a / b
print(result)  # Output: 2.5
```

### 5. Toán tử Chia lấy phần nguyên (//)

Phép chia hai số, kết quả là phần nguyên của phép chia.

#### Ví dụ:

```python
a = 10
b = 4
result = a // b
print(result)  # Output: 2
```

### 6. Toán tử Lấy phần dư (%)

Phép chia lấy phần dư của hai số.

#### Ví dụ:

```python
a = 10
b = 4
result = a % b
print(result)  # Output: 2
```

### 7. Toán tử Lũy thừa (**)

Phép lấy lũy thừa của một số.

#### Ví dụ:

```python
a = 2
b = 3
result = a ** b
print(result)  # Output: 8
```

## Các Ví dụ Tổng hợp

Dưới đây là một số ví dụ tổng hợp về việc sử dụng các toán tử số học trong Python.

### Ví dụ 1: Tính toán đơn giản

```python
x = 15
y = 4

# Cộng
print("x + y =", x + y)  # Output: x + y = 19

# Trừ
print("x - y =", x - y)  # Output: x - y = 11

# Nhân
print("x * y =", x * y)  # Output: x * y = 60

# Chia
print("x / y =", x / y)  # Output: x / y = 3.75

# Chia lấy phần nguyên
print("x // y =", x // y)  # Output: x // y = 3

# Lấy phần dư
print("x % y =", x % y)  # Output: x % y = 3

# Lũy thừa
print("x ** y =", x ** y)  # Output: x ** y = 50625
```

### Ví dụ 2: Tính toán với biến và kết hợp toán tử

```python
a = 7
b = 3

# Kết hợp các toán tử
result = (a + b) * (a - b)
print("(a + b) * (a - b) =", result)  # Output: (a + b) * (a - b) = 40

# Tính toán phức tạp hơn
result = a ** 2 + b ** 2 - 2 * a * b
print("a^2 + b^2 - 2ab =", result)  # Output: a^2 + b^2 - 2ab = 16
```
