#
# ─── CLASS WHICH REPRESENTS THE MENU BAR TKINTER COMPONENT ──────────────────────
#   

import tkinter as tk
from tkinter import *

class MenuBar(tk.Frame):
    def __init__(self, parent, parentView):
        tk.Frame.__init__(self, parent)
        self.config(bg='#F19C79')
        self.parent = parent
        self.view = parentView

        #
        # ─── CREATE COMPONENTS ───────────────────────────────────────────
        self.quit_button = Button(
                            self,
                            text="Quit",
                            command="exit",
                            height=2,
                            width=10,
                            relief=FLAT,
                            bg='#F6F4D2',
                            highlightbackground='#F19C79',
                            borderwidth=1
                           )
        self.menu_button = Button(
                            self,
                            text="Main Menu",
                            height=2,
                            width=15,
                            command=lambda : self.main_menu(),
                            relief=FLAT,
                            bg='#F6F4D2',
                            highlightbackground='#F19C79',
                            borderwidth=1
                           )

        #
        # ─── PACK COMPONENTS ─────────────────────────────────────────────
        self.quit_button.pack(side="right")
        self.menu_button.pack(side="left")

    def main_menu(self):
        print("Got here")
        self.view.cleanup()
        