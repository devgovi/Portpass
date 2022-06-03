# Govine-J
# GITS
# 2022-06-02
from connectDB import portpass_db_con
from datetime import datetime

MODIFIED_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Invoke the database connection. -START
con = portpass_db_con()
# Invoke the database connection. -END

class DBManager:
    """
    Manage the modification of the database.
    """
    def __init__(self, username:str, website:str):
        """
        Initialize the DBManager class.

        Args:
            username: username of the user.
            website: website of the user.
        """
        self.username = username
        self.website = website
    
        
    def exists(self) -> bool:
        """
        Check if the user exists in the database.

        Returns:
            bool: True if the user exists in the database. False otherwise.
        """
        data = con.cursor().execute(f"SELECT * FROM userData WHERE username='{self.username}' AND website='{self.website}'")
        if data.fetchone() is not None:
            return True
        return False


    def edit_username(self, new_username:str) -> None:
        """
        edit username of the user.

        Args:
            new_username: new username of the user.
        """
        
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET username='{new_username}' WHERE username='{self.username}' AND website='{self.website}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE username='{self.username}' AND website='{self.website}'")
            con.commit()
            print("Username updated.")
        else:
            print("Unable to update username.")


    def edit_website(self, new_website:str) -> None:
        """
        edit website of the user.

        Args:
            new_website: new website of the user.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET website='{new_website}' WHERE username='{self.username}' AND website='{self.website}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE username='{self.username}' AND website='{self.website}'")
            con.commit()
            print("Website updated.")
        else:
            print("Unable to update website.")


    def edit_password(self, new_password:str) -> None:
        """
        edit password of the user.

        Args:
            new_password: new password of the user.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET password='{new_password}' WHERE username='{self.username}' AND website='{self.website}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE username='{self.username}' AND website='{self.website}'")
            con.commit()
            print("Password updated.")
        else:
            print("Unable to update password.")


    def edit_note(self, new_note:str) -> None:
        """
        edit note of the user.

        Args:
            new_note: new note of the user.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET notes='{new_note}' WHERE username='{self.username}' AND website='{self.website}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE username='{self.username}' AND website='{self.website}'")
            con.commit()
            print("Note updated.")
        else:
            print("Unable to update note.")


    def edit_tag(self, new_tag:str) -> None:
        """
        edit tag of the user.

        Args:
            new_tag: new tag of the user.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET tags='{new_tag}' WHERE username='{self.username}' AND website='{self.website}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE username='{self.username}' AND website='{self.website}'")
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
            data = con.cursor().execute(f"SELECT * FROM userData WHERE username='{self.username}' AND website='{self.website}'")
            return data.fetchall()
        else:
            print('Unable to get specified data.')


    def get_all_data(self) -> list:
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


    def del_data(self) -> None:
        """
        Delete user data from the database.
        """
        if self.exists() is True:
            con.cursor().execute(f"DELETE FROM userData WHERE username='{self.username}' AND website='{self.website}'")
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
        con.commit()
        print("All data deleted.")
    else:
        print("No data found.")