#  Chuỗi trong Python

Xem thêm: https://www.w3schools.com/python/python_strings.asp

## 1. Giới Thiệu về Chuỗi

**Chuỗi** (string) là một dãy các ký tự được đặt trong dấu nháy đơn, nháy kép, hoặc nháy ba (để viết chuỗi nhiều dòng). Chuỗi là một kiểu dữ liệu quan trọng và được sử dụng rộng rãi trong Python.

## 2. Tạo Chuỗi

Có nhiều cách để tạo chuỗi trong Python:

```python
# Sử dụng dấu nháy đơn
single_quote_str = 'Hello, world!'

# Sử dụng dấu nháy kép
double_quote_str = "Hello, world!"

# Sử dụng dấu nháy ba (để viết chuỗi nhiều dòng)
triple_quote_str = """This is a
multi-line string."""

print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)
```

## 3. Truy Cập Phần Tử của Chuỗi

Chuỗi trong Python là một dãy các ký tự, và bạn có thể truy cập từng ký tự thông qua chỉ số (index):

```python
s = "Hello, world!"
print(s[0])   # Kết quả: H
print(s[7])   # Kết quả: w
print(s[-1])  # Kết quả: !
```

## 4. Các Phép Toán trên Chuỗi

### Nối Chuỗi

Bạn có thể nối chuỗi bằng cách sử dụng toán tử `+`:

```python
s1 = "Hello"
s2 = "world"
s3 = s1 + ", " + s2 + "!"
print(s3)  # Kết quả: Hello, world!
```

### Lặp Chuỗi

Bạn có thể lặp lại chuỗi bằng cách sử dụng toán tử `*`:

```python
s = "Hello"
print(s * 3)  # Kết quả: HelloHelloHello
```

### Kiểm Tra Thành Phần

Bạn có thể kiểm tra xem một chuỗi con có nằm trong một chuỗi khác hay không bằng toán tử `in`:

```python
s = "Hello, world!"
print("world" in s)    # Kết quả: True
print("Python" in s)   # Kết quả: False
```

## 5. Các Hàm và Phương Thức của Chuỗi

### Độ Dài Chuỗi

Hàm `len()` trả về độ dài của chuỗi:

```python
s = "Hello, world!"
print(len(s))  # Kết quả: 13
```

### Chuyển Đổi Ký Tự

Các phương thức `upper()`, `lower()`, `capitalize()`, `title()` giúp chuyển đổi ký tự trong chuỗi:

```python
s = "hello, world!"
print(s.upper())       # Kết quả: HELLO, WORLD!
print(s.lower())       # Kết quả: hello, world!
print(s.capitalize())  # Kết quả: Hello, world!
print(s.title())       # Kết quả: Hello, World!
```

### Loại Bỏ Khoảng Trắng

Các phương thức `strip()`, `lstrip()`, `rstrip()` giúp loại bỏ khoảng trắng ở đầu và cuối chuỗi:

```python
s = "   Hello, world!   "
print(s.strip())   # Kết quả: Hello, world!
print(s.lstrip())  # Kết quả: Hello, world!   
print(s.rstrip())  # Kết quả:    Hello, world!
```

### Thay Thế Ký Tự

Phương thức `replace()` giúp thay thế ký tự trong chuỗi:

```python
s = "Hello, world!"
print(s.replace("world", "Python"))  # Kết quả: Hello, Python!
```

### Tách và Nối Chuỗi

Phương thức `split()` tách chuỗi thành danh sách các chuỗi con, và `join()` nối các phần tử của danh sách thành một chuỗi:

```python
s = "Hello, world!"
words = s.split(", ")
print(words)  # Kết quả: ['Hello', 'world!']

s2 = " ".join(words)
print(s2)  # Kết quả: Hello world!
```

## 6. Định Dạng Chuỗi

Python cung cấp nhiều cách để định dạng chuỗi:

### Định Dạng Bằng Cách Sử Dụng `%`

```python
name = "Alice"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# Kết quả: My name is Alice and I am 30 years old.
```

### Định Dạng Bằng `str.format()`

```python
print("My name is {} and I am {} years old.".format(name, age))
# Kết quả: My name is Alice and I am 30 years old.
```

### Định Dạng Bằng F-String (Python 3.6+)

```python
print(f"My name is {name} and I am {age} years old.")
# Kết quả: My name is Alice and I am 30 years old.
```

## 7. Kết Luận

Chuỗi là một kiểu dữ liệu quan trọng và linh hoạt trong Python, cung cấp nhiều phương thức và phép toán để thao tác và xử lý dữ liệu văn bản. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách làm việc với chuỗi trong Python.