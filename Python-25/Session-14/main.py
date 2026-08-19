import turtle as t

# Cấu hình sân khấu với một kích thước mong muốn
t.setup(400, 300)
# Tâm rùa ở tọa độ 0,0

# Lệnh để cấu hình hình dáng của turtle
t.shape('turtle')

# Lấy hướng của rùa
h = t.heading()
print('h', h)

# Các lệnh điều khiển rùa

# 1. Đi tới n bước
# t.forward(100)
# # 2.Xoay đầu lên trên/ rẻ hướng
# t.left(90)
# t.forward(90)

# t.left(90)
# t.forward(90)

# t.left(90)
# t.forward(90)

# đi lùi
# t.backward(100)

# # Đi tới một tọa độ chỉ định
# t.goto(-100, 100)
# t.goto(0,0)

# Nhấc bút lêm
t.penup()
t.goto(-150, -75)
t.left(55)
t.pendown()

t.pencolor('#111111')
for _ in range(2):
    t.forward(150)
    t.right(55)
    t.forward(300)
    t.right(125)
# t.penup()
# t.home()
# t.goto(x=0, y=-50)
# t.pendown()
# t.fillcolor('red')
# t.pencolor('red')
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.penup()


# Tô màu rùa
#t.fillcolor('yellow')
#t.pencolor('yellow')
# Tô nền cho khối hình vẽ
#t.begin_fill() # bắt đầu tô nền
# vẽ hình
##t.circle(50)
#t.end_fill() # kết thúc tô nền
#
# Giử lại cửa sổ sân khấu
t.done()