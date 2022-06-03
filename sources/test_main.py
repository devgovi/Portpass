# Govine-J
# GITS
# 2022-06-02
# Put together all the functions in the main.py file.
# Test the functions in the main.py file.
from userData import UserData
from dbManager import DBManager as db
from dbManager import del_all_data


# Create a new user data object.
facebook = UserData("Govine-J", "12345678", "facebook.com", "Hello world", "#social #media")

instagram = UserData("King Dod", "mySafePass", "instagram.com", "Hello world this is a note", "#social #media")

gmail = UserData("Jamaica", "12345678", "gmail.com", "Hello world", "#email #work #media")

linkedin = UserData("China", "12345678", "linkedin.com", "This is an note", "#social #media")
figma = UserData("Africa", "12345678", "figma.com", "Create cool UI.", "#social #media #design")


# ADD DATA TO DATABASE - userData table. - START
# facebook.insert_data()
# instagram.insert_data()
# gmail.insert_data()
# linkedin.insert_data()
# figma.insert_data()
# ADD DATA TO DATABASE - userData table. - END

# GET ALL DATA FROM THE DATABASE - userData table. - START
# all_data = db(instagram.get_username(), instagram.get_website()).get_all_data()
# print(all_data)
# GET ALL DATA FROM THE DATABASE - userData table. - END


# GET A SPECIFIC DATA FROM THE DATABASE - userData table. - START
# get_specific_data = db(gmail.get_username(), gmail.get_website()).get_data()
# print(get_specific_data)
# GET A SPECIFIC DATA FROM THE DATABASE - userData table. - END


# DELETE A SPECIFIC DATA FROM THE DATABASE - userData table. - START
# del_specific_data = db(facebook.get_username(), facebook.get_website()).del_data()
# DELETE A SPECIFIC DATA FROM THE DATABASE - userData table. - END


# DELETE ALL DATA FROM THE DATABASE - userData table. - START
# del_all_data()
# DELETE ALL DATA FROM THE DATABASE - userData table. - END


# UPDATE USERNAME - userData table. - START
# db(facebook.get_username(), facebook.get_website()).edit_username("New Govine-J")
# UPDATE USERNAME - userData table. - END


# UPDATE WEBSITE - userData table. - START
# db(instagram.get_username(), instagram.get_website()).edit_website("new.instagram.com")
# UPDATE WEBSITE - userData table. - END


# UPDATE PASSWORD - userData table. - START
# db(gmail.get_username(), gmail.get_website()).edit_password("newGmailPassword")
# UPDATE PASSWORD - userData table. - END


# UPDATE NOTES - userData table. - START
# db(linkedin.get_username(), linkedin.get_website()).edit_note("This is a new note")
# UPDATE NOTES - userData table. - END



# UPDATE TAGS - userData table. - START
# db(figma.get_username(), figma.get_website()).edit_tag("#Ui #Ux #Design #Color")
# UPDATE TAGS - userData table. - END