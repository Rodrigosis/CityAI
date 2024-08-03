import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicação com Barra Lateral Retrátil")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.main_layout = QHBoxLayout(self.central_widget)

        # Criação da barra lateral (side bar)
        self.sidebar = QFrame()
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFixedWidth(200)

        # Layout da barra lateral
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.addWidget(QLabel("Item 1"))
        self.sidebar_layout.addWidget(QLabel("Item 2"))
        self.sidebar_layout.addWidget(QLabel("Item 3"))

        # Botão para retrair/expandir a barra lateral
        self.toggle_button = QPushButton("Retrátil")
        self.toggle_button.setFixedWidth(200)
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Adicionando a barra lateral e o botão ao layout principal
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.toggle_button)
        self.main_layout.addStretch()

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
