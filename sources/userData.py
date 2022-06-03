# Govine-J
# GITS
# 2022-06-01
from datetime import datetime
from connectDB import portpass_db_con 


CURRENT_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

con = portpass_db_con()

class UserData:
    """
    Create a user data object, then inserts the data into
    the portpass database atr the userData table.
    
    NOTE:
    Before any data is inserted, the program query with the 
    database to see if the username and website already exists.
    If the query is true the data will not get commit to the
    database.
    
    """
    def __init__(self, username:str, password:str, website:str, notes:str, tags:str):
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

 
    def user_exists(self) -> bool:
        """
        Check if the user already exists in the database.
        """
        data = con.cursor().execute(f"SELECT * FROM userData WHERE username='{self.username}' AND website='{self.website}'")
        if data.fetchone() is not None:
            return True
        return False


    def get_username(self) -> str:
        return self.username
 
   
    def get_website(self) -> str:
        return self.website
    
    
    def insert_data(self) -> None:
        username = self.username
        password = self.password
        website = self.website
        notes = self.notes
        tags = self.tags
        date = CURRENT_DATE
        
        if self.user_exists() is False:
            con.cursor().execute(f"INSERT INTO userData (username, password, website, notes, tags, dateCreated) VALUES ('{username}', '{password}', '{website}', '{notes}', '{tags}', '{date}')")
            con.commit()
            print(f"\n{username}'s data has been added to the database.")
        else:
            print(f"\n{username}'s data already exists in the database.")



