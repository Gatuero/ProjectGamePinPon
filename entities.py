class Player():
    width = 25
    height = 75
    move = 5
    point = 0
    def __init__(self,x,y,color,select):
        self.x = x
        self.y = y
        self.color=color
        self.select=select
    def update(self):
        if self.select==0:
            self.y-=self.move
class Ball():
    time=0
    hspeed = 4
    vspeed = -3
    width = 15
    height = 15
    sound = 0
    touch_player = 0
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def update(self):
        self.x-=self.hspeed
        self.y-=self.vspeed
        if self.time>0:
            self.time-=1
class Block():
    give_player = 0
    def __init__(self,x,y,colors,size,points):
        self.x=x
        self.y=y
        self.colors=colors
        self.height = size
        self.width = size
        self.points = points
    def update(self):
        self.color=self.colors[self.points]