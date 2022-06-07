# Govine-J
# GITS
# 2022-06-06
from datetime import datetime


DB_PATH = 'sources/data/portpass.db'
USER_ID_FILE = 'sources/data/entryId.txt'
EXPORTED_FILE = 'sources/data/userData.csv'
LOG_FILE = 'sources/log/error.txt'

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
MODIFIED_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")