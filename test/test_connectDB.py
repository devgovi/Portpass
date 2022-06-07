# Govine-J
# GITS
# 2022-06-04
import sqlite3
from sqlite3 import Error

from app_config import (DB_PATH, LOG_FILE, CURRENT_DATE)



def portpass_db_con() -> sqlite3.Connection:
    """ create a database connection to the SQLite database"""
    try:
        return sqlite3.connect(DB_PATH)
    except Error as e:
        with open(LOG_FILE, 'a') as f:
            f.writelines(f'{e} || {CURRENT_DATE}\n')


