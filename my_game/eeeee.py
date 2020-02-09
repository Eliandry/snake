from tkinter import *
import random
class Segment(object):
    def __init__(self,x,y):
        self.instance = c.create_rectangle(x,y,x+snake_size,y+snake_size,fill="white")
class Snake(object):
    def __init__(self,segments):
        self.segments=segments
        self.mapping={"Down":(0,1),"Up":(0,-1),"Left":(-1,0),"Right":(1,0)}
        self.vector=self.mapping["Right"]
    def move(self):
        for index in range(len(self.segments)-1):
            segment=self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment,x1,y1,x2,y2)
        x1,y1,x2,y2=c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                       x1 + self.vector[0]*snake_size,
                       y1 + self.vector[1]*snake_size,
                       x2 + self.vector[0]*snake_size,
                       y2 + self.vector[1]*snake_size)
    def change_direction(self,event):
        if event.keysym in self.mapping:
            self.vector=self.mapping[event.keysym]
    def add_segment(self):
        last_seg=c.coords(self.segments[0].instance)
        x=last_seg[2]-snake_size
        y=last_seg[3]-snake_size
        self.segments.insert(0,Segment(x,y))
def create_block():
    global BLOCK
    posx=snake_size * (random.randint(1,(width-snake_size) / snake_size))
    posy = snake_size * (random.randint(1, (height - snake_size) / snake_size))
    BLOCK=c.create_oval(posx,posy,
                        posx+snake_size,
                        posy+snake_size,
                        fill="red")
def main():
    global in_game
    if in_game:
        s.move()
        head_coords=c.coords(s.segments[-1].instance)
        x1,y1,x2,y2=head_coords
        if x1<0 or x2>width or y1<0 or y2>height:
            in_game=False
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()
        else:
            for index in range(len(s.segments) - 1):
                if c.coords(s.segments[index].instance) == head_coords:
                    in_game = False
    else:
        c.create_text(width / 2, height / 2,
                      text="GAME OVER!",
                      font="Arial 20",
                      fill="#ff0000")


root = Tk()
root.title('snake')
width = 800
height = 600
snake_size = 20
in_game = True
c=Canvas(root,width=width,height=height,bg="#003300")
c.grid()
segments = [Segment(snake_size, snake_size),
            Segment(snake_size*2, snake_size),
            Segment(snake_size*3, snake_size)]
s=Snake(segments)
c.focus_set()
c.bind("<KeyPress>", s.change_direction)
root.mainloop()
