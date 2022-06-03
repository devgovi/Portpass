# Govine-J
# GITS
# 2022-06-01
import sqlite3
from sqlite3 import Error


def portpass_db_con() -> sqlite3.Connection:
    try:
        return sqlite3.connect('sources/database/portpass.db')
    except Error as e:
        with open('sources/log/error.log', 'a') as f:
            f.writelines(f'{e}\n')
