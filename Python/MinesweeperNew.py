# ────────────────────────────────────────────────────────────────────────────────
# ─── MINESWEEPER GAME ───────────────────────────────────────────────────────────
# ─── ENTIRE GAME IMPLEMENTATION FOR MINESWEEPER ─────────────────────────────────
# ─── AUTHOR: ZAYMON FOULDS COOK ─────────────────────────────────────────────────
# ─── VERSION: 0.1 ───────────────────────────────────────────────────────────────
# ─── DATE: 30TH 08 2017 ─────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

import GameController
import Board
import SquareView
import MainMenu

class Minesweeper:
    def __init__(self):
        #
        # ─── DISPLAY MAIN MENU AND POPULATE GAME SETTINGS ────────────────
        #
        self.game_settings = {}
        self.main_menu = Menu(game_settings)

        #
        # ─── CREATE GAME WITH SETTINGS ───────────────────────────────────
        #
        mine_density = 0.15
        dimension = 8
        self.board = Board("square", mine_density, dimension)
        self.game_controller = GameController(board)
        self.view = View(board, game_controller)

    def run(self):

        