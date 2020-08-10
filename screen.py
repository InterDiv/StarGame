from color import Color
import pygame
class Screen:
    def __init__(self, clock_tick = 30, font_type ="monospace", font_size = 35, height = 600, width = 800, background_color = Color.BG_COLOR):
        self.height = height
        self.width = width
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick
    
    def draw_enemies(self, enemy_list):
        for enemy in enemy_list:
            enemy.draw(self.screen)
    
    def draw_player(self, player):
        player.draw(self.screen)
    
    def draw_score(self, score, color = Color.YELLOW):
        text = f'Score: {score}'
        label = self.font.render(text,1,color)
        self.screen.blit(label, (self.width-200, self.height-40))
    
    def update_screen(self, enemy_list, player, score):
        self.refresh_bg()
        self.draw_enemies(enemy_list)
        self.draw_player(player)
        self.draw_score(score)

        self.clock.tick(self.clock_tick)
        pygame.display.update()

    def refresh_bg(self):
        self.screen.fill(self.background_color)