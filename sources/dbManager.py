# Govine-J
# GITS
# 2022-06-02
import pandas as pd
from connectDB import portpass_db_con
import os
from app_config import ( DB_PATH, USER_ID_FILE,
                        EXPORTED_FILE, MODIFIED_DATE)


# Invoke the database connection. -START
con = portpass_db_con()
# Invoke the database connection. -END


class DBManager:
    """
    Manage the modification of the database.
    """
    def __init__(self, entryId:int):
        """ Initialize the class. 
        Args:
            entryId: The unique id for each entry.
        """
        self.entryId = entryId
    
    
    def get_last_entryId(self) -> int:
        """
        Return the last entryId.

        Returns:
            int: entryId of the data entered.
        """
        # data = con.cursor().execute("SELECT entryId FROM userData ORDER BY entryId DESC LIMIT 1")
        
        
        
    def exists(self) -> bool:
        """
        Check if the user exists in the database.

        Returns:
            bool: True if the user exists in the database. False otherwise.
        """
        data = con.cursor().execute(f"SELECT entryId FROM userData WHERE entryId='{self.entryId}'")
        if data.fetchone() is not None:
            return True
        return False


    def edit_username(self, new_username:str) -> None:
        """
        update username of the entryId.

        Args:
            new_username: new username of the user.
        """
        # validate data:
        if new_username == '' or new_username is None:
            print("Please enter a valid username.")
        else:
            if self.exists() is True:
                con.cursor().execute(f"UPDATE userData SET username='{new_username}' WHERE entryId='{self.entryId}'")

                # Update the dateModified field.
                con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE entryId='{self.entryId}'")
                con.commit()
                print("Username updated.")
            else:
                print("Unable to update username.")


    def edit_website(self, new_website:str) -> None:
        """
        update website of the entryId.

        Args:
            new_website: new website of the user.
        """
        if new_website == '' or new_website is None:
            print("Please enter a valid website.")
        else:
            if self.exists() is True:
                con.cursor().execute(f"UPDATE userData SET website='{new_website}' WHERE entryId='{self.entryId}'")
                # Update the dateModified field.
                con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE entryId='{self.entryId}'")
                con.commit()
                print("Website updated.")
            else:
                print("Unable to update website.")


    def edit_password(self, new_password:str) -> None:
        """
        Update password of the user.

        Args:
            new_password: new password of the entryId.
        """
        if new_password == '' or new_password is None:
            print("Please enter a valid password.")
        else:
            if self.exists() is True:
                con.cursor().execute(f"UPDATE userData SET password='{new_password}' WHERE entryId='{self.entryId}'")
                # Update the dateModified field.
                con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE entryId='{self.entryId}'")
                con.commit()
                print("Password updated.")
            else:
                print("Unable to update password.")


    def edit_note(self, new_note:str) -> None:
        """
        edit note of the user.

        Args:
            new_note: new note of the entryId.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET notes='{new_note}' WHERE entryId='{self.entryId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE entryId='{self.entryId}'")
            con.commit()
            print("Note updated.")
        else:
            print("Unable to update note.")


    def edit_tag(self, new_tag:str) -> None:
        """
        edit tag of the user.

        Args:
            new_tag: new tag of the entryId.
        """
        if self.exists() is True:
            con.cursor().execute(f"UPDATE userData SET tags='{new_tag}' WHERE entryId='{self.entryId}'")
            # Update the dateModified field.
            con.cursor().execute(f"UPDATE userData SET dateModified='{MODIFIED_DATE}' WHERE entryId='{self.entryId}'")
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
            data = con.cursor().execute(f"SELECT * FROM userData WHERE entryId='{self.entryId}'")
            return data.fetchall()
        else:
            print('Unable to get specified data.')


    def del_data(self) -> None:
        """
        Delete user data from the database.
        """
        if self.exists() is True:
            con.cursor().execute(f"DELETE FROM userData WHERE entryId='{self.entryId}'")
            con.commit()
            print("Data deleted.")
        else:
            print("Unable to delete data.")















def update_entryId_file(entryId:int) -> None:
    """
    Update the entryId file.

    Args:
        userId: new entryId.
    """
    with open(USER_ID_FILE, 'w') as f:
        f.write(str(entryId))


def del_all_data() -> None:
    """
    Delete all user data from the database.
    """
    
    con.cursor().execute("DELETE FROM userData")
    if con.cursor().fetchall() is not None:
        # Delete the userId.txt file.
        try:
            if os.path.exists(USER_ID_FILE):
                os.remove(USER_ID_FILE)
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


def export_data() -> None:
    """
    Export all user data from the database to a csv file.
    """
    if os.path.exists(DB_PATH):    
        df = pd.read_sql_query("SELECT * FROM userData", con)
        df.to_csv(EXPORTED_FILE, index=False)
        print("Data exported.")
    else:
        print("Unable to export data.")


def import_data() -> None:
    """
    Append data from userData.csv to the database and update the entryId file. 
    """
    if os.path.exists(EXPORTED_FILE):
        
        # Load the data from the csv file.- START
        df = pd.read_csv(EXPORTED_FILE)
        # Load the data from the csv file.- END
        
        # Check is database is empty. - START
        data = con.cursor().execute("SELECT * FROM userData")
        if data.fetchone() is None:
        # Check is database is empty. - END
            
            # Writing the data to the database. - START
            df.to_sql('userData', con, if_exists='append', index=False)
            print("Data imported.")
            # Writing the data to the database. - END
            
            # Get the last entryId. - START
            last_entryId = df.entryId.max()
            # Get the last entryId. - END
            
            # Update the entryId.txt file. - START
            update_entryId_file(last_entryId)
            # Update the entryId.txt file. - END
        
        else:
            # Read the last row of the database. - START
            entryId = con.cursor().execute("SELECT entryId FROM userData ORDER BY entryId DESC LIMIT 1")
            current_entryId = int(entryId.fetchone()[0])
            # Read the last row of the database. - END
            
            # Update the entryId. - START
            new_entryId = 1    
            for index in df.index:
                if index >= current_entryId:
                    df.loc[index, 'entryId'] = new_entryId + current_entryId
                else:
                    df.loc[index, 'entryId'] = current_entryId + new_entryId
                    new_entryId += 1
                # Update the entryId. - END
                
            
            # Append the data to the database. - START
            df.to_sql('userData', con, if_exists='append', index=False)
            print("Data imported.")
            # Append the data to the database. - END
        
            # Update the entryId.txt file. - START
            update_entryId_file(current_entryId + new_entryId)
            # Update the entryId.txt file. - END
            
    else:
        print("Unable to import data.")