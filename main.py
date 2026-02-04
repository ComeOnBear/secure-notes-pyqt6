from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
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


app = QApplication(sys.argv)

window = QWidget()
window.show()
app.exec()
