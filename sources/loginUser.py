# Govine-J
# GITS
# 2022-06-07
# Call this function when the user wants to login.

import os
from app_config import MASTER_PASS_FILE
from cryptoManager import decrypt_password, read_key


def login(password:str) -> bool:
    """
    Check if the password is correct, then return True.
    
    Args:
        password (str): The password to be checked.
    
    Returns:
        bool: True if the password is correct, False otherwise.
    """
    if os.path.exists(MASTER_PASS_FILE):
        
        # Get the master password from the key folder. - START
        with open(MASTER_PASS_FILE, 'rb') as f:
            master_pass = f.read()
        stored_password = decrypt_password(read_key(), master_pass)
        # Get the master password from the key folder. - END
        
        # Check if the password is correct. - START
        if password == stored_password:
            print("Login successful.")
            return True
        else:
            print("Login failed.")
            return False
        # Check if the password is correct. - END
    
    else:
        print("Master password file does not exist.")
        return False
        

# login(input("Enter the master password: "))