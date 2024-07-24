import turtle as t

# Tạo ra vùng làm việc cho turtel
t.setup(500, 500)
# Hình dáng cho con trỏ
t.shape("turtle")
#t.penup() # chế độ nâng bút, ko vẽ
t.pendown() #chế độ hạ bút để vẽ
t.pencolor("red")
t.pensize(5) # độ dày 5 điểm ảnh = 5px

# di chuyển theo tọa độ  goto(x,y)
#t.goto(250, 250)

# # đi tới
# t.forward(100)
# # xoay sang trái 90 độ
# t.left(90)
# # đi tới 100px
# t.forward(100)
# t.left(90)
# # đi tới 100px
# t.forward(100)
# t.left(90)
# # đi tới 100px
# t.forward(100)

# đi lùi 100 bước = 100px = 100 điểm ảnh
# t.backward(100)
# t.setheading(180)
# t.home()

# Vẽ hình tròn với bán kính 50 đơn vị
#t.circle(50)

# Vẻ một hình có màu nền
#b1. Chọn màu
t.fillcolor("red")
#b3: bắt đầu tô màu
t.begin_fill()

#b4. Vẻ hình
for i in range(4):
    t.forward(100)
    t.left(90)

#b5. Kết thúc tô màu
t.end_fill()

t.mainloop()