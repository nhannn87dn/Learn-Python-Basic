# Đồ họa con Rùa

## 1. Giới Thiệu về Turtle Graphics

**Turtle Graphics** là một mô-đun đồ họa chuẩn trong Python, được sử dụng để vẽ các hình ảnh và hình học đơn giản. Mô-đun này rất hữu ích trong việc học lập trình và minh họa các thuật toán hình học.

## 2. Cài Đặt Turtle Graphics

Mô-đun Turtle là một phần của thư viện chuẩn Python, vì vậy bạn không cần phải cài đặt thêm gì cả. Bạn chỉ cần import nó vào chương trình của mình:

```python
import turtle
```

## 3. Các Lệnh Cơ Bản của Turtle

### Tạo và Hiển Thị Cửa Sổ Vẽ

```python
# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Hiển thị cửa sổ vẽ
turtle.done()
```

### Di Chuyển Turtle

```python
# Tạo một đối tượng Turtle
t = turtle.Turtle()

# Di chuyển turtle về phía trước 100 đơn vị
t.forward(100)

# Quay trái 90 độ
t.left(90)

# Di chuyển turtle về phía trước 50 đơn vị
t.forward(50)

# Hiển thị cửa sổ vẽ
turtle.done()
```

### Các Lệnh Di Chuyển Khác

- `t.backward(distance)`: Di chuyển turtle về phía sau `distance` đơn vị.
- `t.right(angle)`: Quay turtle sang phải một góc `angle` độ.
- `t.goto(x, y)`: Di chuyển turtle đến tọa độ `(x, y)`.

## 4. Vẽ Hình Học Cơ Bản

### Vẽ Hình Vuông

```python
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### Vẽ Hình Tam Giác

```python
t = turtle.Turtle()

for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
```

### Vẽ Hình Tròn

```python
t = turtle.Turtle()

# Vẽ hình tròn với bán kính 50 đơn vị
t.circle(50)

turtle.done()
```

## 5. Tùy Chỉnh Turtle

### Thay Đổi Màu Sắc

```python
t = turtle.Turtle()

# Thay đổi màu viền (màu bút)
t.pencolor("blue")

# Thay đổi màu tô (màu nền bên trong hình)
t.fillcolor("red")

# Bắt đầu tô màu
t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.right(90)

# Kết thúc tô màu
t.end_fill()

turtle.done()
```

### Thay Đổi Độ Dày Nét Vẽ

```python
t = turtle.Turtle()

# Thay đổi độ dày nét vẽ
t.pensize(5)

t.forward(100)

turtle.done()
```

### Ẩn và Hiện Turtle

```python
t = turtle.Turtle()

# Ẩn turtle
t.hideturtle()

t.forward(100)

# Hiện turtle
t.showturtle()

turtle.done()
```

## 6. Vẽ Hình Phức Tạp

### Vẽ Ngôi Sao

```python
t = turtle.Turtle()

for _ in range(5):
    t.forward(100)
    t.right(144)

turtle.done()
```

### Vẽ Bông Hoa

```python
t = turtle.Turtle()

t.pencolor("red")

for _ in range(36):
    t.forward(100)
    t.right(170)

turtle.done()
```

## Thực hành

Vẽ những hình học cơ bản sau

![](nhan-hieu-hinh-hoc.jpg)
