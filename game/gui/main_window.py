import sys
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QLabel  # type: ignore
from PyQt6.QtCore import Qt  # type: ignore

from gui.start_screen import StartScreen
from gui.sidebar_screen import SidebarScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("City AI")
        self.setGeometry(100, 100, 800, 600)

        # Criação do QStackedWidget para gerenciar múltiplas telas
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QHBoxLayout(central_widget)

        # Tela inicial
        self.start_screen = StartScreen(self.show_sidebar_screen)

        # Adicionando a barra lateral
        self.sidebar_screen = SidebarScreen()
        self.sidebar_screen.setFixedWidth(300)
        main_layout.addWidget(self.sidebar_screen)

        # Adicionando o conteúdo principal (espaço reservado)
        content = QLabel("Conteúdo principal")
        content.setStyleSheet("background-color: #282c34; color: white;")
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(content)

        # # Adicionar telas ao QStackedWidget
        # self.stack.addWidget(self.start_screen)
        # self.stack.addWidget(self.sidebar_screen)

        # # Mostrar a tela inicial
        # self.stack.setCurrentWidget(self.sidebar_screen)

    def show_sidebar_screen(self):
        # Método para mostrar a tela com a barra lateral
        self.stack.setCurrentWidget(self.sidebar_screen)
