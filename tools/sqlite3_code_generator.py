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


# ---------------------------------------------------------#
