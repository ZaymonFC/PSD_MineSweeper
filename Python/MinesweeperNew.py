# ────────────────────────────────────────────────────────────────────────────────
# ─── MINESWEEPER GAME ───────────────────────────────────────────────────────────
# ─── ENTIRE GAME IMPLEMENTATION FOR MINESWEEPER ─────────────────────────────────
# ─── AUTHOR: ZAYMON FOULDS COOK ─────────────────────────────────────────────────
# ─── VERSION: 0.1 ───────────────────────────────────────────────────────────────
# ─── DATE: 30TH 08 2017 ─────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

# Import Modules
from tkinter import *

# Import Classes
#from GameController import GameController
#from Board import Board
from View import View
from MainMenu import MainMenu


class Minesweeper:
    def __init__(self):
        #
        # ─── CREATE ROOT WINDOW ──────────────────────────────────────────
        #
        self.root = Tk()
        self.root.title("Z-Sweeper")
        self.root.resizable(False, False)
        
        #
        # ─── DISPLAY MAIN MENU AND POPULATE GAME SETTINGS ────────────────
        #
        self.game_settings = {}
        self.game_settings['width'] = 8
        self.game_settings['height'] = 8
        self.main_menu = MainMenu(self.root, self.game_settings)
        self.root.mainloop()
        print(self.game_settings['mode'])

        self.game_controller = []
        self.game_board = []

        self.view = View(self.game_board, self.game_controller, self.root, self.game_settings)

        self.root.mainloop()

        #
        # ─── CREATE GAME WITH SETTINGS ───────────────────────────────────
        #
        # mine_density = 0.15
        # dimension = 8
        # self.board = Board("square", mine_density, dimension)
        # self.game_controller = GameController(board)
        # self.view = View(board, game_controller)

Minesweeper()