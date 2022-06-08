# Govine-J
# GITS
# 2022-06-06
from datetime import datetime


DB_PATH = 'sources/data/sql/portpass.db'
USER_ID_FILE = 'sources/data/sql/entryId.txt'
EXPORTED_FILE = 'sources/data/out/keep_safe.csv'
MASTER_PASS_FILE = 'sources/data/key/masterPass'
MASTER_KEY_FILE = 'sources/data/key/master.key'
LOG_FILE = 'sources/data/log/error.txt'

CURRENT_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
MODIFIED_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")