# Govine-J
# GITS
# 2022-06-06

from userData import UserData
from dbManager import DBManager as db
from dbManager import (del_all_data, get_all_data,
                            export_data, import_data)
from passGen import pass_generator as pass_gen




# Insert a new user into the database. - START
# jnlive = UserData('greenCash20', pass_gen(5,1,4), 
#                   'www.jnbslive.com',
#                   'This is my online banking website.',
#                   '#banking #online #saving #money')

# github = UserData('devGovi', pass_gen(5,2,4),
#                   'www.github.com',
#                   'This is my github account.',
#                   '#github #developer #python #programming')

# google = UserData('happyFace', pass_gen(8,2,3),
#                   'www.google.com', 'This is my google account.',
#                   '#google #search #searching #email')

# facebook = UserData('Prince James', pass_gen(6,2,3),
#                     'www.facebook.com',
#                     'This is my facebook account.',
#                     '#facebook #social #socialMedia #messenger')

# whatsapp = UserData('+1876555444', pass_gen(0,0,6), 'www.whatsapp.com',
#                     'This is my whatsapp account.','#whatsapp #messenger #social #socialMedia')

# instagram = UserData('goviWang', pass_gen(4,2,2), 'www.instagram.com',
#                      'This is my instagram account.', 
#                      '#instagram #social #socialMedia #messenger')

# paypal = UserData('RuddyWang', pass_gen(8,3,5), 'www.paypal.com',
#                   'This is my paypal account.',
#                   '#paypal #payment #money #paymentGateway')

# discord = UserData('goviwang', pass_gen(8,3,5), 'www.discord.com')
# portpass = UserData('admin', pass_gen(9,3,5), 'www.portpass.com', 'This is my portpass account.', '#portpass #passwordManager #safety #security')
# Insert a new user into the database. - END



# Getting all the data from the database. - START
# print(get_all_data())
# Getting all the data from the database. - END

# Getting a specific entry from the database. - START
# print(db(0).get_data())
# Getting a specific entry from the database. - END


# Removing all entries from the database. - START
# del_all_data()
# Removing all entries from the database. - END


# Removing a specific entry from the database. - START
# db(0).del_data()
# Removing a specific entry from the database. - END


# Updating  a specific username entry from the database. - START
# db(5).edit_username('')
# Updating  a specific username entry from the database. - END



# Updating a specific password entry from the database. - START
# db(4).edit_password('')
# Updating a specific password entry from the database. - END


# Updating a specific website entry from the database. - START
# db(2).edit_website('')
# Updating a specific website entry from the database. - END


# Updating a specific note entry from the database. - START
# db(7).edit_note('This is my new note.')
# Updating a specific note entry from the database. - END


# Updating a specific tag entry from the database. - START
# db(7).edit_tag('#newTag')
# Updating a specific tag entry from the database. - END


# Export the database to a csv file. - START
# export_data()
# Export the database to a csv file. - END


# Import the database from a csv file. - START
# import_data()
# Import the database from a csv file. - END