import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Página Inicial do Jogo")

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout vertical
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Botões
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button)

        load_button = QPushButton("Load")
        load_button.clicked.connect(self.load_game)
        layout.addWidget(load_button)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_game)
        layout.addWidget(exit_button)

        start_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")
        load_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 16px;")
        exit_button.setStyleSheet("background-color: #f44336; color: white; font-size: 16px;")
        
    def start_game(self):
        QMessageBox.information(self, "Start Game", "Starting the game...")
        # Aqui você pode adicionar a lógica para iniciar o jogo

    def load_game(self):
        QMessageBox.information(self, "Load Game", "Loading the game...")
        # Aqui você pode adicionar a lógica para carregar o jogo

    def exit_game(self):
        QMessageBox.information(self, "Exit Game", "Exiting the game...")
        # Aqui você pode adicionar a lógica para sair do jogo
        QApplication.instance().quit()



# Inicialização da aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
