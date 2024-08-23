import turtle as t

# Thiết lập sân khấu, kích thước cửa sổ đồ
# họa
t.setup(500, 500)
# Chọn kiểu hiển thị hình dáng con trỏ đồ họa
t.shape('turtle') #con rùa
#Hiển thị hình dáng con rùa lên
t.showturtle()

t.pensize(5)
t.pencolor('red')

# Hình vuông, lặp lại 4 lần đi thẳng, rẻ trái
def drawSquare(a): 
    for i in range(4):
        t.forward(a)
        t.left(90)

drawSquare(100)
  
t.mainloop()