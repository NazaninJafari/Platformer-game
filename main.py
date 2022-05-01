from winsound import PlaySound
import arcade
import time

from player import Me
from enemy import Enemy
from ground import Ground , Cle, Lock

class Game(arcade.Window):
    def __init__(self):
        super().__init__(Screen_width, Screen_height, "Platformer")
        self.backg_image = arcade.load_texture("bg_pic1.jpg")
        self.start_time = time.time()
        self.gravity = 0.4
        self.me = Me()
        self.lock = Lock()
        
        self.star = arcade.load_texture(':resources:images/items/star.png') 
        self.enemy_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()
        self.enemyphysics_engine = []
        self.key_list = []
        #sounds of game
        self.sound_attaque = arcade.load_sound('mixkit.wav')
        self.sound_gov = arcade.load_sound(':resources:sounds/lose5.wav')
        self.sound_key = arcade.load_sound(':resources:sounds/coin4.wav')
        self.sound_win = arcade.load_sound('mix_win.wav')
        #count of star
        self.count = 3
        #key_count
        self.count_key = 0
        #continue= 0 , finish=1
        self.flag = 0
        
        for i in range(0,1000,120):
            ground = Ground(120,135,i,15)
            self.ground_list.append(ground)
 
        self.key_list.append(Cle(60,400))
        self.key_list.append(Cle(420,480))
        self.key_list.append(Cle(710,580))

        for i in range(50,200,100):
            ground = Ground(100,100,i,300)
            self.ground_list.append(ground)    

        for i in range(400,550,100):
            ground = Ground(100,100,i,400)
            self.ground_list.append(ground) 

        for i in range(700,710,10):
            ground = Ground(100,100,i,500)
            self.ground_list.append(ground) 

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant=self.gravity)

    def on_draw(self):

        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, Screen_width, Screen_height, self.backg_image)

        if self.flag == 1:
            arcade.draw_text('You Win', 250, 300, arcade.color.GREEN, 50)
            arcade.draw_text('press space for exit',250, 300, arcade.color.BABY_PINK, 40)   
            
        if self.count == 0: 
            arcade.play_sound(self.sound_gov)
            arcade.draw_text('GAME OVER', 250, 600, arcade.color.ORANGE ,50)
            arcade.draw_text('press space for exit',250, 300, arcade.color.BABY_PINK, 40) 
        
        self.me.draw()
        self.lock.draw()    
        
        for enemy in self.enemy_list:
            enemy.draw()

        for g in self.ground_list:
            g.draw()

        for key in self.key_list:
            key.draw()
        
        #show star
        for i in range(self.count):
            arcade.draw_lrwh_rectangle_textured((i*10)+700 + i*10 , Screen_height - 40, 40, 40 , self.star)    

    def on_update(self, delta_time: float):
        
        self.physics_engine.update()
 
        self.end_time = time.time()
        if self.end_time - self.start_time > 3 :
            enemies = Enemy()
            self.enemy_list.append(enemies)
            self.enemyphysics_engine.append(arcade.PhysicsEnginePlatformer(enemies , self.ground_list, gravity_constant = self.gravity))
            self.start_time = time.time()    
        
        for i in self.enemyphysics_engine:
            i.update()
        
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                self.count -= 1
                arcade.play_sound(self.sound_attaque)
                self.enemy_list.remove(enemy)

        for key in self.key_list:
            if arcade.check_for_collision(self.me , key):
                self.key_list.remove(key)
                arcade.play_sound(self.sound_key)
                self.count_key += 1        
    
        if arcade.check_for_collision(self.me , self.lock) and self.count_key == 3:
            arcade.play_sound(self.sound_win)     
            del self.lock
            self.flag = 1
        
        if self.me.center_x < 0 :
                self.me.center_x = 30
        if self.me.center_x > Screen_width:
                self.me.center_x = Screen_width - 30

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed
            
        elif symbol == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed

        elif symbol == arcade.key.UP:
            if self.physics_engine.can_jump:
                self.me.change_y = 10

        elif symbol == arcade.key.SPACE:
            arcade.finish_render()
            arcade.exit()

    def on_key_release(self, key, modifiers):
        self.me.change_x = 0


Screen_width = 900
Screen_height = 700

game = Game()
arcade.run()