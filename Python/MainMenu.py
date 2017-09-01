#
# ─── MAINMENU CLASS ─────────────────────────────────────────────────────────────
#
from tkinter import *
# from Configuration import Configuration

class MainMenu:
    def __init__(self, master, settings):
        self.config = {}
        self.config['bg_colour'] = "#F19C79"
        self.settings = settings
        settings['difficulty'] = 0.15
        #
        # ─── DEFINE THE FRAME ────────────────────────────────────────────
        #
        self.frame = Frame(master, background="#F19C79", borderwidth=10, height=720, width=720)
        self.frame.pack()

        #
        # ─── DEFINE THE IMAGES ───────────────────────────────────────────
        #
        self.square_btn_img = PhotoImage(file="assets/stdBtn.png")
        self.hex_btn_img    = PhotoImage(file="assets/hexBtn.png")
        self.title_img       = PhotoImage(file="assets/title.png")
        #highscore_btn_img = PhotoImage(file="assets/highscoreBtn.png")

        #
        # ─── CREATE THE Components ───────────────────────────────────────
        #
        self.square_button = Button(
                                self.frame,
                                image=self.square_btn_img,
                                command=lambda mode="square": self.return_settings(mode),
                                width=149,
                                height=47,
                                bg=self.config['bg_colour'],
                                relief=FLAT,
                                borderwidth=0
                            )

        self.hex_button = Button(self.frame,
                                image=self.hex_btn_img,
                                command=lambda mode="hex": self.return_settings(mode),
                                width=149,
                                height=47,
                                bg=self.config['bg_colour'],
                                relief=FLAT,
                                borderwidth=0
                            )
        self.title_label = Label(
                                image=self.title_img,
                                bg=self.config['bg_colour']
                                )
        #
        # ─── PACK AND PLACE COMPONENTS ───────────────────────────────────
        #
        self.square_button.pack()
        self.hex_button.pack()
        self.title_label.pack()
        self.square_button.place(bordermode=OUTSIDE, x=280, y=300)
        self.hex_button.place(bordermode=OUTSIDE, x=280, y=400)
        self.title_label.place(bordermode=OUTSIDE, x=60, y=80)


    #
    # ─── EVENT LISTENER FOR CLICK DESTROYS COMPONENT AND RETURNS SETTINGS ───────
    #
    def return_settings(self, mode):
        self.clean_components()
        self.settings['mode'] = mode
        self.frame.destroy()
        self.frame.quit()
    

    #
    # ─── FUNCTION TO DESTROY ALL COMPONENTS [CLEAN UP] ──────────────────────────
    #
    def clean_components(self):
        self.square_button.destroy()
        self.hex_button.destroy()
        self.title_label.destroy()
        