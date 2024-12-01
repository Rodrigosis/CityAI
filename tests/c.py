import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget

class TextAdventureGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jogo de Aventura Textual")
        self.setGeometry(100, 100, 600, 400)

        # Criação dos componentes
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.input_line = QLineEdit(self)
        self.send_button = QPushButton("Enviar", self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.input_line)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Estado do jogo
        self.state = "inicio"
        self.inventory = []

        # Conectar o botão de enviar ao método que processa o input do jogador
        self.send_button.clicked.connect(self.process_input)

        # Mensagem inicial do jogo
        self.update_text("Você está na entrada de uma caverna escura. Você vê uma tocha no chão.")

    def update_text(self, text):
        self.text_area.append(text)

    def process_input(self):
        player_input = self.input_line.text().strip().lower()
        self.input_line.clear()

        if self.state == "inicio":
            if player_input == "pegar tocha":
                self.inventory.append("tocha")
                self.update_text("Você pegou a tocha. Agora você pode ver melhor na escuridão.")
                self.state = "entrada_caverna"
            else:
                self.update_text("Comando inválido. Tente 'pegar tocha'.")

        elif self.state == "entrada_caverna":
            if player_input == "entrar":
                self.update_text("Você entra na caverna. Está frio e úmido.")
                self.state = "dentro_caverna"
            else:
                self.update_text("Comando inválido. Tente 'entrar'.")

        elif self.state == "dentro_caverna":
            if player_input == "explorar":
                self.update_text("Você explora a caverna e encontra um baú.")
                self.state = "encontrou_bau"
            else:
                self.update_text("Comando inválido. Tente 'explorar'.")

        elif self.state == "encontrou_bau":
            if player_input == "abrir baú":
                self.update_text("Você abriu o baú e encontrou uma espada!")
                self.inventory.append("espada")
                self.state = "fim"
            else:
                self.update_text("Comando inválido. Tente 'abrir baú'.")

        elif self.state == "fim":
            self.update_text("Fim de jogo. Você encontrou a espada e venceu!")
            self.send_button.setDisabled(True)
        else:
            self.update_text("Comando não reconhecido.")

def main():
    app = QApplication(sys.argv)
    window = TextAdventureGame()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
