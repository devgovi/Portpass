# Govine-J
# GITS
# 2022-06-02
from test_connectDB import portpass_db_con
from datetime import datetime
import os

MODIFIED_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Invoke the database connection. -START
con = portpass_db_con()
# Invoke the database connection. -END

class DBManager:
    """
    Manage the modification of the database.
    """
    def __init__(self, userId:int):
        """ Initialize the class. 
        Args:
            userId: The unique id for each entry.
        """
        self.userId = userId
        
    def exists(self) -> bool:
        """
        Check if the user exists in the database.

        Returns:
            bool: True if the user exists in the database. False otherwise.
        """
        data = con.cursor().execute(f"SELECT userId FROM userData WHERE userId='{self.userId}'")
        if data.fetchone() is not None:
            return True
        return False


    def edit_username(self, new_username:str) -> None:
        """
        update username of the userId.

        Args:
            new_username: new username of the user.
        """
        
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET username='{new_username}' WHERE userId='{self.userId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE userId='{self.userId}'")
            con.commit()
            print("Username updated.")
        else:
            print("Unable to update username.")


    def edit_website(self, new_website:str) -> None:
        """
        update website of the userId.

        Args:
            new_website: new website of the user.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET website='{new_website}' WHERE userId='{self.userId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE userId='{self.userId}'")
            con.commit()
            print("Website updated.")
        else:
            print("Unable to update website.")


    def edit_password(self, new_password:str) -> None:
        """
        Update password of the user.

        Args:
            new_password: new password of the userId.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET password='{new_password}' WHERE userId='{self.userId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE userId='{self.userId}'")
            con.commit()
            print("Password updated.")
        else:
            print("Unable to update password.")


    def edit_note(self, new_note:str) -> None:
        """
        edit note of the user.

        Args:
            new_note: new note of the userId.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET notes='{new_note}' WHERE userId='{self.userId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE userId='{self.userId}'")
            con.commit()
            print("Note updated.")
        else:
            print("Unable to update note.")


    def edit_tag(self, new_tag:str) -> None:
        """
        edit tag of the user.

        Args:
            new_tag: new tag of the userId.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET tags='{new_tag}' WHERE userId='{self.userId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE userId='{self.userId}'")
            con.commit()
            print("Tag updated.")
        else:
            print("Unable to update tag.")


    def get_data(self) -> list:
        """
        Return user data from the database.

        Returns:
            list: user data from the database.
        """
        if self.exists() is True:
            data = con.cursor().execute(f"SELECT * FROM userData WHERE userId='{self.userId}'")
            return data.fetchall()
        else:
            print('Unable to get specified data.')


    def del_data(self) -> None:
        """
        Delete user data from the database.
        """
        if self.exists() is True:
            con.cursor().execute(f"DELETE FROM userData WHERE userId='{self.userId}'")
            con.commit()
            print("Data deleted.")
        else:
            print("Unable to delete data.")



def del_all_data() -> None:
    """
    Delete all user data from the database.
    """
    
    con.cursor().execute("DELETE FROM userData")
    if con.cursor().fetchall() is not None:
        # Delete the userId.txt file.
        try:
            if os.path.exists('test/database/userId.txt'):
                os.remove('test/database/userId.txt')
        finally:
            con.commit()
            print("All data deleted.")
    else:
        print("No data found.")


def get_all_data() -> list:
        """
        Return all user data from the database.

        Returns:
            list: user data from the database.
        """
        all_user = con.cursor().execute("SELECT * FROM userData")
        if all_user.fetchone() is not None:
            return all_user.fetchall()
        else:
            print("No data found.")