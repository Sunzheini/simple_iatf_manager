import random
from functools import wraps
from tkinter import *
from gui_tkinter.gui_tkinter_functions import create_main_window, create_frames, create_a_label, create_a_button, \
    create_an_entry, create_new_window
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
                 f6_display_processes,
                 f7_get_spec_info,
                 query_requirements):

        # functions received from main.py
        # ------------------------------------------------------------------------------------
        self.function1 = f1_print
        self.function2 = f2_create_table
        self.function3 = f3_drop_table
        self.function4 = f4_open_excel_file_path
        self.function5 = f5_empty_table
        self.function6 = f6_display_processes
        self.function7 = f7_get_spec_info

        self.query_requirements = query_requirements

        # root window
        # ------------------------------------------------------------------------------------
        self.root = Tk()
        create_main_window(self.root, self.MAIN_GEOMETRY)

        self.f1, self.f2, self.f3, self.f4 = create_frames(self.root, self.MAIN_COLOR)
        self.f1.config(bg='white')
        self.f3.config(bg='white')

        # process window (window2)
        # ------------------------------------------------------------------------------------
        self.process_window = None
        self.process_window_f1 = None
        self.process_window_f2 = None
        self.process_window_f3 = None
        self.process_window_f4 = None
        self.process_window_f5 = None
        self.process_window_f6 = None
        self.process_window_f7 = None
        self.process_window_f8 = None
        self.process_window_f9 = None

        self.process_window_l1 = None
        self.process_window_l2 = None
        self.process_window_l3 = None
        self.process_window_l4 = None
        self.process_window_l5 = None

        self.process_window_e1 = None
        self.process_window_e2 = None
        self.process_window_e3 = None
        self.process_window_e4 = None
        self.process_window_e5 = None

        self.var1 = None
        self.var2 = None
        self.var3 = None
        self.var4 = None
        self.var5 = None

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

        # ToDo: hardcoded for development
        command = 'processes'
        # query = self.function6(self.entry1_f2.get())
        query = self.function6(command)
        self.entry1_f2.delete(0, END)
        self.printer_function(query)

        result = process_code_generator.display_processes_formatter(query)

        current_column = 0
        for idx in range(len(result)):
            current_button = create_a_button(self.f2, result[idx], self.process_menu)
            current_button.config(width=20, height=1, bg='light grey', anchor=W)
            # current_button.pack()
            current_row = idx
            if idx >= 10:
                current_row -= 10
                current_column = 1
            current_button.grid(row=current_row, column=current_column)

    def process_menu(self):
        self.process_window, \
            self.process_window_f1, \
            self.process_window_f2, \
            self.process_window_f3, \
            self.process_window_f4, \
            self.process_window_f5, \
            self.process_window_f6, \
            self.process_window_f7, \
            self.process_window_f8, \
            self.process_window_f9 = create_new_window()

        # labels
        self.process_window_l1 = create_a_label(self.process_window_f2, "table_name")
        self.process_window_l1.config(width=17)
        self.process_window_l1.grid(row=0, column=0)
        self.process_window_l2 = create_a_label(self.process_window_f2, "is_distinct")
        self.process_window_l2.config(width=17)
        self.process_window_l2.grid(row=1, column=0)
        self.process_window_l3 = create_a_label(self.process_window_f2, "target_column_name")
        self.process_window_l3.config(width=17)
        self.process_window_l3.grid(row=2, column=0)
        self.process_window_l4 = create_a_label(self.process_window_f2, "condition_column_name")
        self.process_window_l4.config(width=17)
        self.process_window_l4.grid(row=3, column=0)
        self.process_window_l5 = create_a_label(self.process_window_f2, "condition_column_value")
        self.process_window_l5.config(width=17)
        self.process_window_l5.grid(row=4, column=0)

        options1 = self.query_requirements['options1']
        options2 = self.query_requirements['options2']
        options3 = self.query_requirements['options3']
        options4 = self.query_requirements['options4']
        options5 = self.query_requirements['options5']  # not used

        self.var1 = StringVar(self.process_window_f2)
        self.var1.set(options1[0])
        dd = OptionMenu(self.process_window_f2, self.var1, *options1)
        dd.grid(row=0, column=1, sticky=W)

        self.var2 = StringVar(self.process_window_f2)
        self.var2.set(options2[0])
        dd = OptionMenu(self.process_window_f2, self.var2, *options2)
        dd.grid(row=1, column=1, sticky=W)

        self.var3 = StringVar(self.process_window_f2)
        self.var3.set(options3[0])
        dd = OptionMenu(self.process_window_f2, self.var3, *options3)
        dd.grid(row=2, column=1, sticky=W)

        self.var4 = StringVar(self.process_window_f2)
        self.var4.set(options4[0])
        dd = OptionMenu(self.process_window_f2, self.var4, *options4)
        dd.grid(row=3, column=1, sticky=W)

        self.process_window_e5 = Entry(self.process_window_f2, width=15)
        self.process_window_e5.grid(row=4, column=1)

        # button to get the info from db
        info_button1 = create_a_button(self.process_window_f2, 'Get info', self.get7)
        info_button1.grid(sticky="W", row=0, column=2)
        info_button1.config(bg='light grey')

    def get7(self):
        query = self.function7(
            self.var1.get(),
            self.var2.get(),
            self.var3.get(),
            self.var4.get(),
            self.process_window_e5.get(),
        )
        self.printer_function(query)

        result = process_code_generator.specific_results_formatter(query)

        # print in the middle of the new window
        query_label = create_a_label(self.process_window_f5, result)
        query_label.config(width=42, height=20, bg='yellow')
        query_label.place(x=0, y=0)
        query_label.place(x=0, y=0)

    # ------------------------------------------------------------------------------------
    def mainloop(self):
        self.root.mainloop()
