# Instructions for Database access

# 1. If you are going to work with the database on your local machine please install
# requirements.txt by running pip install > "requirements.txt" from the command line

# 2. Please email tbanis86@gmail.com your public IP address so it can be whitelisted on the db server.
# You can figure out your public IP by going to https://www.ipchicken.com/

# 3. Items 1 and 2 also apply to where ever the application is being hosted on the web

# 4. Please use the following functions to write to the db. Please note that if you change the name of the variable 
# i.e (firstname to firstName) please be sure to also change it in the databaseFunctions.py file
#
# createAdminUser(firstname, lastname, username, email, city_assigned, state_assigned)
# createGenericUser(firstname, lastname, email, username)
# createIssue(street, city, state, zip)

# 5. If you want to access the functions from the databaseFunctions file, be sure to import it to the file you are working on.

# 6. If you want to interact with the db directly with a gui or to see the tables structure, download a DB Admin tool 
# (such as Navicat for Mysql) and enter the information found in the databaseConnection.py file. Again I'll need your 
# public IP so you can connect.
