from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTextBrowser,
    QScrollArea,
    QGridLayout,
    QLabel,
)
from PyQt5.QtCore import Qt
import sys


class MainGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Jogo Reescrito com PyQt5")
        self.setGeometry(100, 100, 1366, 768)  # Tamanho inicial da janela

        self.central_widget = QWidget()  # Widget central
        self.setCentralWidget(self.central_widget)

        # Layout principal: Grid para alinhar os elementos
        grid_layout = QGridLayout()
        self.central_widget.setLayout(grid_layout)

        # Instanciando os painéis do jogo

        content = ["Nivel: 10", "XP: 1500/2000", "Classe: Guerreiro"]
        vida = 75  # 75% de vida
        player_status_box_content = [f"Player Status {i}." for i in range(50)]
        player_status_box_content.insert(0, content)
        self.player_status_box = self.create_html_box(
            "Player Status", self.generate_html_player_status(content, vida)
        )

        midley_box_content = [f"Texto de exemplo para o midley box {i}." for i in range(50)]
        self.midley_box = self.create_html_box(
            "Midley Box", self.generate_html_midley(midley_box_content)
        )

        characters_present_box_content = [f"Character {i}." for i in range(50)]
        self.characters_present_box = self.create_html_box(
            "Characters Present", self.generate_html_characters_present(characters_present_box_content)
        )

        # Adicionando o "mapa" como um quadrado branco
        self.map_box = self.create_map_box()

        # Adicionando os widgets no grid layout (organização ajustada)
        grid_layout.addWidget(self.player_status_box, 0, 0, 2, 1)  # Linha 0 e 1, coluna 0 (lado esquerdo)
        grid_layout.addWidget(self.midley_box, 0, 1, 2, 1)  # Linha 0 e 1, coluna 1 (centro)
        grid_layout.addWidget(self.characters_present_box, 0, 2)  # Linha 0, coluna 2 (topo direito)
        grid_layout.addWidget(self.map_box, 1, 2)  # Linha 1, coluna 2 (embaixo à direita)

        # Ajustando tamanhos relativos de cada widget
        grid_layout.setColumnStretch(0, 2)  # Coluna esquerda (Player Status) menor
        grid_layout.setColumnStretch(1, 3)  # Coluna central (Midley Box) maior
        grid_layout.setColumnStretch(2, 2)  # Coluna direita
        grid_layout.setRowStretch(0, 3)  # Linha superior
        grid_layout.setRowStretch(1, 2)  # Linha inferior

    def create_html_box(self, title: str, html_content: str) -> QScrollArea:
        """
        Cria um componente scrollável contendo HTML com estilo CSS.
        """
        # Configurar um QTextBrowser para renderizar HTML
        text_browser = QTextBrowser()
        text_browser.setHtml(html_content)
        text_browser.setReadOnly(True)
        text_browser.setStyleSheet("background-color: #2e2e2e; color: white; border: none;")

        # Configurar uma área de scroll para rolagem
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(text_browser)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: 2px solid #2e2e2e;
                border-radius: 5px;
            }
            QScrollBar:vertical {
                background: #2e2e2e; /* Cor de fundo da barra vertical */
                width: 12px;         /* Largura da barra vertical */
                margin: 15px 3px 15px 3px; /* Margem da barra (superior, direita, inferior, esquerda) */
                border-radius: 5px;  /* Bordas arredondadas */
            }
            QScrollBar::handle:vertical {
                background: #5e5e5e; /* Cor da alça (scroll que se move) */
                min-height: 20px;    /* Altura mínima da alça */
                border-radius: 5px;  /* Bordas arredondadas */
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;    /* Remove os botões "+" e "-" */
                border: none;
            }
            QScrollBar:horizontal {
                background: #2e2e2e; /* Cor de fundo da barra horizontal */
                height: 12px;        /* Altura da barra horizontal */
                margin: 3px 15px 3px 15px; /* Margem da barra (superior, direita, inferior, esquerda) */
                border-radius: 5px;  /* Bordas arredondadas */
            }
            QScrollBar::handle:horizontal {
                background: #5e5e5e; /* Cor da alça */
                min-width: 20px;     /* Largura mínima da alça */
                border-radius: 5px;  /* Bordas arredondadas */
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none;    /* Remove os botões "+" e "-" */
                border: none;
            }
            QScrollBar::handle:hover {
                background: #787878; /* Cor da alça quando o mouse está sobre ela */
            }
        """)

        return scroll_area

    def create_map_box(self) -> QLabel:
        """
        Cria o quadrado branco que representa o mapa.
        """
        map_label = QLabel("Mapa")
        map_label.setAlignment(Qt.AlignCenter)
        map_label.setStyleSheet(
            """
            background-color: white;
            border: 2px solid black;
            font-size: 20px;
            font-weight: bold;
            color: black;
            border-radius: 5px;
            """
        )
        return map_label

    def generate_html_player_status(self, content: list, vida: int) -> str:
        """
        Gera o conteúdo HTML para a caixa Player Status com uma barra de vida.
        :param content: Lista de itens de conteúdo.
        :param vida: Percentual de vida do personagem (0 a 100).
        """
        formatted_content = "".join(
            f"<div class='player-text'>{item}</div>" for item in content
        )
        t = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #ffffff;
                    background-color: #2e2e2e;
                    padding: 10px;
                }}
                .player-box {{
                    margin-bottom: 20px;
                }}
                .player-image {{
                    width: 100%;
                    max-height: 200px;
                    object-fit: contain;
                    margin-bottom: 10px;
                }}
                .player-text {{
                    font-size: 16px;
                }}
                /* Estilos para a barra de vida */
                .vida-bar {{
                    width: 100%;
                    height: 20px;
                    background-color: #555;
                    border: 1px solid #333;
                    border-radius: 5px;
                    margin-top: 10px;
                    overflow: hidden;
                }}
                .vida-bar-inner {{
                    width: {vida}%; /* Percentual de vida */
                    height: 100%;
                    background-color: {self.get_cor_vida(vida)};
                    transition: width 0.3s ease-in-out; /* Suavidade na atualização */
                }}
            </style>
        </head>
        <body>
            <div>
                <div class="player-box">
                    <img src="../img/test_img_player_200.png" class="player-image" />
                    {formatted_content}
                    <!-- Barra de vida -->
                    <div class="vida-bar">
                        <div class="vida-bar-inner"></div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        print(t)
        return t

    def get_cor_vida(self, vida: int) -> str:
        """
        Retorna a cor da barra de vida com base no percentual de vida.
        :param vida: Percentual de vida do personagem.
        :return: Código de cor em HEX.
        """
        if vida > 50:
            return "#00FF00"  # Verde
        elif vida > 20:
            return "#FFFF00"  # Amarelo
        else:
            return "#FF0000"  # Vermelho

    def generate_html_midley(self, content: list) -> str:
        """
        Gera o conteúdo HTML para o Midley Box.
        :param content: Lista de itens de conteúdo.
        """
        formatted_content = "".join(
            f"<div class='midley-item'>{item}</div>" for item in content
        )
        return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #ffffff;
                    background-color: #303030;
                    padding: 10px;
                }}
                .midley-item {{
                    margin-bottom: 10px;
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>
            {formatted_content}
        </body>
        </html>
        """

    def generate_html_characters_present(self, content: list) -> str:
        """
        Gera o conteúdo HTML para a caixa Characters Present.
        :param content: Lista de itens de conteúdo.
        """
        formatted_content = "".join(
            f"<div class='character'>{item}</div>" for item in content
        )
        return f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #ffffff;
                    background-color: #2e2e2e;
                    padding: 10px;
                    border: 2px solid #5e5e5e;
                }}
                .character {{
                    margin: 5px 0;
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            {formatted_content}
        </body>
        </html>
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)

    game_window = MainGameWindow()
    game_window.show()

    sys.exit(app.exec_())
