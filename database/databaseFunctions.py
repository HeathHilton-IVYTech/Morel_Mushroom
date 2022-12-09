import databaseConnection


cursor = databaseConnection.db.cursor()
userId = (1,)

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
  

def getGenericUserInfo(userId):
    sql = "SELECT * FROM generic_user WHERE id = %s"
    val = userId
    cursor.execute(sql, val)
    print(cursor.fetchall())

def getIssueByUser():
    sql = "SELECT generic_user.firstname, generic_user.lastname, issue.street\
           FROM generic_user INNER JOIN issue ON issue.id = generic_user.issue_id"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    
    return myresult
      

getGenericUserInfo(userId)

getIssueByUser()

issue = getIssueByUser()

print(issue)



