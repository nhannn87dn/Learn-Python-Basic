# Session 01 - Giới thiệu về Python

## 1. Giới Thiệu về Python

**Python** là một ngôn ngữ lập trình cấp cao, dễ học, và linh hoạt. Được thiết kế với cú pháp rõ ràng và dễ đọc, Python là ngôn ngữ lập trình tuyệt vời cho cả người mới học và các chuyên gia. Python được sử dụng rộng rãi trong nhiều lĩnh vực như phát triển web, khoa học dữ liệu, học máy, trí tuệ nhân tạo, tự động hóa, và nhiều hơn nữa.

## 2. Cài Đặt Python

### Trên Windows
1. Tải Python từ trang web chính thức: [python.org](https://www.python.org/downloads/).
2. Chạy file cài đặt và nhớ chọn tùy chọn “Add Python to PATH”.
3. Hoàn tất quá trình cài đặt.

### Trên macOS
1. Mở Terminal và cài đặt Homebrew nếu chưa có: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Cài đặt Python bằng Homebrew: `brew install python`

### Trên Linux
1. Mở Terminal.
2. Cài đặt Python bằng trình quản lý gói của hệ điều hành. Ví dụ trên Ubuntu:
   ```bash
   sudo apt update
   sudo apt install python3
   ```

## 3. Chạy Python

Bạn có thể chạy Python theo nhiều cách:
- **Interactive Interpreter**: Mở Terminal hoặc Command Prompt, gõ `python` hoặc `python3` và bạn sẽ vào môi trường tương tác của Python.
- **Chạy Script**: Viết mã Python vào một file có đuôi `.py`, sau đó chạy bằng cách gõ `python script.py` trong Terminal hoặc Command Prompt.

## 4. Viết Chương Trình Python Đầu Tiên

Mở một trình soạn thảo văn bản (như Notepad, Sublime Text, hoặc Visual Studio Code) và viết chương trình đơn giản sau vào một file có đuôi `.py`:

```python
print("Hello, World!")
```

Lưu file với tên `hello.py` và chạy nó trong Terminal hoặc Command Prompt:

```bash
python hello.py
```

## 5. Cú Pháp Cơ Bản của Python

### Biến và Kiểu Dữ Liệu

```python
# Biến số nguyên
x = 5

# Biến số thập phân
y = 3.14

# Biến chuỗi
name = "Alice"

# Biến boolean
is_valid = True
```

### Toán Tử

```python
# Toán tử số học
a = 10 + 5  # Cộng
b = 10 - 5  # Trừ
c = 10 * 5  # Nhân
d = 10 / 5  # Chia
e = 10 % 3  # Chia lấy dư
f = 10 ** 2 # Lũy thừa

# Toán tử so sánh
print(a == b)  # Bằng
print(a != b)  # Không bằng
print(a > b)   # Lớn hơn
print(a < b)   # Nhỏ hơn
print(a >= b)  # Lớn hơn hoặc bằng
print(a <= b)  # Nhỏ hơn hoặc bằng
```

### Cấu Trúc Điều Khiển

```python
# Câu lệnh if
age = 18
if age >= 18:
    print("Bạn là người lớn.")
else:
    print("Bạn là trẻ em.")

# Vòng lặp for
for i in range(5):
    print(i)

# Vòng lặp while
count = 0
while count < 5:
    print(count)
    count += 1
```

## 6. Hàm trong Python

### Định Nghĩa và Gọi Hàm

```python
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

### Hàm với Giá Trị Trả Về

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Kết quả: 8
```

## 7. Làm Việc với Danh Sách

### Tạo và Truy Cập Phần Tử

```python
# Tạo danh sách
numbers = [1, 2, 3, 4, 5]

# Truy cập phần tử
print(numbers[0])  # Kết quả: 1

# Thay đổi phần tử
numbers[1] = 20
print(numbers)  # Kết quả: [1, 20, 3, 4, 5]
```

### Thêm, Xóa và Duyệt Phần Tử

```python
# Thêm phần tử
numbers.append(6)
print(numbers)  # Kết quả: [1, 20, 3, 4, 5, 6]

# Xóa phần tử
numbers.remove(20)
print(numbers)  # Kết quả: [1, 3, 4, 5, 6]

# Duyệt phần tử
for number in numbers:
    print(number)
```

## 8. Làm Việc với Từ Điển

### Tạo và Truy Cập Giá Trị

```python
# Tạo từ điển
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Truy cập giá trị
print(person["name"])  # Kết quả: Alice

# Thay đổi giá trị
person["age"] = 26
print(person)  # Kết quả: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

## 9. Làm Việc với Tệp

### Đọc Tệp

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Ghi Tệp

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

## 10. Kết Luận

Python là một ngôn ngữ lập trình mạnh mẽ và dễ học, phù hợp cho cả người mới bắt đầu và các lập trình viên chuyên nghiệp. Hy vọng bài giảng này giúp bạn bắt đầu với Python và khám phá nhiều khả năng của ngôn ngữ này.