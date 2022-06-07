# Govine-J
# GITS
# 2022-06-02
import pandas as pd
from test_connectDB import portpass_db_con
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
        # validate data:
        if new_username == '' or new_username is None:
            print("Please enter a valid username.")
        else:
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
        if new_website == '' or new_website is None:
            print("Please enter a valid website.")
        else:
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
        if new_password == '' or new_password is None:
            print("Please enter a valid password.")
        else:
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















def update_userId_file(userId:int) -> None:
    """
    Update the userId file.

    Args:
        userId: new userId.
    """
    with open(USER_ID_FILE, 'w') as f:
        f.write(str(userId))


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
    Append data from userData.csv to the database and update the userId file. 
    """
    if os.path.exists(DB_PATH):
        
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
            
            # Get the last userId. - START
            last_userId = df.userId.max()
            # Get the last userId. - END
            
            # Update the userId.txt file. - START
            update_userId_file(last_userId)
            # Update the userId.txt file. - END
        
        else:
            # Read the last row of the database. - START
            userId = con.cursor().execute("SELECT userId FROM userData ORDER BY userId DESC LIMIT 1")
            current_userId = int(userId.fetchone()[0])
            # Read the last row of the database. - END
            
            # Update the userId. - START
            new_userId = 1          
            for index in df.index:
                if index >= current_userId:
                    df.loc[index, 'userId'] = new_userId + current_userId
                else:
                    df.loc[index, 'userId'] = current_userId + new_userId
                    new_userId += 1
                # Update the userId. - END
                
            
            # Append the data to the database. - START
            df.to_sql('userData', con, if_exists='append', index=False)
            print("Data imported.")
            # Append the data to the database. - END
        
            # Update the userId.txt file. - START
            update_userId_file(current_userId + new_userId)
            # Update the userId.txt file. - END
            
    else:
        print("Unable to import data.")