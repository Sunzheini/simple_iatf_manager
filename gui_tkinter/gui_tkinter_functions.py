from tkinter import *


def create_main_window(root, geometry):
    root.title("Simple IATF Manager")

    # commented this after adding the file menu since it was not working
    # root.eval("tk::PlaceWindow . center")
    # x = root.winfo_screenwidth() // 4          # 4: left edge starts from, 1/4 of screen width
    # y = int(root.winfo_screenheight() * 0.2)    # top edge starts from 20% of screen height
    # root.geometry('500x600+' + str(x) + '+' + str(y))

    root.geometry(geometry)
    icon = PhotoImage(file='../staticfiles/iatf_logo.png')  # convert image
    root.iconphoto(True, icon)  # change icon image


def create_frames(root, color):
    frame1 = Frame(
        root,
        bg=color,
        bd=2,
        relief='ridge'
    )
    frame1.place(x=5, y=5, width=300, height=300)

    frame2 = Frame(
        root,
        bg=color,
        bd=2,
        relief='ridge'
    )
    frame2.place(x=305, y=5, width=300, height=300)

    frame3 = Frame(
        root,
        bg=color,
        bd=2,
        relief='ridge'
    )
    frame3.place(x=5, y=305, width=300, height=300)

    frame4 = Frame(
        root,
        bg=color,
        bd=2,
        relief='ridge'
    )
    frame4.place(x=305, y=305, width=300, height=300)

    return frame1, frame2, frame3, frame4
