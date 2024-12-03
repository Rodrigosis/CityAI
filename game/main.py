import pygame
import sys

from content_box import ContentBox


pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Interface Inspirada")

# Configuração do relógio
clock = pygame.time.Clock()
FPS = 30

# Inicializando as caixas
window_width, window_height = pygame.display.get_window_size()
windows = ContentBox(window_width, window_height)

running = True
while running:
    screen.fill((0, 0, 0))  # Preenchendo fundo

    # Desenhando caixas
    player_box = windows.player_status_box(screen)
    characters_box = windows.characters_present_box(screen)
    midley_box = windows.midley_box(screen)
    windows.maps_box(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window_width, window_height = event.w, event.h
            windows.window_width = window_width
            windows.window_height = window_height
        else:
            # Verifica em qual janela o mouse está antes de scrollar
            if windows.is_mouse_over(*player_box[:4]):
                windows.scroll_y_player = windows.handle_scroll(event, windows.scroll_y_player, player_box[4], player_box[3])
            elif windows.is_mouse_over(*characters_box[:4]):
                windows.scroll_y_characters = windows.handle_scroll(event, windows.scroll_y_characters, characters_box[4], characters_box[3])
            elif windows.is_mouse_over(*midley_box[:4]):
                windows.scroll_y_midley = windows.handle_scroll(event, windows.scroll_y_midley, midley_box[4], midley_box[3])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
