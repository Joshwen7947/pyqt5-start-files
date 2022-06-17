from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QRadioButton, QButtonGroup
# 
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
# 
window.setWindowTitle('My App')
window.setGeometry(100, 100, 500, 800)
# 
button = QPushButton('center')
layout.addWidget(button, alignment=Qt.AlignCenter)
# 
def print_text():
    text = QLabel('Button Clicked!')
    layout.addWidget(text,alignment=Qt.AlignCenter)
    window.setLayout(layout)

button.clicked.connect(print_text)
# 
# 
# 
radio1 = QRadioButton('1')
radio1.setChecked(True)
radio2 = QRadioButton('2')
radio2.setChecked(False)
radio3 = QRadioButton('3')
radio3.setChecked(False)
# 
btn_group = QButtonGroup()
btn_group.addButton(radio1, id = 1)
btn_group.addButton(radio2, id = 2)
btn_group.addButton(radio2, id = 3)
# 
layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(radio3)

display = QLabel()
layout.addWidget(display, alignment=Qt.AlignCenter)
window.setLayout(layout)


def radio_checked():
    display.setText("You chose button number " + str(btn_group.checkedId()))

radio1.clicked.connect(radio_checked)
radio2.clicked.connect(radio_checked)
radio3.clicked.connect(radio_checked)


window.show()
window.setLayout(layout)
app.exec_()




