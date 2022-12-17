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
   


def createIssue(fullName, street, city, state, emailAddress, issueDescription):
    sql = "INSERT INTO issue (fullName, street, city, state, emailAddress, issueDescription) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (fullName, street, city, state, emailAddress, issueDescription)
    cursor.execute(sql, val)
    databaseConnection.db.commit()
    return("True")
  

def getGenericUserInfo(userId):
    sql = "SELECT * FROM generic_user WHERE id = %s"
    val = userId
    cursor.execute(sql, val)
    print(cursor.fetchall())

def getAdminUserInfo(userId):
    sql = "SELECT * FROM admin_user WHERE id = %s"
    val = userId
    cursor.execute(sql, val)
    print(cursor.fetchall())

def getIssueByUser():
    sql = "SELECT generic_user.firstname, generic_user.lastname, issue.street\
           FROM generic_user INNER JOIN issue ON issue.id = generic_user.issue_id"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    
    for row in myresult:
        print("First Name: ", row[0])
        print("Last Name: ", row[1])
        print("Street: ", row[2])
    

    return myresult

def getAllIssues():
    sql = "SELECT * FROM issue"
    cursor.execute(sql)
    issues = cursor.fetchall()

    for row in issues:
        print("ID: ", row[0])
        print("Submitters Name: ", row[1])
        print("Street: ", row[2])
        print("City: ", row[3])
        print("State: ", row[4])
        print("Email Address: ", row[5])
        print("Description: ", row[6])
        print("Completed: ", row[7])
    return issues



