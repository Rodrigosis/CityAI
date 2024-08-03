import sys
from PyQt6.QtWidgets import QMainWindow, QStackedWidget  # type: ignore

from game.gui.start_screen import StartScreen
from game.gui.sidebar_screen import SidebarScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicação com Múltiplas Telas")
        self.setGeometry(100, 100, 800, 600)

        # Criação do QStackedWidget para gerenciar múltiplas telas
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Criação das telas
        self.start_screen = StartScreen(self.show_sidebar_screen)
        self.sidebar_screen = SidebarScreen()

        # Adicionar telas ao QStackedWidget
        self.stack.addWidget(self.start_screen)
        self.stack.addWidget(self.sidebar_screen)

        # Mostrar a tela inicial
        self.stack.setCurrentWidget(self.start_screen)

    def show_sidebar_screen(self):
        # Método para mostrar a tela com a barra lateral
        self.stack.setCurrentWidget(self.sidebar_screen)