import pygame
import os 
from grid import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic Tac Toe')

running = True
player = "X"

grid = Grid()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse(pos[0]//200,pos[1]//200,player)
                if grid.switch_player:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                
                grid.print_grid()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                
    screen.fill((0,0,0))
    grid.draw(screen)
    pygame.display.flip()
