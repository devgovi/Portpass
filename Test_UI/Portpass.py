# Govine-J
# GITS
# 2022-06-07
import os
from app_config import (MASTER_PASS_FILE, MASTER_KEY_FILE, DB_PATH)
from setupScreen import SetupScreen



if os.path.exists(MASTER_PASS_FILE) or os.path.exists(MASTER_KEY_FILE) or os.path.exists(DB_PATH):
    print("The application is already setup.")
else:
    print("The application is not setup.")
    SetupScreen().mainloop()
    