import arcade

class Me(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png')
        self.w = 85
        self.h = 90
        self.center_x = 100
        self.center_y = 150
        self.speed = 3