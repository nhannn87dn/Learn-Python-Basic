import turtle as t

# Thiết lập sân khấu, kích thước cửa sổ đồ
# họa
t.setup(500, 500)
# Chọn kiểu hiển thị hình dáng con trỏ đồ họa
t.shape('turtle') #con rùa
#Hiển thị hình dáng con rùa lên
t.showturtle()

t.pensize(5)
t.penup() # chế độ nâng bút
t.backward(100)
t.pendown() # chế độ hạ bút, để vẻ
t.right(90)
t.forward(100)

# để lặp lại việc hiển thị cửa sổ
t.mainloop()
