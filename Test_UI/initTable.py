# Govine-J
# GITS
# 2022-06-01
# Use to initialize the database tables.
from connectDB import portpass_db_con as con


def init_table(con):
    """Use to initialize the database tables.

    Args:
        con (connection object): _description_
    """
    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE userData( entryId int, username text, password text, website text, notes text, tags text, dateCreated date, dateModified date)")

    con.commit()
    print("Database and Table created successfully.")


# RUN ONCE IS DATABASE DON'T EXISTS
# init_table(con())