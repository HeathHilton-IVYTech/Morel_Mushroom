import databaseConnection


cursor = databaseConnection.db.cursor()


def createAdminUser(firstname, lastname, username, email, city_assigned, state_assigned):
    sql = "INSERT INTO admin_user (firstname, lastname, username, email, city_assigned, state_assigned) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (firstname, lastname, username, email, city_assigned, state_assigned)
    cursor.execute(sql, val)
    databaseConnection.db.commit()


def createGenericUser(firstname, lastname, email, username):
    sql = "INSERT INTO generic_user (firstname, lastname, email, username) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, username)
    cursor.execute(sql, val)
    databaseConnection.db.commit()


def createIssue(street, city, state, zip):
    sql = "INSERT INTO issue (street, city, state, zip) VALUES (%s, %s, %s, %s)"
    val = (street, city, state, zip)
    cursor.execute(sql, val)
    databaseConnection.db.commit()


