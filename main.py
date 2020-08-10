from Player import HumanPlayer
from screen import Screen
from game import Game
import sys
import pygame 

pygame.init()

screen = Screen()
player = HumanPlayer(screen.width/2, screen.height-100)

game = Game()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= player.size
            elif event.key == pygame.K_RIGHT:
                player.x += player.size


    game.drop_enemies(screen.width)
    game.update_enemy_position(screen.height)
    game.set_level()

    screen.update_screen(game.enemy_list, player, game.score)

    if game.collision_check(player):
        game_over = True
        break