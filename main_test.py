import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QFrame, QSizePolicy, QSpacerItem, QProgressBar
from PyQt6.QtCore import Qt

class Sidebar(QWidget):
    def __init__(self, main_content_widget):
        super().__init__()
        self.main_content_widget = main_content_widget
        self.init_ui()

    def init_ui(self):
        # Layout principal da barra lateral
        layout = QVBoxLayout(self)

        # Adicionando itens de exemplo à barra lateral
        layout.addWidget(QLabel("£29,896   06:23   Thu"))
        layout.addWidget(QLabel("It's a school day."))
        layout.addWidget(QLabel("You are wearing a black school shirt, a pink school skirt, a black plain bra and black plain panties. Your identity is concealed by your surgical mask."))

        # Adicionando os status
        status_layout = QVBoxLayout()
        self.status_bars = []
        status_labels = [
            ("Pain: You feel okay.", 80),
            ("Arousal: You feel cold.", 40),
            ("Fatigue: You are wide awake.", 60),
            ("Stress: You are serene.", 20),
            ("Trauma: You are healthy.", 100),
            ("Control: You are confident.", 90),
            ("Allure: You look lewd.", 50)
        ]
        for status, value in status_labels:
            label = QLabel(status)
            label.setStyleSheet("color: green;" if "You" in status else "color: red;")
            status_layout.addWidget(label)
            progress_bar = QProgressBar()
            progress_bar.setValue(value)
            status_layout.addWidget(progress_bar)
            self.status_bars.append((label, progress_bar))
        status_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addLayout(status_layout)

        # Adicionando dica
        tip_label = QLabel("Tip: Being wet will cause your body to dissipate heat faster.")
        tip_label.setStyleSheet("color: yellow;")
        layout.addWidget(tip_label)

        # Adicionando botões
        buttons = [
            ("CHARACTERISTICS", "This is the characteristics screen."),
            ("SOCIAL", "This is the social screen."),
            ("TRAITS", "This is the traits screen."),
            ("JOURNAL", "This is the journal screen."),
            ("STATS", "This is the stats screen."),
            ("FEATS", "This is the feats screen."),
            ("DOL+ CREDITS", "This is the DOL+ credits screen."),
            ("OPTIONS", "This is the options screen."),
            ("SAVES", "This is the saves screen.")
        ]
        button_layout = QVBoxLayout()
        for button_text, content_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("background-color: grey; color: white;")
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.clicked.connect(lambda _, text=content_text: self.update_content(text))
            button_layout.addWidget(button)
        button_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addLayout(button_layout)

        # Adicionando um espaçador para alinhar os itens ao topo
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def update_content(self, text):
        self.main_content_widget.setText(text)

    def update_status(self, index, value):
        if 0 <= index < len(self.status_bars):
            label, progress_bar = self.status_bars[index]
            progress_bar.setValue(value)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Barra Lateral")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QHBoxLayout(central_widget)

        # Adicionando o conteúdo principal (espaço reservado)
        self.content = QLabel("Conteúdo principal")
        self.content.setStyleSheet("background-color: #282c34; color: white;")
        self.content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.content)

        # Adicionando a barra lateral
        self.sidebar = Sidebar(self.content)
        self.sidebar.setFixedWidth(250)
        main_layout.addWidget(self.sidebar)

        # Adicionando um botão no conteúdo principal para atualizar um status como exemplo
        update_button = QPushButton("Aumentar Arousal")
        update_button.clicked.connect(lambda: self.sidebar.update_status(1, 70))
        main_layout.addWidget(update_button)

# Inicialização da aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
