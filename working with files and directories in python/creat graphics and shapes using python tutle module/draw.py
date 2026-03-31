import turtle
t= turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.reset()
t.clear()

t.backward(100 )
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)
t.up()
t.right(90)
t.forward(20)
t.down()
t.circle(40)

for x in range (1,5):
    t.forward(50)
    t.left(90)
    
for x in range (1,9):
    t.forward(100)
    t.right(225)    