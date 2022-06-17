from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('X')
window.setGeometry(100,100,500,800)
# 
num1 = QLabel('Javascript')
num2 = QLabel('Python')
num3 = QLabel('C#')
num4 = QLabel('C++')
num5 = QLabel('PHP')
num6 = QLabel('Java')

# Make 4 layouts
layoutVertical = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

# Add 2 QLabels to each ROW.
layoutH1.addWidget(num1, alignment=Qt.AlignCenter)
layoutH1.addWidget(num2, alignment=Qt.AlignCenter)
layoutH2.addWidget(num3, alignment=Qt.AlignCenter)
layoutH2.addWidget(num4, alignment=Qt.AlignCenter)
layoutH3.addWidget(num5, alignment=Qt.AlignCenter)
layoutH3.addWidget(num6, alignment=Qt.AlignCenter)
# 
layoutVertical.addLayout(layoutH1)
layoutVertical.addLayout(layoutH2)
layoutVertical.addLayout(layoutH3)
# 
window.setLayout(layoutVertical)

window.show()
app.exec_()