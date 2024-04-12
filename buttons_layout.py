from PyQt5.QtWidgets import (QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

menu_layout = QVBoxLayout()

category1_btn = QPushButton("Категорія 1")
category2_btn = QPushButton("Категорія 2")
category3_btn = QPushButton("Категорія 3")

menu_layout.addWidget(category1_btn, alignment=Qt.AlignCenter)
menu_layout.addWidget(category2_btn, alignment=Qt.AlignCenter)
menu_layout.addWidget(category3_btn, alignment=Qt.AlignCenter)