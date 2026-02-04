from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
import sys

print("Hello from PySide67")
print("never mind no 67 here")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        windowIcon = QIcon()
        windowIcon.addFile('assets/secure.png')
        self.setWindowIcon(windowIcon)
        self.setWindowTitle("Secure Notes v0.1")
        self.setMinimumSize


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
