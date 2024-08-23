import turtle as t

t.setup(400, 400)
t.shape('arrow')


def drawSquare(a):
    for i in range(1,5):
        t.forward(100)  
        t.left(90)
        
drawSquare(100)
       
t.mainloop()