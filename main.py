from database_app.database_controller import DatabaseController
from gui_tkinter.gui_tkinter_controller import GuiTkinterController


database_name_definition = 'simple_iatf_database.db'
table_structure_definition = {
        'process_number': 'text',
        'process_responsible': 'integer',
    }


def main():
    database_name = database_name_definition
    table_structure = table_structure_definition

    def f1(message):
        print(message)
        return message

    def f2(message):
        result = new_database.create_database_and_table(message, table_structure)
        return result

    def f3(message):
        result = new_database.drop_table(message)
        return result

    new_database = DatabaseController(database_name)
    new_gui = GuiTkinterController()
    new_gui.start(
        f1, f2, f3
    )


if __name__ == '__main__':
    main()
