# Govine-J
# GITS
# 2022-06-01
from app_config import (USER_ID_FILE, CURRENT_DATE)
from test_connectDB import portpass_db_con



con = portpass_db_con()

class UserData:
    """
    Create a user data object, then inserts the data into
    the portpass database at the userData table.
    
    NOTE:
    Before any data is inserted, the program query with the 
    database to see if the username and website already exists.
    If the query is true the data will not get commit to the
    database.
    
    """
    def __init__(self, username:str, password:str, website:str, notes:str=None, tags:str=None):  
        """
        Initialize the AddData class.
        
        Args:
            username: username of the user.
            password: password of the user.
            website: website of the user.
            notes: notes of the user.
            tags: tags of the user.
        """
        self.username = username
        self.password = password
        self.website = website
        self.notes = notes
        self.tags = tags
        self.create_entry_id()
    
    
    
    def exists(self) -> bool:
        """
        Check if the user exists in the database.

        Returns:
            bool: True if the user exists in the database. False otherwise.
        """
        data = con.cursor().execute(f"SELECT userId FROM userData WHERE userId='{self.user_id}'")
        if data.fetchone() is not None:
            return True
        return False


    def valid_data(self) -> bool:
        """
        Validate the data before inserting into the database.
        """
        if self.username == '' or self.username is None:
            print("Unable to add data. Please fill in username field.")
            return False
        elif self.password == '' or self.password is None:
            print("Unable to add data. Please fill in password field.")
            return False
        elif self.website == '' or self.website is None:
            print("Unable to add data. Please fill in website field.")
            return False
        return True
    
    
    def insert_data(self) -> None:
        # write the pervious user id to the userId.txt file.
        with open(USER_ID_FILE, "w") as f:
            f.write(str(self.user_id + 1))
        user_id = self.user_id
        username = self.username
        password = self.password
        website = self.website
        notes = self.notes
        tags = self.tags
        date = CURRENT_DATE
        
        if self.exists() is False:
            con.cursor().execute(f"INSERT INTO userData (userId, username, password, website, notes, tags, dateCreated) VALUES ('{user_id}', '{username}', '{password}', '{website}', '{notes}', '{tags}', '{date}')")
            con.commit()
            print(f"\n{username}'s data has been added to the database.")
        else:
            print(f'Unable to add data. The userId: {self.user_id} already exists.')


    def create_entry_id(self) -> None:
        """ 
        Create a id for each entry,
        then insert the data into the database. 
        """
        if  self.valid_data() is True:
            try:
                with open(USER_ID_FILE, "r") as f:
                    self.user_id = int(f.read())
                self.insert_data()
            except FileNotFoundError:
                with open(USER_ID_FILE, 'w') as f:
                    f.write('0')
                self.user_id = 0
                self.insert_data()

