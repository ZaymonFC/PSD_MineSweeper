#####   ---------------------------------------------------------------   #####
##                                 View Class                                ##
##                                                                           ##
#####   ---------------------------------------------------------------   #####

#
# ─── IMPORTS ────────────────────────────────────────────────────────────────────
#
from tkinter import *


class View:
    #
    # ─── CALLBACK FOR LEFT CLICKING THE CANVAS ──────────────────────────────────────
    #
    def callback(self, event):
        print("clicked at", event.x, event.y)
        x = event.x
        y = event.y
        button_i = x // 46
        button_j = y // 46
        print("clicked button: ", button_i, button_j)

    def __init__(self, game_board, game_controller, master, settings):
        #
        # ─── ASSIGN REFERENCE VARIABLES ──────────────────────────────────
        #
        self.board = game_board
        self.controller = game_controller

        #
        # ─── EXTRACT SETTINGS ────────────────────────────────────────────
        #
        self.height = settings['window_dimension']
        self.width = settings['window_dimension']
        self.game_size = settings['game_size']

        print 
            
        #
        # ─── DEFINE THE FRAME ────────────────────────────────────────────
        #
        self.frame = Frame(master, background="#F19C79", borderwidth=3, height=self.height, width=self.width)
        self.frame.pack()

        self.square_up   = PhotoImage(file="assets/square_up.png")
        self.square_down = PhotoImage(file="assets/square_down.png")
        self.square_bomb = PhotoImage(file="assets/square_bomb.png")

        #
        # ─── CREATE COMPONENTS ───────────────────────────────────────────
        #
        self.canvas = Canvas(self.frame, width=self.width, height=self.height, background="#F19C79")
        self.canvas.bind("<Button-1>", self.callback)
        self.canvas.pack()
        self.populate_buttons(12,12)



        #
        # ─── PACK AND PLACE ──────────────────────────────────────────────
        #
        # self.canvas.pack()

    #
    # ─── ADD GRID OF BUTTONS TO CANVAS BASED ON SPEC DIMENSION ──────────────────────
    #
    def populate_buttons(self, width, height):
        img_dimension = 46
        for i in range(width):
            for j in range(height):
                self.canvas.create_image(i * img_dimension, j * img_dimension, anchor=NW, image=self.square_up);

    
    #
    # ─── LOAD IMAGES INTO DICTIONARY ──────────────────────────────────────────────
    #
    def load_images(self):
        images = {}
        images['square_up']   = PhotoImage(file="assets/square_up.png")
        images['square_down'] = PhotoImage(file="assets/square_down.png")
        images['square_bomb'] = PhotoImage(file="assets/square_bomb.png")
        
        return images
    


