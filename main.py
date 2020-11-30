from tkinter import *
from game import Game
from settings import *
from objects import *
from PIL import ImageTk, Image

tk = Tk()
tk.title(GAME_NAME)
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

canvas = Canvas(tk, width=WIDHT, height=HEIGHT, highlightthickness=0)
canvas.pack()



tk.update()

game = Game(tk, canvas)

if __name__ == '__main__':
    game.game_run() 

