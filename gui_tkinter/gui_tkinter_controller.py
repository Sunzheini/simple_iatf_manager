from tkinter import *
from tkinter import colorchooser, messagebox, filedialog, ttk
from gui_tkinter.gui_tkinter_functions import create_main_window, create_frames
from main import new

color = '#7698cb'
geometry = '610x610'
root = Tk()
create_main_window(root, geometry)
f1, f2, f3, f4 = create_frames(root, color)


f1.config(bg='white')
label1 = Label(
    f1,
    text="database control",
    width=10,
    height=2,
    bg='white',
    borderwidth=1,
    relief="ridge",
)
label1.grid(sticky="E", row=0, column=0)

button1 = Button(
    f1,
    text='create db',
    command=new,
)
button1.grid(sticky="E", row=1, column=0)

root.mainloop()
