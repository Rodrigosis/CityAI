import sys
from PyQt6.QtWidgets import QApplication  # type: ignore

from game.gui.main_window import MainWindow


# Inicialização da aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
