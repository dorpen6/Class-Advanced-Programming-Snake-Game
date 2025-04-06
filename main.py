from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE =  50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# classes & objects

class Snake:
    pass

class Food:
    pass

class next_turn():
    pass

def change_direction(new_direciton):
    pass

def game_over():
    pass


window = Tk()
window.title("Snake Game")
window.resizable(True, True)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack

window.mainloop()