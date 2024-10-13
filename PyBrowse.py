import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView


class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Simple PySide6 Browser")
        self.setGeometry(100, 100, 800, 600)

        # Create a layout for the browser window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget) # type: ignore
        
        # Add a QLineEdit for the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.load_url)
        self.layout.addWidget(self.url_bar)

        # Add a QWebEngineView to display web pages
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        # Set default URL
        self.browser.setUrl("http://www.google.com")

    def load_url(self):
        # Load the URL from the line edit
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    window.show()
    sys.exit(app.exec())
