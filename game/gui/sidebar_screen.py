from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QPushButton, QLabel, QSizePolicy, QSpacerItem, QProgressBar  # type: ignore


class SidebarScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout principal da barra lateral
        layout = QVBoxLayout(self)

         # Adicionando itens de exemplo à barra lateral
        layout.addWidget(QLabel("£29,896   06:23   Thu"))
        layout.addWidget(QLabel("It's a school day."))
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        # Adicionando dica
        tip_label = QLabel("Tip: Being wet will cause your body to dissipate heat faster.")
        tip_label.setStyleSheet("color: yellow;")
        layout.addWidget(tip_label)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        # Adicionando os status
        status_layout = QVBoxLayout()
        self.status_bars = []
        status_labels = [
            ("Health: You feel okay.", 80),
            ("Fatigue: You feel cold.", 40),
            ("Stress: You are wide awake.", 60),
            ("Arousal: You are serene.", 20),
            ("Pain: You are healthy.", 100),
            ("Willpower: You are confident.", 90),
            ("Allure: You look lewd.", 80)
        ]
        for status, value in status_labels:
            label = QLabel(status)
            label.setStyleSheet("color: green;" if "You" in status else "color: red;")
            status_layout.addWidget(label)
            progress_bar = QProgressBar()
            progress_bar.setValue(value)
            progress_bar.setTextVisible(False)  # Ocultar o texto de percentagem
            status_layout.addWidget(progress_bar)
            self.status_bars.append((label, progress_bar))
        status_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addLayout(status_layout)

        # Adicionando botões
        buttons = [
            "CHARACTER", "SOCIAL", "JOURNAL", "MAP"
        ]
        button_layout = QVBoxLayout()
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("background-color: grey; color: white;")
            button_layout.addWidget(button)
        button_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addLayout(button_layout)

        # Adicionando um espaçador para alinhar os itens ao topo
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Adicionando botões lado a lado
        hbox = QHBoxLayout()
        btn1 = QPushButton("OPTIONS")
        btn1.setStyleSheet("background-color: grey; color: white;")
        btn2 = QPushButton("LOAD")
        btn2.setStyleSheet("background-color: grey; color: white;")
        btn3 = QPushButton("SAVE")
        btn3.setStyleSheet("background-color: grey; color: white;")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        layout.addLayout(hbox)

        # Botão para retrair/expandir a barra lateral
        self.toggle_button = QPushButton("Retrátil")
        self.toggle_button.setFixedWidth(200)
        self.toggle_button.clicked.connect(self.toggle_sidebar)

    def toggle_sidebar(self):
        # Alterna a visibilidade da barra lateral
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()
