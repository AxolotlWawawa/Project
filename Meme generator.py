import PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import random
import buttons_layout

window_menu = QWidget()
window_menu.resize(300, 400)
window_menu.setWindowTitle("Memory Card")
window_menu.setLayout(menu_layout)

window_menu.show()

window_study = QWidget()
window_study.resize(600, 500)
window_study.setWindowTitle("Memory Card")
window_study.setLayout(buttons_layout)
window_study.hide()

category1_btn.clicked.connect(ok_click)
category2_btn.clicked.connect(test_click)
category3_btn.clicked.connect(open_menu)


app.exec_()