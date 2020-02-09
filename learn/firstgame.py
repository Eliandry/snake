import turtle
window = turtle.Screen()
window.bgpic("dad.png")
window.screensize(1000,500)
window.setup()
pen = turtle.Turtle()
pen.color('red')
for i in [-200,-100,0,100]:
    pen.setpos(x=i,y=0)
    pen.circle(radius=100)
    pen.forward(100)
    pen.circle(radius=100)
    pen.down()
    pen.color('black')

window.mainloop()
