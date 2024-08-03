import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicação com Múltiplas Telas")
        self.setGeometry(100, 100, 800, 600)

        # Criação do QStackedWidget para gerenciar múltiplas telas
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Criação das telas
        self.start_screen = self.create_start_screen()
        self.sidebar_screen = self.create_sidebar_screen()

        # Adicionar telas ao QStackedWidget
        self.stack.addWidget(self.start_screen)
        self.stack.addWidget(self.sidebar_screen)

        # Mostrar a tela inicial
        self.stack.setCurrentWidget(self.start_screen)

    def create_start_screen(self):
        # Criação da tela inicial com botão "Start"
        start_screen = QWidget()
        layout = QVBoxLayout(start_screen)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.show_sidebar_screen)
        layout.addWidget(start_button)

        return start_screen

    def create_sidebar_screen(self):
        # Criação da tela com barra lateral retrátil
        sidebar_screen = QWidget()
        main_layout = QHBoxLayout(sidebar_screen)

        # Criação da barra lateral (side bar)
        self.sidebar = QFrame()
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFixedWidth(200)

        # Layout da barra lateral
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.addWidget(QLabel("Item 1"))
        sidebar_layout.addWidget(QLabel("Item 2"))
        sidebar_layout.addWidget(QLabel("Item 3"))

        # Botão para retrair/expandir a barra lateral
        self.toggle_button = QPushButton("Retrátil")
        self.toggle_button.setFixedWidth(200)
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Adicionando a barra lateral e o botão ao layout principal
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.toggle_button)
        main_layout.addStretch()

        return sidebar_screen

    def show_sidebar_screen(self):
        # Método para mostrar a tela com a barra lateral
        self.stack.setCurrentWidget(self.sidebar_screen)

    def toggle_sidebar(self):
        # Alterna a visibilidade da barra lateral
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()

# Inicialização da aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
