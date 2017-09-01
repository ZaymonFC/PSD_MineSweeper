#####   ---------------------------------------------------------------   #####
##                                 View Class                                ##
##                                                                           ##
#####   ---------------------------------------------------------------   #####

class View:
    def __init__(self, game_board, game_controller, master, settings):
        #
        # ─── ASSIGN REFERENCE VARIABLES ──────────────────────────────────
        #
        self.board = game_board
        self.controller = game_contoller

        #
        # ─── EXTRACT SETTINGS ────────────────────────────────────────────
        #
        self.height = settings['height']
        self.width = settings['width']
            
        #
        # ─── DEFINE THE FRAME ────────────────────────────────────────────
        #
        self.frame = Frame(master, background="#F19C79", borderwidth=3, height=720, width=720)
        self.frame.pack()

        self.images = self.load_images

        #
        # ─── CREATE COMPONENTS ───────────────────────────────────────────
        #
        self.canvas = Canvas(frame, )
    
    #
    # ─── LOAD IMAGES INTO DICTIONARY ──────────────────────────────────────────────
    #
    def load_images():
        images = {}
        images['square_up']   = PhotoImage(file="assets/square_up.png")
        images['square_down'] = PhotoImage(file="assets/square_down.png")
        images['square_bomb'] = PhotoImage(file="assets/square_bomb.png")
        
        return images

    


