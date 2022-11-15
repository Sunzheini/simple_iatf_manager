import random
from tkinter import *
from gui_tkinter.gui_tkinter_functions import create_main_window, create_frames, create_a_label, create_a_button, \
    create_an_entry
from process_app import process_code_generator


class GuiTkinterController:
    MAIN_COLOR = '#7698cb'
    MAIN_GEOMETRY = '610x610'

    def __init__(self,
                 f1_print,
                 f2_create_table,
                 f3_drop_table,
                 f4_open_excel_file_path,
                 f5_empty_table,
                 f6_display_processes):

        self.function1 = f1_print
        self.function2 = f2_create_table
        self.function3 = f3_drop_table
        self.function4 = f4_open_excel_file_path
        self.function5 = f5_empty_table
        self.function6 = f6_display_processes

        self.root = Tk()
        create_main_window(self.root, self.MAIN_GEOMETRY)

        self.f1, self.f2, self.f3, self.f4 = create_frames(self.root, self.MAIN_COLOR)
        self.f1.config(bg='white')
        self.f3.config(bg='white')

# db control layout
# ------------------------------------------------------------------------------------
        self.label_f1 = create_a_label(self.f1, "db control")
        self.label_f1.grid(row=0, column=0, columnspan=2)

        self.entry1_f1 = Entry(self.f1, width=20)
        self.entry1_f1.grid(row=1, column=0)

        self.entry2_f1 = create_an_entry(self.f1)
        self.entry2_f1.grid(row=2, column=0)

        self.entry3_f1 = create_an_entry(self.f1)
        self.entry3_f1.grid(row=3, column=0)

        self.entry4_f1 = create_an_entry(self.f1)
        self.entry4_f1.grid(row=4, column=0)

        self.entry5_f1 = create_an_entry(self.f1)
        self.entry5_f1.grid(row=5, column=0)

        # f1_print
        self.button1_f1 = create_a_button(self.f1, 'print', self.get1)
        self.button1_f1.grid(sticky="W", row=1, column=1)
        self.button1_f1.config(bg='light grey')

        # f2_create_table
        self.button2_f1 = create_a_button(self.f1, 'create table', self.get2)
        self.button2_f1.grid(sticky="W", row=2, column=1)
        self.button2_f1.config(bg='light grey')

        # f3_drop_table
        self.button3_f1 = create_a_button(self.f1, 'delete table', self.get3)
        self.button3_f1.grid(sticky="W", row=3, column=1)
        self.button3_f1.config(bg='light grey')

        # f4_open_excel_file_path
        self.button4_f1 = create_a_button(self.f1, 'load excel', self.get4)
        self.button4_f1.grid(sticky="W", row=4, column=1)
        self.button4_f1.config(bg='light grey')

        # f5_empty_table
        self.button5_f1 = create_a_button(self.f1, 'empty table', self.get5)
        self.button5_f1.grid(sticky="W", row=5, column=1)
        self.button5_f1.config(bg='light grey')

# process control layout
# ------------------------------------------------------------------------------------

        self.label1_f2 = create_a_label(self.f3, "process control")
        self.label1_f2.grid(row=0, column=0, columnspan=2)

        self.entry1_f2 = Entry(self.f3, width=20)
        self.entry1_f2.grid(row=1, column=0)

        # f6
        self.button1_f2 = create_a_button(self.f3, 'process list', self.get6)
        self.button1_f2.grid(sticky="W", row=1, column=1)
        self.button1_f2.config(bg='light grey')

# db control methods
# ------------------------------------------------------------------------------------

    def test_func(self):
        result = random.randint(1, 100)
        self.printer_function(result)
        print(result)

    def printer_function(self, query):
        query_label = create_a_label(self.f4, query)
        query_label.config(width=42, height=20, bg='light green')
        query_label.place(x=0, y=0)
        query_label.place(x=0, y=0)

    def get1(self):
        query = self.function1(self.entry1_f1.get())
        self.entry1_f1.delete(0, END)
        self.printer_function(query)

    def get2(self):
        query = self.function2(self.entry2_f1.get())
        self.entry2_f1.delete(0, END)
        self.printer_function(query)

    def get3(self):
        query = self.function3(self.entry3_f1.get())
        self.entry3_f1.delete(0, END)
        self.printer_function(query)

    def get4(self):
        query = self.function4(self.entry4_f1.get())
        self.entry4_f1.delete(0, END)
        self.printer_function(query)

    def get5(self):
        query = self.function5(self.entry5_f1.get())
        self.entry5_f1.delete(0, END)
        self.printer_function(query)

# process control methods
# ------------------------------------------------------------------------------------

    def get6(self):
        query = self.function6(self.entry1_f2.get())
        self.entry1_f2.delete(0, END)
        self.printer_function(query)

        result = process_code_generator.display_processes_formatter(query)

        for idx in range(len(result)):
            current_button = create_a_button(self.f2, result[idx], self.process_menu)
            current_button.config(width=35, height=1, bg='light grey', anchor=W)
            current_button.pack()

    def process_menu(self):
        new_window2 = Toplevel()

        # ToDo: continue here - what to take from db and to display

# ------------------------------------------------------------------------------------
    def mainloop(self):
        self.root.mainloop()
