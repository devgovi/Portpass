# Govine-J
# GITS
# 2022-06-04
import sqlite3
from sqlite3 import Error


def portpass_db_con() -> sqlite3.Connection:
    """ create a database connection to the SQLite database"""
    try:
        return sqlite3.connect('test/database/test_portpass.db')
    except Error as e:
        with open('sources/log/error.log', 'a') as f:
            f.writelines(f'{e}\n')


