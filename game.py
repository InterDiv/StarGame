import random
from Player import Enemy
from screen import Screen
class Game:
    def __init__(self, delay = 0.1, speed=5, score=0, max_enemies = 10):
        self.speed = speed
        self.delay = delay
        self.score = score
        self.max_enemies = max_enemies
        self.enemy_list = []

    def drop_enemies(self, screen_width):
        delay = random.random()
        if len(self.enemy_list) < self.max_enemies and delay < 0.1:
            random_x = random.randint(0, screen_width)
            y_pos = 0
            enemy = Enemy(random_x, y_pos)
            self.enemy_list.append(enemy)     
     
    def update_enemy_position(self, screen_height): # import screen height correctly(video in Downloads)
        new_enemy_list = []
        for enemy in self.enemy_list:
            if enemy.y >=0 and enemy.y < screen_height: # compare with screen_height
                enemy.y += self.speed
                new_enemy_list.append(enemy)
            else:
                self.score += 1
        self.enemy_list = new_enemy_list

    def set_level(self):
        if self.score < 20:
            self.speed  = 8
        elif self.score > 20:
            self.speed = 15
        
    
    def collision_check(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
        return False