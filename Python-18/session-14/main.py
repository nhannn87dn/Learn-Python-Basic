import turtle as t

# Thiết lập sân khấu, kích thước cửa sổ đồ
# họa
t.setup(500, 500)

# Chọn kiểu hiển thị hình dáng con trỏ đồ họa
t.shape('turtle') #con rùa
#Hiển thị hình dáng con rùa lên
t.showturtle()

# Đi thẳng
# t.forward(100) # đi tời 100 điểm ảnh, 100 bước
# # Rẻ trái
# t.left(90)# rẻ trái 90 độ
# t.forward(100)

# t.right(90) # nghiêng đầu sang phải 90 độ
# t.backward(100) # đi lùi 100 bước

# Thiết lập màu cho nét vẻ
# Thực hiện trước khi di chuyển
t.pencolor('red')
t.pensize(5) # Độ dày nét vẻ 5px

t.fillcolor('red')
t.begin_fill() # bắt đầu tô màu

# Di chuyển bằng tọa độ
t.goto(x = 100, y=100)
t.backward(200)
t.goto(x = 0, y = 0) # rùa quay về tâm

# Kết thúc tô màu nền
t.end_fill()

# để lặp lại việc hiển thị cửa sổ
t.mainloop()
