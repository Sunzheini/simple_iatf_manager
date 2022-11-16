# Create table
# ---------------------------------------------------------#

# example: CREATE TABLE IF NOT EXISTS processes(
#             first_name text,
#             last_name text,
#             address text,
#             zipcode integer       # no comma!
#             )
#         """
def create_table_string(table_name, dd):
    create_table = f"CREATE TABLE IF NOT EXISTS {table_name}("
    for x, y in dd.items():
        create_table += "\n"
        create_table += f"{x} {y},"
    create_table = create_table.rstrip(',')
    create_table += "\n"
    create_table += ")"
    # create_table = create_table.replace('integer,', 'integer')
    return create_table.strip()


# Drop table
# ---------------------------------------------------------#

# example: "DROP TABLE processes;"
drop_table = f"DROP TABLE "


# Insert single row into table
# ---------------------------------------------------------#
# "INSERT INTO addresses VALUES (:f_name, :l_name, :address, :zipcode)",
#               {
#                   'f_name': f_name.get(),
#                   'l_name': l_name.get(),
#                   'address': address.get(),
#                   'zipcode': zipcode.get(),
#               }

def insert_single_row(table_name, values):
    to_be_inserted = values
    for i in range(len(to_be_inserted)):
        if to_be_inserted[i] is None:
            to_be_inserted[i] = 'Blank'
    to_be_inserted = tuple(to_be_inserted)

    insert_into_table = f"INSERT INTO {table_name} VALUES {to_be_inserted}"

    return insert_into_table


# Empty table
# ---------------------------------------------------------#

def empty_table(table_name):
    empty = f"DELETE FROM {table_name}"
    return empty


# Get process list
# ---------------------------------------------------------#

def get_process_list(table_name):
    # command = f"SELECT process FROM {table_name} WHERE step_number = '1'"
    command = f"SELECT DISTINCT process FROM {table_name}"
    return command


# Get specific info
# ---------------------------------------------------------#

def fetch_specific_info(
        table_name,
        is_distinct,
        target_column_name,
        condition_column_name,
        condition_column_value):
    command = ''
    if is_distinct:
        command = f"SELECT DISTINCT {target_column_name} FROM {table_name} WHERE {condition_column_name} = '{condition_column_value}'"
        print(command)
    else:
        command = f"SELECT {target_column_name} FROM {table_name} WHERE {condition_column_name} = '{condition_column_value}'"
        print(command)
    return command
