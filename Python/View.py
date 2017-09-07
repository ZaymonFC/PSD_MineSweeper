# coding=utf-8
#####   ---------------------------------------------------------------   #####
##                                 View Class                                ##
##                                                                           ##
#####   ---------------------------------------------------------------   #####

#
# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from tkinter import *
from MenuBar import MenuBar

class View:
    #
    # ─── CALLBACK FOR LEFT CLICKING THE CANVAS ──────────────────────────────────────
    #
    def callback_toggle(self, event):
        #
        # ─── DISABLE THE BOARD ON LOSS ───────────────────────────────────
        if self.board.get_state_loss():
            return NONE
        if self.board.get_state_win():
            return NONE
        
        #
        # ─── MUTATE THE BOARD THROUGH THE CONTROLLER ─────────────────────
        print("clicked at", event.x, event.y)
        button_i = event.x // 46
        button_j = event.y // 46
        print("clicked button: ", button_i, button_j)
        self.controller.activate(button_i, button_j)

        #
        # ─── BEFORE REDRAW CHECK IF THE GAME IS OVER ─────────────────────
        if self.board.get_state_loss():
            self.draw_mines()
        else: 
            self.draw();


    def callback_cover(self, event):
        if self.board.get_state_loss():
            return NONE
        if self.board.get_state_win():
            return NONE
        #
        # ─── MUTATE THE BOARD THROUGH THE CONTROLLER ─────────────────────
        print("clicked at", event.x, event.y)
        button_i = event.x // 46
        button_j = event.y // 46
        print("clicked button: ", button_i, button_j)
        self.controller.cover(button_i, button_j)
        
        self.draw()

        if self.board.get_state_win():
            print("HEY YOU WON!!")
        #    # covers = self.board.get_state_covers()
            # for row in covers:
            #     for covers in row:
            #         if covers:
            #             print("1", end='\t')
            #         else:
            #             print("0", end='\t')
            #     print("\n") 



    # 


    def __init__(self, game_board, game_controller, master, settings):
        #
        # ─── ASSIGN REFERENCE VARIABLES ──────────────────────────────────
        self.board = game_board
        self.controller = game_controller

        #
        # ─── EXTRACT SETTINGS ────────────────────────────────────────────
        self.height = settings['window_dimension']
        self.width = settings['window_dimension']
        self.game_size = settings['game_size']
        self.tile_dimesion = settings['tile_dimension']

        #
        # ─── CALCULATE CANVAS DIMENSIONS ─────────────────────────────────
        canvas_dimension = self.tile_dimesion * self.game_size
            
        #
        # ─── DEFINE THE FRAME ────────────────────────────────────────────
        self.frame = Frame(master, background="#F19C79", borderwidth=23)
        self.frame.pack()

        self.square_up    = PhotoImage(file="assets/square_up.png")
        self.square_down  = PhotoImage(file="assets/square_down.png")
        self.square_bomb  = PhotoImage(file="assets/square_bomb.png")
        self.square_cover = PhotoImage(file="assets/square_cover.png")

        #
        # ─── CREATE COMPONENTS ───────────────────────────────────────────
        self.canvas = Canvas(self.frame, width=canvas_dimension, height=canvas_dimension, background="#F19C79",)
        self.canvas.bind("<Button-1>", self.callback_toggle)
        self.canvas.bind("<Button-3>", self.callback_cover)
        self.canvas.pack(side="top")
        self.populate_buttons(self.game_size, self.game_size)
        self.menubar = MenuBar(self.frame, self)
        self.menubar.pack(side="bottom", pady=(40,0))


    #
    # ─── ADD GRID OF BUTTONS TO CANVAS BASED ON SPEC DIMENSION ──────────────────────
    def populate_buttons(self, width, height):
        for i in range(width):
            for j in range(height):
                self.draw_tile(i, j, self.square_up)

    def draw(self):
        #
        # ─── GET CURRENT STATE OF THE MODEL ──────────────────────────────
        toggles = self.board.get_state_toggles()
        numbers = self.board.get_state_button_numbers()
        covers  = self.board.get_state_covers()

        # ─── REDRAW THE GAME BOARD ───────────────────────────────────────
        self.canvas.delete(ALL)
        for i in range(self.game_size):
            for j in range(self.game_size):
                if covers[i][j] == True:
                    self.draw_tile(i, j, self.square_cover)
                elif not toggles[i][j]:
                    self.draw_tile(i, j, self.square_up)
                elif numbers[i][j] == 0:
                    self.draw_tile(i, j, self.square_down)
                else:
                    self.draw_tile(i, j, self.square_down, numbers[i][j])
    #
    # ─── DRAW A SINGLE TILE ─────────────────────────────────────────────────────────
    def draw_tile(self, i, j, image, text=0):
        img_dimension = 46
        pos_x = img_dimension * i
        pos_y = img_dimension * j
        self.canvas.create_image(pos_x, pos_y, anchor=NW, image=image, tags="tile");

        if text != 0:
            if self.board.get_state_button_numbers()[i][j] is 'zero':
                 return
            self.canvas.create_text(pos_x + 22.5, pos_y + 22.5, text=text)


    def draw_mines(self):
        numbers = self.board.get_state_button_numbers()
    
        for i in range(self.game_size):
            for j in range(self.game_size):
                if numbers[i][j] == -1:
                    self.draw_tile(i, j, self.square_bomb)

    #
    # ─── FUNCTION TO DESTROY ALL TKINTER COMPONENTS AND RETURN TO MENU ──────────────
    #
    def cleanup(self):
        self.canvas.destroy()
        self.menubar.destroy()
        self.frame.destroy()
        self.frame.quit()
        