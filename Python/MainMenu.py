#
# ─── MAINMENU CLASS ─────────────────────────────────────────────────────────────
#

from tkinter import *

class MainMenu:
    def __init__(self, master, settings):
        self.settings = settings
        settings['difficulty'] = 0.15
        #
        # ─── DEFINE THE FRAME ────────────────────────────────────────────
        #
        frame = frame(master, background="", borderwidth=3, height=720, width=720)
        frame.pack()

        #
        # ─── DEFINE THE IMAGES ───────────────────────────────────────────
        #
        square_btn_img = PhotoImage(file="assets/squareBtn.png")
        hex_btn_img = PhotoImage(file="assets/hexBtn.png")
        highscore_btn_img = PhotoImage(file="assets/highscoreBtn.png")

        #
        # ─── CREATE THE BUTTONS ──────────────────────────────────────────
        #
        self.square_button = Button(frame, command="self.")
        self.hex_button = Button(frame, )

        #
        # ─── PACK AND POSITION COMPONENTS ────────────────────────────────
        #

    def return_settings(self, mode):
