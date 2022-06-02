# Govine-J
# GITS
# 2022-06-01
from connectDB import portpass_db_con as con
from passGen import pass_generator



class UserData:
    """
    Create then add user data to the portpass database.
    """
    def __init__(self, username:str, password:str, website:str, notes:str, tags:str):
        self.username = username
        self.password = password
        self.website = website
        self.notes = notes
        self.tags = tags


    def exists(self) -> bool:
        pass
    
    def get_username(self) -> str:
        return self.username
    
    def get_password(self) -> str:
        return self.password
    
    def get_website(self) -> str:
        return self.website
    
    def get_notes(self) -> str:
        return self.notes
    
    def get_tags(self) -> str:
        return self.tags
    
    
    def insert_data(self) -> None:
        username = self.get_username()
        password = self.get_password()
        website = self.get_website()
        notes = self.get_notes()
        tags = self.get_tags()
        
        con().cursor().execute(f"INSERT INTO userData VALUES('{username}', '{password}', '{website}', '{notes}', '{tags}')")
        con().commit()





facebook = UserData("Govine-J", pass_generator(0,0,8), "https://www.facebook.com", "This is a note", "#social #facebook")


instagram = UserData("Govine-Jarvis", pass_generator(5,2,3), "https://www.instagram.com", "This is a note", "#social #instagram")


instagram.insert_data()
facebook.insert_data()

