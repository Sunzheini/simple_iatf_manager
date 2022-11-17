from database_app.db_controller import DatabaseController
from gui_tkinter.gui_tkinter_controller import GuiTkinterController


database_name_definition = 'simple_iatf_database.db'

table_structure_definition = {
    'process': 'text',
    'subprocess': 'text',
    'step_number': 'text',
    'step_name': 'text',
    'step_text': 'text',
    'step_responsible': 'text',
    'step_evidence': 'text',
    'from_process': 'text',
    'input_element': 'text',
    'to_process': 'text',
    'output_element': 'text',
    }

query_requirements = {
    'options1': ['processes', 'processes2', 'processes3'],
    'options2': ['Yes', 'No'],
    'options3': ['process',
            'subprocess',
            'step_number',
            'step_name',
            'step_text',
            'step_responsible',
            'step_evidence',
            'from_process',
            'input_element',
            'to_process',
            'output_element'],
    'options4': ['process',
            'subprocess',
            'step_number',
            'step_name',
            'step_text',
            'step_responsible',
            'step_evidence',
            'from_process',
            'input_element',
            'to_process',
            'output_element'],
    'options5': ['1', '2', '3'],
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

    def f4_open_excel(table_name):
        file_path = new_database.load_from_excel(table_name)
        return file_path

    def f5_empty_table(table_name):
        result = new_database.empty_table(table_name)
        return result

    def f6_display_processes(table_name):
        result = new_database.display_processes(table_name)
        return result

    def f7_get_spec_info(
            table_name,
            is_distinct,
            target_column_name,
            condition_column_name,
            condition_column_value
    ):
        result = new_database.get_specific_process_info(
            table_name,
            is_distinct,
            target_column_name,
            condition_column_name,
            condition_column_value
        )
        return result

    new_database = DatabaseController(database_name)
    new_gui = GuiTkinterController(
        f1_print,
        f2_create,
        f3_drop,
        f4_open_excel,
        f5_empty_table,
        f6_display_processes,
        f7_get_spec_info,
        query_requirements,
    )
    new_gui.mainloop()


if __name__ == '__main__':
    main()
