from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QGridLayout, QWidget, QLabel, QVBoxLayout, QMessageBox
)

from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QFont, QKeyEvent

from sys import argv
from random import randint
from functools import lru_cache

from settings.settings import *
from classes.cell import Cell


class Snake_Game(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_UI()
        self.snake = snake_body_parts_start_possitions
        self.generate_food()
        self.draw_snake()
        self.draw_food()

    def init_UI(self) -> None:
        self.setWindowTitle('Snake QT')
        self.setStyleSheet(f'background-color: {background_color};')

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        grid_widget = QWidget()
        grid = QGridLayout()
        grid.setSpacing(1)

        self.board = [[Cell() for i in range(width)] for j in range(height)]

        self.counter = QLabel()
        self.counter.setText('0')

        self.counter.setFixedSize(QSize(label_width, label_height))
        self.counter.setFont(QFont(font_family, font_size))
        self.counter.setContentsMargins(5, 2, 0, 0)
        self.counter.setStyleSheet(f'color: {font_color};')
        self.counter.setAlignment(Qt.AlignmentFlag.AlignRight)

        for i in range(height):
            for j in range(width):
                grid.addWidget(self.board[i][j], i, j)

        grid_widget.setLayout(grid)

        main_layout.addWidget(self.counter)
        main_layout.addWidget(grid_widget)

        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)

        self.current_direction = Directions.RIGHT.value

        self.timer = QTimer()
        self.timer.setInterval(game_speed)
        self.timer.timeout.connect(self.move_snake)
        self.timer.start()

    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        self.current_direction = directions_connected_to_offsets[event.key()]

    def generate_food(self) -> None:
        while True:
            i, j = randint(0, height - 1), randint(0, width - 1)
            
            if [i, j] in self.snake: continue
            self.food_current_position = [i, j]
            self.draw_food()
            return
            
    def draw_food(self) -> None:
        self.board[self.food_current_position[0]][self.food_current_position[1]].css(food_color)

    def collision_checker(self, head_i: int, head_j: int) -> None:
        if head_i < 0 or head_i >= height or\
            head_j < 0 or head_j >= width or\
                [head_i, head_j] in self.snake[1:]: return True
        return False
    
    def food_eatten_checker(self, head_i: int, head_j: int) -> None:
        return True if [head_i, head_j] == self.food_current_position else False

    def move_snake(self) -> None:
        offset_i, offset_j = offsets[self.current_direction]
        head_i, head_j = [self.snake[0][0] + offset_i, self.snake[0][1] + offset_j]

        if self.collision_checker(head_i, head_j):
            self.show_game_over_dialog()
        elif self.food_eatten_checker(head_i, head_j):
            self.snake = [[head_i, head_j]] + self.snake
            self.generate_food()
            self.increment_counter()
            self.draw_snake()
        else:
            i, j = self.snake[-1]
            self.board[i][j].css(cell_default_color)
            self.snake = [[head_i, head_j]] + self.snake[:-1]
            self.draw_snake()

    def draw_snake(self) -> None:
        self.board[self.snake[0][0]][self.snake[0][1]].css(snake_body_color)

    def increment_counter(self) -> None:
        self.counter.setText(str(int(self.counter.text()) + 10))

    def show_game_over_dialog(self) -> None:
        msg = QMessageBox()

        msg.setText('Would you like to try again ?')
        msg.setWindowTitle('Game Over')

        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        response = msg.exec()

        if response == QMessageBox.StandardButton.Yes:
            self.restart_game()
        else:
            QApplication.quit()

    def restart_game(self) -> None:
        self.init_UI()
        self.snake = snake_body_parts_start_possitions
        self.generate_food()
        self.draw_food()
        self.draw_snake()
        

def main(*args, **Kwargs) -> None:
    app = QApplication(argv)
    snake_game = Snake_Game()
    snake_game.show()
    app.exec()

if __name__ == '__main__':
    main()
