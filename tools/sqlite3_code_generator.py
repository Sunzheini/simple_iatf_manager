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
    create_table = f"CREATE TABLE IF NOT EXISTS {table_name}(\n"
    for x, y in dd.items():
        create_table += f"{x} {y},\n"
    create_table += ")"
    create_table = create_table.replace('integer,', 'integer')
    return create_table.strip()


# Drop table
# ---------------------------------------------------------#

# example: "DROP TABLE processes;"
drop_table = f"DROP TABLE "


# ---------------------------------------------------------#
