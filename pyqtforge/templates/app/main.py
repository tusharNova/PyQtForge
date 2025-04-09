import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello PyQt")
layout = QVBoxLayout()
label1 = QLabel("Hello from {{project_name}}!")
layout.addWidget(label1)

window.setLayout(layout)
window.resize(300, 200)
window.show()

sys.exit(app.exec_())
