import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 + HTML Example')

        # Cria um widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout vertical
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Cria uma instância de QWebEngineView
        self.web_view = QWebEngineView()

        # Carrega uma página HTML
        self.web_view.setHtml('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>PyQt5 + HTML</title>
            </head>
            <body>
                <h1>Olá, Mundo!</h1>
                <p>Este é um exemplo de conteúdo HTML renderizado em uma aplicação PyQt5.</p>
            </body>
            </html>
        ''')


        # Adiciona QWebEngineView ao layout
        layout.addWidget(self.web_view)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
