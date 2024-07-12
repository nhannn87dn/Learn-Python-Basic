# Module và Function Python

## Module

### 1. Giới Thiệu về Module

**Module** trong Python là một tệp chứa mã Python, có thể bao gồm các định nghĩa hàm, lớp, biến, và cả các đoạn mã thực thi. Module giúp tổ chức và quản lý mã nguồn một cách hiệu quả hơn, đặc biệt là trong các dự án lớn.

### 2. Sử Dụng Module Dựng Sẵn

Python cung cấp một số lượng lớn các module dựng sẵn trong thư viện tiêu chuẩn của nó. Dưới đây là một số module phổ biến:

- `math`: Cung cấp các hàm toán học như lượng giác, lũy thừa, logarit, và các hằng số toán học.
- `datetime`: Xử lý ngày và giờ.
- `random`: Tạo các số ngẫu nhiên.
- `os`: Tương tác với hệ điều hành.
- `sys`: Tương tác với trình thông dịch Python.

#### Ví dụ minh họa:

1. **Module `math`**:
```python
import math

# Sử dụng hàm sqrt để tính căn bậc hai
print(math.sqrt(16))  # Kết quả: 4.0

# Sử dụng hằng số pi
print(math.pi)  # Kết quả: 3.141592653589793
```

2. **Module `datetime`**:
```python
import datetime

# Lấy thời gian hiện tại
now = datetime.datetime.now()
print(now)

# Tạo đối tượng datetime cụ thể
specific_date = datetime.datetime(2020, 5, 17)
print(specific_date)
```

3. **Module `random`**:
```python
import random

# Tạo một số ngẫu nhiên giữa 1 và 10
print(random.randint(1, 10))

# Chọn ngẫu nhiên một phần tử từ danh sách
options = ['apple', 'banana', 'cherry']
print(random.choice(options))
```

### 3. Tự Định Nghĩa Module

Bạn có thể tự định nghĩa module của riêng mình bằng cách tạo một tệp `.py` và lưu các hàm, lớp hoặc biến trong đó. Ví dụ, tạo một tệp `mymodule.py` như sau:

**mymodule.py**:
```python
def greeting(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

pi = 3.14159
```

Sau đó, bạn có thể import và sử dụng module này trong một tệp Python khác:

```python
import mymodule

# Sử dụng hàm greeting từ mymodule
print(mymodule.greeting("Alice"))  # Kết quả: Hello, Alice!

# Sử dụng hàm add từ mymodule
print(mymodule.add(10, 5))  # Kết quả: 15

# Sử dụng biến pi từ mymodule
print(mymodule.pi)  # Kết quả: 3.14159
```

### 4. Cách Import Module

Python cung cấp nhiều cách để import module:

- Import toàn bộ module:
  ```python
  import mymodule
  print(mymodule.greeting("Alice"))
  ```

- Import một phần cụ thể từ module:
  ```python
  from mymodule import greeting
  print(greeting("Alice"))
  ```

- Đổi tên module khi import:
  ```python
  import mymodule as mm
  print(mm.greeting("Alice"))
  ```

### 5. Kết Luận

Module là một phần không thể thiếu trong Python, giúp tổ chức mã nguồn một cách hợp lý và tái sử dụng được nhiều lần. Python cung cấp nhiều module dựng sẵn rất hữu ích và bạn cũng có thể tự định nghĩa các module của riêng mình. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách sử dụng module trong Python.


## Function trong Python

### 1. Giới Thiệu về Function

**Function** (hàm) là một khối mã được tổ chức và tái sử dụng để thực hiện một nhiệm vụ cụ thể. Hàm giúp chia nhỏ chương trình thành các phần dễ quản lý và hiểu rõ hơn.

### 2. Định Nghĩa Function

Hàm trong Python được định nghĩa bằng từ khóa `def`, theo sau là tên hàm, danh sách tham số trong dấu ngoặc đơn và dấu hai chấm. Khối mã của hàm được thụt lề dưới dòng định nghĩa.

#### Cấu trúc cơ bản của một hàm:
```python
def function_name(parameters):
    """Docstring: mô tả chức năng của hàm"""
    # Khối mã của hàm
    return result
```

### 3. Ví Dụ Minh Họa

1. **Hàm đơn giản không có tham số và không trả về giá trị**:
```python
def greet():
    """Hàm chào hỏi"""
    print("Hello, world!")

greet()  # Kết quả: Hello, world!
```

2. **Hàm có tham số**:
```python
def greet(name):
    """Hàm chào hỏi một người cụ thể"""
    print(f"Hello, {name}!")

greet("Alice")  # Kết quả: Hello, Alice!
```

3. **Hàm có giá trị trả về**:
```python
def add(a, b):
    """Hàm tính tổng của hai số"""
    return a + b

result = add(5, 3)
print(result)  # Kết quả: 8
```

4. **Hàm có giá trị mặc định cho tham số**:
```python
def greet(name="world"):
    """Hàm chào hỏi với giá trị mặc định"""
    print(f"Hello, {name}!")

greet()          # Kết quả: Hello, world!
greet("Alice")   # Kết quả: Hello, Alice!
```

5. **Hàm với số lượng tham số không cố định**:
```python
def greet(*names):
    """Hàm chào hỏi nhiều người"""
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")  
# Kết quả: 
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### 4. Các Kiểu Function

#### 4.1. Hàm Lambda (Hàm ẩn danh)

Lambda là một kiểu hàm nhỏ gọn không có tên, thường được sử dụng cho các thao tác đơn giản và ngắn gọn.

Cú pháp:
```python
lambda arguments: expression
```

Ví dụ:
```python
# Hàm lambda tính bình phương của một số
square = lambda x: x * x
print(square(5))  # Kết quả: 25

# Hàm lambda cộng hai số
add = lambda a, b: a + b
print(add(3, 7))  # Kết quả: 10
```

#### 4.2. Hàm Đệ Quy

Hàm đệ quy là hàm gọi chính nó, thường được sử dụng để giải quyết các vấn đề có tính chất lặp lại theo cấu trúc phân rã.

Ví dụ:
```python
def factorial(n):
    """Hàm tính giai thừa bằng đệ quy"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Kết quả: 120
```

#### 4.3. Hàm Nội Bộ (Hàm lồng nhau)

Hàm nội bộ là hàm được định nghĩa bên trong một hàm khác. Chúng giúp tạo ra phạm vi riêng biệt cho mã nguồn và bảo vệ các biến nội bộ.

Ví dụ:
```python
def outer_function(text):
    """Hàm bên ngoài"""
    def inner_function():
        """Hàm bên trong"""
        print(text)
    inner_function()

outer_function("Hello from inner function!")
# Kết quả: Hello from inner function!
```

### 5. Kết Luận

Hàm là một thành phần quan trọng trong lập trình, giúp mã nguồn dễ hiểu, dễ quản lý và tái sử dụng. Python cung cấp nhiều kiểu hàm linh hoạt, bao gồm hàm thông thường, hàm lambda, hàm đệ quy và hàm nội bộ. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về cách định nghĩa và sử dụng hàm trong Python.