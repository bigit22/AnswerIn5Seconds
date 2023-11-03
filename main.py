import pygame
from manage import *
from player import Player
from temp import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(NAME)
clock = pygame.time.Clock()

running = True

player1 = Player('data/image/chess_suffering.png', 'Малой')

field = pygame.image.load('data/image/field.png')


if __name__ == '__main__':
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player1.roll_a_dice()

        draw_field(screen, field)
        draw_pawn(pygame, screen, player1)
        #draw_pawn(pygame, screen, player2)
        #player1.roll_a_dice()






        pygame.display.flip()

pygame.quit()
