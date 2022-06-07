# Portpass
 Portpass is a portable password manager, which uses a local SQLite database that can be exported to a CSV file.
 
  You are also able to import data with the accepted format into the application.

  The data format headers should be as follow:
  entryId, username, password, website, notes, tags, dateCreated, dateModified.

  NOTE: 
    This should be in the format of a CSV file when importing data.

# FEATURES

    [] Username, password and website entry must be 
    populated before data can be inserted into the
    portpass.db

    [] Require to setup a master password when using the app
    for the first time.

    [] Export portpass.db to userData.csv
    [] Import userData.csv into portpass.db
    [] For each entry a unique Id is created.
    [] Edit or update entry by unique entry Id.
    [] Remove and entry by unique entry Id.
    [] Remove all entry from userData table at portpass.db
    [] Log error if unable to connect to portpass.db
    [] Can store a note and tag for each entry.
    [] Can display all entry from the portpass.db
    [] can display entry by Id.