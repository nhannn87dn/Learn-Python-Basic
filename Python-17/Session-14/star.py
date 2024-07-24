import turtle

# Tạo đối tượng Turtle
t = turtle.Turtle()

# Vẽ ngôi sao năm cánh
# Vẽ ngôi sao năm cánh
def draw_star(size, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
    t.end_fill()

# Chỉnh vị trí và kích thước của ngôi sao
t.penup()
t.goto(-50, 0)  # Đặt vị trí ban đầu của ngôi sao
t.pendown()
t.speed(1)  # Điều chỉnh tốc độ vẽ

# Vẽ ngôi sao với kích thước 100


draw_star(100, 'yellow')

# Đóng cửa sổ khi nhấp chuột vào nó
turtle.Screen().exitonclick()