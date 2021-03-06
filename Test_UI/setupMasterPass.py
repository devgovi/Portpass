# Govine-J
# GITS
# 2022-06-07
# Call when lunching the application for the first time.
from cryptoManager import create_key
from app_config import MASTER_PASS_FILE
from cryptoManager import encrypt_password, read_key



def isSecure(masterPass:str) -> bool:
    """
    Checks if the master password is secure.

    Args:
        masterPass (str): The password to be checked.

    Returns:
        bool: True if the password is secure, False otherwise.
    """
    if len(masterPass) >= 8:
        # create the master key
        create_key()
        return True
    else:
        return False



def takeMasterPass(masterPass:str) -> bool:
    """
    Takes the master password from the user and store it in the key folder.
    
    Args:
        masterPass (str): The master password to be stored.
    """

    if isSecure(masterPass):
        password = encrypt_password(read_key(), masterPass)
        with open(MASTER_PASS_FILE, 'wb') as f:
            f.write(password)
        # print("Master password stored.")
        return True
    else:
        # print("Master password is not secure.\nTry again.")
        return False



# takeMasterPass(input("Enter the master password: "))
