import pygame

pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Barra de Scroll no Pygame")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

# Fonte
font = pygame.font.Font(None, 24)

# Configuração do conteúdo rolável
content_height = 1000  # Altura total do conteúdo
view_height = 400  # Altura visível (janela de visualização)
scroll_y = 0  # Posição inicial do scroll

# Configuração da barra de rolagem
scroll_bar_width = 20
scroll_bar_height = (view_height / content_height) * view_height
scroll_bar_y = 0

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll para cima
                scroll_y = max(scroll_y - 20, 0)
            elif event.button == 5:  # Scroll para baixo
                scroll_y = min(scroll_y + 20, content_height - view_height)

    # Preenchendo a tela
    screen.fill(WHITE)

    # Desenho do conteúdo rolável (um retângulo grande com texto de exemplo)
    content_surface = pygame.Surface((WIDTH, content_height))
    content_surface.fill(GRAY)
    for i in range(50):
        text = font.render(f"Linha {i+1}", True, BLACK)
        content_surface.blit(text, (10, i * 20))

    # Desenha a área visível do conteúdo rolável
    visible_rect = pygame.Rect(0, scroll_y, WIDTH - scroll_bar_width, view_height)
    screen.blit(content_surface, (0, 0), visible_rect)

    # Desenho da barra de rolagem
    scroll_bar_y = (scroll_y / content_height) * view_height
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH - scroll_bar_width, scroll_bar_y, scroll_bar_width, scroll_bar_height))

    # Atualiza a tela
    pygame.display.flip()

pygame.quit()
