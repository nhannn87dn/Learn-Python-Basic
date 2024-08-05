# File Handling trong Python

## 1. Giới Thiệu về File Handling

**File handling** trong Python là kỹ thuật giúp bạn đọc và ghi dữ liệu vào tệp tin. Python cung cấp nhiều hàm và phương thức để thực hiện các thao tác này một cách dễ dàng và hiệu quả.

## 2. Mở và Đóng Tệp

### Mở Tệp

Để mở một tệp, bạn sử dụng hàm `open()`. Hàm này trả về một đối tượng tệp (file object), cho phép bạn thực hiện các thao tác đọc và ghi trên tệp.

```python
file = open("example.txt", "r")  # Mở tệp ở chế độ đọc (read)
```

Các chế độ mở tệp phổ biến:

- `"r"`: Mở tệp để đọc (mặc định).
- `"w"`: Mở tệp để ghi, nội dung cũ sẽ bị xóa nếu tệp tồn tại.
- `"a"`: Mở tệp để ghi, nội dung mới sẽ được thêm vào cuối tệp nếu tệp tồn tại.
- `"b"`: Mở tệp ở chế độ nhị phân (binary).
- `"t"`: Mở tệp ở chế độ văn bản (text, mặc định).
- `"+"`: Mở tệp để cập nhật (đọc và ghi).

### Đóng Tệp

Sau khi làm việc xong với tệp, bạn nên đóng tệp để giải phóng tài nguyên hệ thống bằng phương thức `close()`.

```python
file.close()
```

## 3. Đọc Tệp

Python cung cấp nhiều cách để đọc nội dung của tệp:

### Đọc Toàn Bộ Nội Dung

Phương thức `read()` đọc toàn bộ nội dung của tệp và trả về một chuỗi.

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

### Đọc Theo Dòng

Phương thức `readline()` đọc một dòng từ tệp mỗi lần.

```python
file = open("example.txt", "r")
line = file.readline()
while line:
    print(line, end='')  # Dùng end='' để không thêm dòng trống
    line = file.readline()
file.close()
```

### Đọc Tất Cả Các Dòng

Phương thức `readlines()` đọc tất cả các dòng từ tệp và trả về một danh sách các chuỗi.

```python
file = open("example.txt", "r")
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()
```

## 4. Ghi Tệp

Bạn có thể ghi dữ liệu vào tệp bằng phương thức `write()` hoặc `writelines()`.

### Ghi Chuỗi Vào Tệp

```python
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.write("This is a new line.\n")
file.close()
```

### Ghi Danh Sách Chuỗi Vào Tệp

```python
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open("example.txt", "w")
file.writelines(lines)
file.close()
```

## 5. Sử Dụng Câu Lệnh `with`

Câu lệnh `with` giúp bạn mở tệp và đảm bảo rằng tệp sẽ được đóng tự động sau khi khối lệnh kết thúc, ngay cả khi có lỗi xảy ra.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# Tệp sẽ tự động được đóng ở đây
```

## 6. Ví Dụ Minh Họa

### Ví Dụ Đọc Tệp

Giả sử bạn có một tệp `example.txt` với nội dung sau:

```
Hello, world!
This is a new line.
```

Bạn có thể đọc tệp như sau:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Ví Dụ Ghi Tệp

Bạn có thể ghi dữ liệu vào tệp như sau:

```python
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")
```

### Ví Dụ Thêm Nội Dung Vào Tệp

Bạn có thể thêm nội dung vào tệp mà không xóa nội dung cũ như sau:

```python
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
```

## 7. Kết Luận

File handling là một kỹ thuật quan trọng trong lập trình, giúp bạn lưu trữ và xử lý dữ liệu một cách hiệu quả. Python cung cấp nhiều phương thức mạnh mẽ để đọc và ghi tệp, giúp bạn thực hiện các thao tác này một cách dễ dàng. Hy vọng bài giảng này giúp bạn hiểu rõ hơn về file handling trong Python.