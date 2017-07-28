from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack(side=TOP)
label_1 = Label(frame, text="Name")
label_2 = Label(frame, text="Password")
entry_1 = Entry(frame)
entry_1 = Entry(frame)

label_1.grid(row=0)
label_2.grid(row=0, column=1)

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button1 = Button(frame2, text="Hello There")
button1.grid(row=0)
root.mainloop()