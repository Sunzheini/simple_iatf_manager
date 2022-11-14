from database_app.database_controller import DatabaseController


def new():
    new_database = DatabaseController(
        database_name,
        table_name,
        table_structure,
    )
    new_database.create_database_and_table()
    return new_database


def remove(database):
    database.drop_table(table_name)


database_name = 'simple_iatf_database.db'
table_name = 'rrr'
table_structure = {
    'process_number': 'text',
    'process_responsible': 'integer',
}


# new_database = DatabaseController(
#     database_name,
#     table_name,
#     table_structure,
#     )
database = new()
remove(database)

# new_database.drop_table(table_name)
