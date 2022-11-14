from database_app.database_controller import DatabaseController
from database_app.table_specification import Table


database_name = 'simple_iatf_database.db'
table_name = 'sss'
table_structure = {
    'process_number': 'text',
    'process_responsible': 'integer',
}

#
# new_database = DatabaseController(database_name, table_name)
# new_database.create_database_and_table()
#
# # new_database.drop_table(table_name)

dd = {
    'process_number': 'text',
    'process_responsible': 'integer',
}

table = Table(dd)
print(table.column_names_and_types)
