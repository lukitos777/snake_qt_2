width, height = 30, 20

cell_size = 44

game_speed = 200 # ms (1 ms = 1 second)

cell_default_color = '#bdeeff'
snake_body_color = '#00cc99'
food_color = '#ff0066'
background_color = '#ffffff'

stylesheet_for_cell = 'QPushButton {\nbackground-color: _____;\nborder: none;' +\
            '\nborder: none;\n}' +\
            'QPushButton:hover {\nbackground-color: _____;\n}\n' +\
            'QPushButton:disabled {\nbackground-color: _____;\n}'

font_family = 'Consolas'
font_size = 12
font_color = '#000000'

label_width, label_height = 1349, 18

from enum import Enum

class Directions(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'

# right , left, down, up
offsets = {
    Directions.LEFT.value: (0, -1), Directions.RIGHT.value: (0, 1),
    Directions.UP.value: (-1, 0), Directions.DOWN.value: (1, 0)    
}

snake_body_parts_start_possitions = [[11, 15], [10, 15], [9, 15]]

from PyQt6.QtCore import Qt 

directions_connected_to_offsets = {
    Qt.Key.Key_W: Directions.UP.value, Qt.Key.Key_S: Directions.DOWN.value,
    Qt.Key.Key_D: Directions.RIGHT.value, Qt.Key.Key_A: Directions.LEFT.value
}