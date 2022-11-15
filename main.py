from database_app.database_controller import DatabaseController
from gui_tkinter.gui_tkinter_controller import GuiTkinterController


database_name_definition = 'simple_iatf_database.db'
# table_structure_definition = {
#         'process_number': 'text',
#         'process_responsible': 'integer',
#     }
table_structure_definition = {
    'process_number': 'integer',
    'process_name': 'text',
    'step_number': 'integer',
    'step_name': 'text',
    'step_text': 'text',
    'step_responsible': 'text',
    'step_evidence': 'text',
    'from_process': 'text',
    'input_element': 'text',
    'to_process': 'text',
    'output_element': 'text',
    }


def main():
    database_name = database_name_definition
    table_structure = table_structure_definition

    def f1_print(command):
        print(command)
        return command

    def f2_create(table_name):
        result = new_database.create_database_and_table(table_name, table_structure)
        return result

    def f3_drop(table_name):
        result = new_database.drop_table(table_name)
        return result

    def f4_open_path(table_name):
        file_path = new_database.load_from_excel(table_name)
        return file_path

    new_database = DatabaseController(database_name)
    new_gui = GuiTkinterController(
        f1_print,
        f2_create,
        f3_drop,
        f4_open_path,
    )
    new_gui.mainloop()


if __name__ == '__main__':
    main()
