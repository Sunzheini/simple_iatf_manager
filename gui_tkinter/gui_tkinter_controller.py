from tkinter import *
from gui_tkinter.gui_tkinter_functions import create_main_window, create_frames, create_a_label, create_a_button, \
    create_an_entry


class GuiTkinterController:

    @staticmethod
    def start(function1, function2, function3):
        def printer_function(query):
            query_label = create_a_label(f4, query)
            query_label.config(width=30, height=5)
            query_label.place(x=0, y=0)

        def get1():
            query = function1(entry1.get())
            entry1.delete(0, END)
            printer_function(query)

        def get2():
            query = function2(entry2.get())
            entry2.delete(0, END)
            printer_function(query)

        def get3():
            query = function3(entry3.get())
            entry3.delete(0, END)
            printer_function(query)

        color = '#7698cb'
        geometry = '610x610'
        root = Tk()
        create_main_window(root, geometry)

        f1, f2, f3, f4 = create_frames(root, color)
        f1.config(bg='white')

        label1 = create_a_label(f1, "db control")
        label1.grid(row=0, column=0, columnspan=2)

        entry1 = Entry(f1, width=20)
        entry1.grid(row=1, column=0)

        entry2 = create_an_entry(f1)
        entry2.grid(row=2, column=0)

        entry3 = create_an_entry(f1)
        entry3.grid(row=3, column=0)

        button1 = create_a_button(f1, 'print', get1)
        button1.grid(sticky="W", row=1, column=1)
        button1.config(bg='light grey')

        button2 = create_a_button(f1, 'create table', get2)
        button2.grid(sticky="W", row=2, column=1)
        button2.config(bg='light grey')

        button3 = create_a_button(f1, 'delete table', get3)
        button3.grid(sticky="W", row=3, column=1)
        button3.config(bg='light grey')

        root.mainloop()
