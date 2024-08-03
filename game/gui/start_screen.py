from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton  # type: ignore


class StartScreen(QWidget):
    def __init__(self, switch_to_sidebar_screen):
        super().__init__()
        self.switch_to_sidebar_screen = switch_to_sidebar_screen
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.switch_to_sidebar_screen)
        layout.addWidget(start_button)
