import pygame

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quebra de Texto")

# Fonte
font = pygame.font.Font(None, 24)

# Texto longo para testar
long_text = "Nests 1: This is an example of a very long text that needs to wrap to fit inside the box."

def draw_wrapped_text(surface, text, font, color, x, y, max_width):
    """
    Desenha texto na tela quebrando automaticamente quando o espaço horizontal acabar.
    - surface: Superfície onde o texto será desenhado.
    - text: String do texto a ser desenhado.
    - font: Fonte usada para renderizar o texto.
    - color: Cor do texto.
    - x, y: Coordenadas iniciais para o texto.
    - max_width: Largura máxima antes de quebrar o texto para a linha seguinte.
    """
    words = text.split(' ')  # Divide o texto em palavras
    line = ""  # Linha atual
    y_offset = 0  # Offset vertical para cada linha

    for word in words:
        # Testa o tamanho da linha com a palavra atual adicionada
        test_line = f"{line} {word}".strip()
        test_surface = font.render(test_line, True, color)
        test_width = test_surface.get_width()

        if test_width <= max_width:  # Cabe na largura máxima
            line = test_line
        else:  # Não cabe, renderiza a linha atual e começa uma nova
            rendered_surface = font.render(line, True, color)
            surface.blit(rendered_surface, (x, y + y_offset))
            y_offset += font.get_height()  # Move para a próxima linha
            line = word  # Começa uma nova linha com a palavra atual

    # Renderiza qualquer texto restante na última linha
    if line:
        rendered_surface = font.render(line, True, color)
        surface.blit(rendered_surface, (x, y + y_offset))

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche a tela com branco
    screen.fill((255, 255, 255))

    # Desenha um retângulo
    rect_x, rect_y, rect_width, rect_height = 50, 50, 300, 200
    pygame.draw.rect(screen, (200, 200, 200), (rect_x, rect_y, rect_width, rect_height), border_radius=5)

    # Desenha o texto dentro do retângulo
    draw_wrapped_text(screen, long_text, font, (0, 0, 0), rect_x + 10, rect_y + 10, rect_width - 20)

    pygame.display.flip()

pygame.quit()
