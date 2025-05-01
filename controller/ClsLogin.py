from PyQt5.QtWidgets import QMainWindow
from views.login import Ui_MainWindow

class ClsLogin(QMainWindow):
    def __init__(self):
        super(ClsLogin ,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)