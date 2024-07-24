# Đồ họa con Rùa

## 1. Giới Thiệu về Turtle Graphics

**Turtle Graphics** là một mô-đun đồ họa chuẩn trong Python, được sử dụng để vẽ các hình ảnh và hình học đơn giản. Mô-đun này rất hữu ích trong việc học lập trình và minh họa các thuật toán hình học.

## 2. Cài Đặt Turtle Graphics

Mô-đun Turtle là một phần của thư viện chuẩn Python, vì vậy bạn không cần phải cài đặt thêm gì cả. Bạn chỉ cần import nó vào chương trình của mình:

```python
import turtle
```

## 3. Các Lệnh Cơ Bản của Turtle

Dưới đây là bảng phân nhóm các lệnh của thư viện `turtle` kèm theo giải thích bằng tiếng Việt, lấy từ tài liệu [turtle — Turtle graphics — Python 3.12.4 documentation](https://docs.python.org/3/library/turtle.html#turtle-methods).

### Turtle Methods

#### Turtle Motion

- **Move and Draw**
  - `forward() | fd()`: Di chuyển rùa về phía trước một khoảng cách nhất định.
  - `backward() | bk() | back()`: Di chuyển rùa lùi về phía sau một khoảng cách nhất định.
  - `right() | rt()`: Xoay rùa sang phải một góc nhất định.
  - `left() | lt()`: Xoay rùa sang trái một góc nhất định.
  - `goto() | setpos() | setposition()`: Di chuyển rùa đến vị trí (x, y) xác định.
  - `teleport()`: Dịch chuyển rùa tức thời đến vị trí mới mà không vẽ đường.
  - `setx()`: Đặt tọa độ x của rùa.
  - `sety()`: Đặt tọa độ y của rùa.
  - `setheading() | seth()`: Đặt hướng của rùa.
  - `home()`: Đưa rùa về vị trí gốc (0, 0).
  - `circle()`: Vẽ một hình tròn với bán kính xác định.
  - `dot()`: Vẽ một chấm tròn tại vị trí hiện tại của rùa.
  - `stamp()`: Đóng dấu hình rùa tại vị trí hiện tại.
  - `clearstamp()`: Xóa một dấu đã được đóng.
  - `clearstamps()`: Xóa tất cả các dấu đã được đóng.
  - `undo()`: Hoàn tác hành động cuối cùng.
  - `speed()`: Đặt tốc độ di chuyển của rùa.

#### Tell Turtle’s State

- **Position and Orientation**
  - `position() | pos()`: Trả về tọa độ hiện tại của rùa.
  - `towards()`: Tính toán góc để rùa quay về một vị trí xác định.
  - `xcor()`: Trả về tọa độ x hiện tại của rùa.
  - `ycor()`: Trả về tọa độ y hiện tại của rùa.
  - `heading()`: Trả về hướng hiện tại của rùa.
  - `distance()`: Tính khoảng cách từ vị trí hiện tại của rùa đến một điểm xác định.

#### Settings and Measurement

- **Unit Settings**
  - `degrees()`: Đặt đơn vị đo góc là độ.
  - `radians()`: Đặt đơn vị đo góc là radian.

#### Pen Control

- **Drawing State**

  - `pendown() | pd() | down()`: Đặt bút xuống để bắt đầu vẽ.
  - `penup() | pu() | up()`: Nhấc bút lên để ngừng vẽ.
  - `pensize() | width()`: Đặt độ rộng của nét vẽ.
  - `pen()`: Trả về hoặc đặt các thuộc tính của bút.
  - `isdown()`: Kiểm tra xem bút có đang ở trạng thái vẽ hay không.

- **Color Control**

  - `color()`: Đặt màu của bút và màu tô.
  - `pencolor()`: Đặt màu của bút.
  - `fillcolor()`: Đặt màu tô.

- **Filling**

  - `filling()`: Kiểm tra xem rùa có đang ở trạng thái tô màu hay không.
  - `begin_fill()`: Bắt đầu một vùng để tô màu.
  - `end_fill()`: Kết thúc và tô màu vùng đã xác định.

- **More Drawing Control**
  - `reset()`: Đặt lại rùa về trạng thái ban đầu và xóa toàn bộ bản vẽ.
  - `clear()`: Xóa toàn bộ bản vẽ nhưng giữ nguyên trạng thái của rùa.
  - `write()`: Viết văn bản tại vị trí hiện tại của rùa.

#### Turtle State

- **Visibility**

  - `showturtle() | st()`: Hiển thị rùa.
  - `hideturtle() | ht()`: Ẩn rùa.
  - `isvisible()`: Kiểm tra xem rùa có đang được hiển thị hay không.

- **Appearance**
  - `shape()`: Đặt hình dạng của rùa.
  - `resizemode()`: Đặt chế độ thay đổi kích thước hình rùa.
  - `shapesize() | turtlesize()`: Đặt kích thước hình rùa.
  - `shearfactor()`: Đặt hệ số biến dạng của rùa.
  - `settiltangle()`: Đặt góc nghiêng của rùa.
  - `tiltangle()`: Trả về góc nghiêng của rùa.
  - `tilt()`: Nghiêng rùa một góc nhất định.
  - `shapetransform()`: Đặt phép biến hình của rùa.
  - `get_shapepoly()`: Trả về hình đa giác của rùa.

#### Using Events

- **Mouse and Keyboard Events**
  - `onclick()`: Đăng ký một hàm xử lý sự kiện click chuột.
  - `onrelease()`: Đăng ký một hàm xử lý sự kiện thả chuột.
  - `ondrag()`: Đăng ký một hàm xử lý sự kiện kéo chuột.

#### Special Turtle Methods

- **Polygon Handling**
  - `begin_poly()`: Bắt đầu ghi lại hình đa giác.
  - `end_poly()`: Kết thúc ghi lại hình đa giác.
  - `get_poly()`: Trả về hình đa giác đã ghi lại.
  - `clone()`: Tạo một bản sao của rùa.
  - `getturtle() | getpen()`: Trả về chính đối tượng rùa.
  - `getscreen()`: Trả về đối tượng màn hình mà rùa đang vẽ trên đó.
  - `setundobuffer()`: Đặt kích thước bộ đệm hoàn tác.
  - `undobufferentries()`: Trả về số lượng mục trong bộ đệm hoàn tác.

### Methods of TurtleScreen/Screen

#### Window Control

- **Background and Screen Settings**
  - `bgcolor()`: Đặt màu nền của màn hình.
  - `bgpic()`: Đặt hình nền của màn hình.
  - `clearscreen()`: Xóa toàn bộ màn hình.
  - `resetscreen()`: Đặt lại màn hình về trạng thái ban đầu.
  - `screensize()`: Đặt kích thước của màn hình.
  - `setworldcoordinates()`: Đặt tọa độ thế giới cho màn hình.

#### Animation Control

- **Animation Settings**
  - `delay()`: Đặt độ trễ của hoạt hình.
  - `tracer()`: Đặt số bước vẽ sẽ được bỏ qua để tăng tốc độ vẽ.
  - `update()`: Cập nhật màn hình với các thay đổi vẽ.

#### Using Screen Events

- **Event Listeners**
  - `listen()`: Đặt màn hình vào chế độ lắng nghe sự kiện.
  - `onkey() | onkeyrelease()`: Đăng ký một hàm xử lý sự kiện nhấn/phát hành phím.
  - `onkeypress()`: Đăng ký một hàm xử lý sự kiện nhấn phím.
  - `onclick() | onscreenclick()`: Đăng ký một hàm xử lý sự kiện click chuột trên màn hình.
  - `ontimer()`: Đăng ký một hàm xử lý sự kiện hẹn giờ.
  - `mainloop() | done()`: Bắt đầu vòng lặp chính của chương trình.

#### Settings and Special Methods

- **Screen Mode and Shape Management**
  - `mode()`: Đặt chế độ màn hình.
  - `colormode()`: Đặt chế độ màu.
  - `getcanvas()`: Trả về đối tượng canvas của màn hình.
  - `getshapes()`: Trả về danh sách các hình dạng có sẵn.
  - `register_shape() | addshape()`: Đăng ký một hình dạng mới.
  - `turtles()`: Trả về danh sách các rùa trên màn hình.
  - `window_height()`: Trả về chiều cao cửa sổ.
  - `window_width()`: Trả về chiều rộng cửa sổ.

#### Input Methods

- **User Input**
  - `textinput()`: Hiển thị hộp thoại nhập văn bản từ người dùng.
  - `numinput()`: Hiển thị hộp thoại nhập số từ người dùng.

#### Methods Specific to Screen

- **Screen Specific**
  - `bye()`: Đóng cửa sổ màn hình.
  - `exitonclick()`: Đóng cửa sổ màn hình khi người dùng click chuột.
  - `setup()`: Đặt kích thước và vị trí của cửa sổ màn hình.
  - `title()`: Đặt tiêu đề của cửa sổ màn hình.

Bạn có thể truy cập danh sách đầy đủ các lệnh và mô tả chi tiết từ đường dẫn tài liệu chính thức: [turtle — Turtle graphics — Python 3.12.4 documentation](https://docs.python.org/3/library/turtle.html#turtle-methods).

Cách vẽ một số hình cơ bản:

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
