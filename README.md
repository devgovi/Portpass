
# Portpass

Portpass is a portable password manager, which uses a local SQLite<br>database that can be exported to a CSV file.

You are also able to import data with the accepted format<br>into the application.

The data format headers should be as follow:
- entryId, 
- username, 
- password, 
- website, 
- notes, 
- tags, 
- dateCreated, 
- dateModified.

## NOTE:

This should be in the format of a CSV file when importing data.


# FEATURES

1. Username, password and website entry must be<br>populated before data can be inserted into the<br>portpass.db

2. Require to setup a master password when using the app<br>for the first time.

3. Export portpass.db to userData.csv
4. Import userData.csv into portpass.db
5. For each entry a unique Id is created.
6. Edit or update entry by unique entry Id.
7. Remove and entry by unique entry Id.
8. Remove all entry from userData table at portpass.db
9. Log error if unable to connect to portpass.db
10. Can store a note and tag for each entry.
11. Can display all entry from the portpass.db
12. Can display entry by Id.
13. Generates secure password(s) or pin(s)