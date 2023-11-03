from manage import *


def draw_field(screen, field):
    screen.blit(field, (0, 0))


def draw_pawn(pygame, screen, player):
    chess_surf = pygame.image.load(player.pic_path)
    try:
        chess_rect = chess_surf.get_rect(topleft=(POS_COORDINATES[player.pos][0], POS_COORDINATES[player.pos][1]))
    except:
        chess_rect = chess_surf.get_rect(topleft=(WIDTH / 2 - chess_surf.get_width(), 54))
    chess_surf = pygame.transform.scale(chess_surf, (57, 53))
    screen.blit(chess_surf, chess_rect)
