import arcade
import random

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/robot/robot_fall.png')
        self.width = 90
        self.height = 140
        self.speed = 2
        self.center_x = random.randint(0,800) 
        self.center_y = 150
        self.change_x = random.choice([-1,1]) * self.speed
