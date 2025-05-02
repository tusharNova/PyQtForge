from PyQt5.QtWidgets import QMainWindow
from views.mainWindow import Ui_MainWindow


class ClsMainWindow(QMainWindow):
    def __init__(self):
        super(ClsMainWindow , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText("Hello World")