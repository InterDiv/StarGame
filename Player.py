from color import Color
import pygame 
class Player:
    def __init__(self, x, y, size, color = Color.RED):
        self.x = x
        self.y = y 
        self.size = size 
        self.color = color 
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
    
    def detect_collision(self, other):
        if (self.x <= other.x and (self.x + self.size)>other.x) or (self.x >= other.x and (other.x + other.size)>self.x):
            if (self.y <= other.y and (self.y + self.size)>other.y) or (self.y >= other.y and (other.y + other.size)>self.y):
                return True
        return False

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color = Color.BLUE)

class Large_Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=100, color = Color.BLUE)

class HumanPlayer(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color = Color.RED)