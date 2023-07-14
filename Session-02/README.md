# Buổi 2: Cú pháp và Biến trong Python

Trong buổi học này, chúng ta sẽ tìm hiểu về cú pháp cơ bản của Python, cách làm việc với biến và kiểu dữ liệu, và thực hiện các phép toán số học. Điều này sẽ giúp bạn hiểu rõ hơn về cách sử dụng Python để thực hiện các tác vụ cơ bản trong lập trình.

## I. Cú pháp cơ bản của Python

### A. Khai báo biến

Khai báo biến là một trong những khái niệm cơ bản nhất trong Python. Để khai báo biến, bạn có thể sử dụng dấu bằng (=) để gán giá trị cho biến. Ví dụ:

```python
x = 5
y = "Hello, world!"
```

#### 1. Gán giá trị cho biến

Để gán giá trị cho biến, bạn chỉ cần sử dụng dấu bằng (=) và đặt giá trị cần gán bên phải dấu bằng. Ví dụ:

```python
x = 5
y = "Hello, world!"
```

#### 2. Quy tắc đặt tên biến

Khi đặt tên biến, bạn cần tuân thủ một số quy tắc sau:

- Tên biến phải bắt đầu bằng một chữ cái hoặc dấu gạch dưới ().
- Tên biến không được bắt đầu bằng một số.
- Tên biến chỉ có thể chứa các ký tự chữ cái, số và dấu gạch dưới ().
- Tên biến phân biệt chữ hoa và chữ thường.

### B. In ra màn hình

Để in ra màn hình trong Python, bạn có thể sử dụng hàm print(). Ví dụ:

```python
print("Hello, world!")
```

#### 1. Sử dụng hàm print()

Để in ra màn hình, bạn chỉ cần sử dụng hàm print() và đặt nội dung cần in trong dấu ngoặc kép. Ví dụ:


```python
print("Hello, world!")
```

#### 2. Định dạng chuỗi với f-strings

Để định dạng chuỗi trong Python, bạn có thể sử dụng f-strings. F-strings là một cách đơn giản và dễ đọc để định dạng chuỗi trong Python. Ví dụ:

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

### C. Điều khiển luồng

Điều khiển luồng là một khái niệm quan trọng trong lập trình. Trong Python, bạn có thể sử dụng câu lệnh if, else, elif để điều khiển luồng. Ví dụ:

```python
x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

#### 1. Câu lệnh if, else, elif

Câu lệnh if, else, elif được sử dụng để kiểm tra một điều kiện nào đó và thực hiện một hành động tương ứng. Ví dụ:

```python
x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

#### 2. Toán tử so sánh (==, !=, >, <, >=, <=)

Toán tử so sánh được sử dụng để so sánh hai giá trị với nhau. Ví dụ:

```python
x = 5
y = 10
if x < y:
    print("x is less than y")
```

#### 3. Toán tử logic (and, or, not)

Toán tử logic được sử dụng để kết hợp các điều kiện với nhau. Ví dụ:

```python
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive")
```

### D. Vòng lặp

Vòng lặp là một khái niệm quan trọng trong lập trình. Trong Python, bạn có thể sử dụng vòng lặp for và while để lặp lại một hành động nhiều lần. Ví dụ:

```python
for i in range(5):
    print(i)
```

#### 1. Vòng lặp for

Vòng lặp for được sử dụng để lặp lại một hành động nhiều lần với một danh sách các giá trị. Ví dụ:

```python
for i in range(5):
    print(i)
```

#### 2. Vòng lặp while

Vòng lặp while được sử dụng để lặp lại một hành động nhiều lần cho đến khi một điều kiện nào đó không còn đúng nữa. Ví dụ:


```python
i = 0
while i < 5:
    print(i)
    i += 1
```

#### 3. Toán tử break và continue

Toán tử break được sử dụng để kết thúc vòng lặp ngay lập tức, trong khi toán tử continue được sử dụng để bỏ qua một vòng lặp và tiếp tục với vòng lặp tiếp theo. Ví dụ:


```python
for i in range(10):
    if i == 5:
        break
    elif i % 2 == 0:
        continue
    print(i)
```

## II. Làm việc với biến và kiểu dữ liệu

### A. Kiểu dữ liệu cơ bản

Trong Python, có bốn kiểu dữ liệu cơ bản: số nguyên (int), số thực (float), chuỗi ký tự (str) và boolean (bool). Ví dụ:


```python
x = 5
y = 3.14
z = "Hello, world!"
w = True
```

#### 1. Số nguyên (int)

Số nguyên là một kiểu dữ liệu cơ bản trong Python, được sử dụng để lưu trữ các số nguyên. Ví dụ:


```python
x = 5
```

#### 2. Số thực (float)

Số thực là một kiểu dữ liệu cơ bản trong Python, được sử dụng để lưu trữ các số thực. Ví dụ:

```python
y = 3.14
```

#### 3. Chuỗi ký tự (str)

Chuỗi ký tự là một kiểu dữ liệu cơ bản trong Python, được sử dụng để lưu trữ các chuỗi ký tự. Ví dụ:

```python
z = "Hello, world!"

```

#### 4. Boolean (bool)

Boolean là một kiểu dữ liệu cơ bản trong Python, được sử dụng để lưu trữ các giá trị đúng hoặc sai. Ví dụ:

```python
w = True

```

### B. Ép kiểu dữ liệu

Trong Python, bạn có thể ép kiểu dữ liệu từ một kiểu sang một kiểu khác. Có hai loại ép kiểu dữ liệu: ép kiểu ngầm định và ép kiểu tường minh.

#### 1. Ép kiểu ngầm định

Ép kiểu ngầm định là quá trình ép kiểu dữ liệu tự động bởi Python. Ví dụ:

```python
x = 5
y = 3.14
z = x + y
```

#### 2. Ép kiểu tường minh

Ép kiểu tường minh là quá trình ép kiểu dữ liệu được thực hiện bởi người lập trình. Ví dụ:

```python
x = 5
y = str(x)
```

## III. Thực hiện các phép toán số học

Trong Python, bạn có thể thực hiện các phép toán số học như phép cộng, trừ, nhân, chia, chia lấy phần nguyên, chia lấy phần dư, lũy thừa và căn bậc hai.

### A. Phép cộng, trừ, nhân, chia

Phép cộng, trừ, nhân, chia là các phép toán số học cơ bản trong Python. Ví dụ:

```python
x = 5
y = 3
print(x + y) # Output: 8
print(x - y) # Output: 2
print(x * y) # Output: 15
print(x / y) # Output: 1.6666666666666667

```

### B. Chia lấy phần nguyên và chia lấy phần dư

Chia lấy phần nguyên và chia lấy phần dư là hai phép toán số học đặc biệt trong Python. Ví dụ:

```python
x = 5
y = 3
print(x // y) # Output: 1
print(x % y) # Output: 2
```

### C. Lũy thừa và căn bậc hai

Lũy thừa và căn bậc hai là hai phép toán số học đặc biệt trong Python. Ví dụ:

```python
x = 5
print(x ** 2) # Output: 25
print(x ** 0.5) # Output: 2.23606797749979
```

### D. Toán tử modulo

Toán tử modulo là một phép toán số học đặc biệt trong Python, được sử dụng để tính toán phần dư của một phép chia. Ví dụ:

```python
x = 5
y = 3
print(x % y) # Output: 2
```
