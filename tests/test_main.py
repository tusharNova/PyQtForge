import sys

from PyQt5.QtWidgets import QApplication
# from controller.ClsLogin import ClsLogin

if __name__ == '__main__':
    app = QApplication([])
    f = ClsLogin()
    f.show()
    sys.exit(app.exec_())
