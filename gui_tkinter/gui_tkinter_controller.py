from tkinter import *
from gui_tkinter.gui_tkinter_functions import create_main_window, create_frames, create_a_label, create_a_button, \
    create_an_entry


class GuiTkinterController:
    MAIN_COLOR = '#7698cb'
    MAIN_GEOMETRY = '610x610'

    def __init__(self, f1_print, f2_create_table, f3_drop_table, f4_open_excel_file_path):
        self.function1 = f1_print
        self.function2 = f2_create_table
        self.function3 = f3_drop_table
        self.function4 = f4_open_excel_file_path

        self.root = Tk()
        create_main_window(self.root, self.MAIN_GEOMETRY)

        self.f1, self.f2, self.f3, self.f4 = create_frames(self.root, self.MAIN_COLOR)
        self.f1.config(bg='white')

        self.label1 = create_a_label(self.f1, "db control")
        self.label1.grid(row=0, column=0, columnspan=2)

        self.entry1 = Entry(self.f1, width=20)
        self.entry1.grid(row=1, column=0)

        self.entry2 = create_an_entry(self.f1)
        self.entry2.grid(row=2, column=0)

        self.entry3 = create_an_entry(self.f1)
        self.entry3.grid(row=3, column=0)

        self.entry4 = create_an_entry(self.f1)
        self.entry4.grid(row=4, column=0)

        # f1_print
        self.button1 = create_a_button(self.f1, 'print', self.get1)
        self.button1.grid(sticky="W", row=1, column=1)
        self.button1.config(bg='light grey')

        # f2_create_table
        self.button2 = create_a_button(self.f1, 'create table', self.get2)
        self.button2.grid(sticky="W", row=2, column=1)
        self.button2.config(bg='light grey')

        # f3_drop_table
        self.button3 = create_a_button(self.f1, 'delete table', self.get3)
        self.button3.grid(sticky="W", row=3, column=1)
        self.button3.config(bg='light grey')

        # f4_open_excel_file_path
        self.button4 = create_a_button(self.f1, 'load excel', self.get4)
        self.button4.grid(sticky="W", row=4, column=1)
        self.button4.config(bg='light grey')

    def printer_function(self, query):
        query_label = create_a_label(self.f4, query)
        query_label.config(width=42, height=5, bg='white')
        query_label.place(x=0, y=0)

    def get1(self):
        query = self.function1(self.entry1.get())
        self.entry1.delete(0, END)
        self.printer_function(query)

    def get2(self):
        query = self.function2(self.entry2.get())
        self.entry2.delete(0, END)
        self.printer_function(query)

    def get3(self):
        query = self.function3(self.entry3.get())
        self.entry3.delete(0, END)
        self.printer_function(query)

    def get4(self):
        query = self.function4(self.entry4.get())
        self.entry4.delete(0, END)
        self.printer_function(query)

    def mainloop(self):
        self.root.mainloop()
