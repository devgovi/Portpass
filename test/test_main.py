# Govine-J
# GITS
# 2022-06-04
# Put together all the functions in the main.py file.
# Test the functions in the main.py file.
from test_userData import UserData
from test_dbManager import DBManager as db
from test_dbManager import del_all_data, get_all_data
from test_passGen import pass_generator as pass_gen




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
# discord = UserData('goviwang', pass_gen(8,3,5), None)
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
# db(0).edit_username('NewUsername')
# Updating  a specific username entry from the database. - END



# Updating a specific password entry from the database. - START
# db(1).edit_password('newPassword')
# Updating a specific password entry from the database. - END


# Updating a specific website entry from the database. - START
# db(2).edit_website('www.newWebsite.com')
# Updating a specific website entry from the database. - END


# Updating a specific note entry from the database. - START
# db(3).edit_note('This is my new note.')
# Updating a specific note entry from the database. - END

# Updating a specific tag entry from the database. - START
# db(6).edit_tag('#newTag')
# Updating a specific tag entry from the database. - END