# Govine-J
# GITS
# 2022-06-04
import sqlite3
from sqlite3 import Error
import os
from app_config import (DB_PATH, LOG_FILE, CURRENT_DATE)



def portpass_db_con() -> sqlite3.Connection:
    """ create a database connection to the SQLite database"""
    try:
        return sqlite3.connect(DB_PATH)
    except Error as e:
        if os.path.exists(LOG_FILE) is False:
            with open(LOG_FILE, 'w') as f1:
                f1.write(f"{CURRENT_DATE} - {e}\n")
        else:           
            with open(LOG_FILE, 'a') as f2:
                f2.write(f"{CURRENT_DATE} - {e}\n")


