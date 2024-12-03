import pygame
import sys


class ContentBox:
    def __init__(self, window_width: int, window_height: int) -> None:
        self.window_width = window_width
        self.window_height = window_height
        self.margin = 5
        self.color_1 = (90, 90, 90)
        self.color_2 = (50, 50, 50)
        self.color_3 = (255, 255, 255)

        # Scroll positions
        self.scroll_y_player = 0
        self.scroll_y_characters = 0
        self.scroll_y_midley = 0

    def add_scroll(self, surface, x, y, width, height, content_height, scroll_y):
        """Desenha a barra de scroll e ajusta o valor de scroll_y."""
        pygame.draw.rect(surface, (70, 70, 70), (x + width - 15, y, 15, height))  # Fundo da barra
        scroll_bar_height = (height / content_height) * height
        scroll_bar_y = y + (scroll_y / content_height) * height
        pygame.draw.rect(surface, (150, 150, 150), (x + width - 15, scroll_bar_y, 15, scroll_bar_height))  # Barra de rolagem

    def handle_scroll(self, event, scroll_y, content_height, view_height):
        """Gerencia eventos de scroll para uma janela."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll para cima
                scroll_y = max(scroll_y - 20, 0)
            elif event.button == 5:  # Scroll para baixo
                scroll_y = min(scroll_y + 20, content_height - view_height)
        return scroll_y

    def player_status_box(self, surface, width: int = 300, height: int = 100):
        font = pygame.font.Font(None, 24)
        height = self.window_height - (self.margin * 2)
        x = self.margin
        y = self.margin
        content_height = 800  # Altura do conteúdo interno
        pygame.draw.rect(surface, self.color_1, (x, y, width, height), border_radius=5)

        # Criando uma superfície para o conteúdo
        content_surface = pygame.Surface((width, content_height))
        content_surface.fill(self.color_1)

        # Renderizando itens no conteúdo
        for i in range(30):
            text_surface = font.render(f"Player Status {i+1}", True, self.color_3)
            content_surface.blit(text_surface, (10, i * 30))

        # Mostrando conteúdo visível
        visible_rect = pygame.Rect(0, self.scroll_y_player, width - 15, height)
        surface.blit(content_surface, (x, y), visible_rect)

        # Adicionando a barra de scroll
        self.add_scroll(surface, x, y, width, height, content_height, self.scroll_y_player)

    def characters_present_box(self, surface, width: int = 300, height: int = 100):
        font = pygame.font.Font(None, 24)
        height = self.window_height - 300 - (self.margin * 3)
        x = self.window_width - width - self.margin
        y = self.margin
        content_height = 600  # Altura do conteúdo interno
        pygame.draw.rect(surface, self.color_1, (x, y, width, height), border_radius=5)

        # Criando uma superfície para o conteúdo
        content_surface = pygame.Surface((width, content_height))
        content_surface.fill(self.color_1)

        # Renderizando itens no conteúdo
        for i in range(20):
            text_surface = font.render(f"Character {i+1}", True, self.color_3)
            content_surface.blit(text_surface, (10, i * 30))

        # Mostrando conteúdo visível
        visible_rect = pygame.Rect(0, self.scroll_y_characters, width - 15, height)
        surface.blit(content_surface, (x, y), visible_rect)

        # Adicionando a barra de scroll
        self.add_scroll(surface, x, y, width, height, content_height, self.scroll_y_characters)

    def midley_box(self, surface, width: int = 300, height: int = 300):
        font = pygame.font.Font(None, 24)
        width = self.window_width - 600 - (self.margin * 4)
        height = self.window_height - (self.margin * 2)
        x = 300 + (self.margin * 2)
        y = self.margin
        content_height = 1200  # Altura do conteúdo interno
        pygame.draw.rect(surface, self.color_2, (x, y, width, height), border_radius=5)

        # Criando uma superfície para o conteúdo
        content_surface = pygame.Surface((width, content_height))
        content_surface.fill(self.color_2)

        # Renderizando itens no conteúdo
        for i in range(50):
            text_surface = font.render(f"Nests {i+1}", True, self.color_3)
            content_surface.blit(text_surface, (10, i * 30))

        # Mostrando conteúdo visível
        visible_rect = pygame.Rect(0, self.scroll_y_midley, width - 15, height)
        surface.blit(content_surface, (x, y), visible_rect)

        # Adicionando a barra de scroll
        self.add_scroll(surface, x, y, width, height, content_height, self.scroll_y_midley)


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
    windows.player_status_box(screen)
    windows.characters_present_box(screen)
    windows.midley_box(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window_width, window_height = event.w, event.h
            windows.window_width = window_width
            windows.window_height = window_height
        else:
            # Gerenciar scroll para cada janela
            windows.scroll_y_player = windows.handle_scroll(event, windows.scroll_y_player, 800, window_height - 10)
            windows.scroll_y_characters = windows.handle_scroll(event, windows.scroll_y_characters, 600, window_height - 310)
            windows.scroll_y_midley = windows.handle_scroll(event, windows.scroll_y_midley, 1200, window_height - 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
