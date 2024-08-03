from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QPushButton, QLabel  # type: ignore


class SidebarScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)

        # Criação da barra lateral (side bar)
        self.sidebar = QFrame()
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFixedWidth(200)

        # Layout da barra lateral
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.addWidget(QLabel("Item 1"))
        sidebar_layout.addWidget(QLabel("Item 2"))
        sidebar_layout.addWidget(QLabel("Item 3"))
        sidebar_layout.addWidget(QLabel("Item 3"))
        sidebar_layout.addWidget(QLabel("Item 3"))
        sidebar_layout.addWidget(QLabel("Item 2"))

        # Botão para retrair/expandir a barra lateral
        self.toggle_button = QPushButton("Retrátil")
        self.toggle_button.setFixedWidth(200)
        self.toggle_button.clicked.connect(self.toggle_sidebar)

        # Adicionando a barra lateral e o botão ao layout principal
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.toggle_button)
        main_layout.addStretch()

    def toggle_sidebar(self):
        # Alterna a visibilidade da barra lateral
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()
