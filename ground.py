import arcade

class Ground(arcade.Sprite):
    def __init__(self,w,h,x,y):
        super().__init__(':resources:images/tiles/grassMid.png')
        self.width = w
        self.height = h
        self.center_x = x
        self.center_y = y

class Cle(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(':resources:images/items/keyYellow.png')        
        self.width = 40
        self.height = 35
        self.center_x = x
        self.center_y = y

class Lock(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/tiles/lockYellow.png')
        self.width = 80
        self.height = 80
        self.center_x = 850
        self.center_y = 130
