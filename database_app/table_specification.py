from abc import ABC


class Table(ABC):
    def __init__(self, dictz):
        self.column_names_and_types = dictz








# create_table = """
#             CREATE TABLE IF NOT EXISTS processes(
#             first_name text,
#             last_name text,
#             address text,
#             zipcode integer
#             )
#         """
#
# drop_table = "DROP TABLE processes;"
