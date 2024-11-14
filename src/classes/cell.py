from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

from settings.settings import (
    stylesheet_for_cell, cell_default_color, cell_size
)

class Cell(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(QSize(cell_size, cell_size))
        self.css()

    def css(self, color=cell_default_color) -> None:
        self.setStyleSheet(stylesheet_for_cell.replace('_____', color))