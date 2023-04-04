from tkinter import *
import tkinter as tk
from tkinter import messagebox
import databaseFunctions
import mailer
import pandas as pd

#Overall declaration of global variables that the program uses
fullName = ""
street = ""
city = ""
state = ""
emailAddress = ""
issueDescription = ""
blank = ""
testFunction = False

#Create the initial project submittal screen with titles, labels, entry fields, and buttons
root = Tk()
root.geometry('500x500')
root.title("Road Issue")

titleLabel = Label(root, text="Road Issue Form", width=20, font=("bold", 20))
titleLabel.place(x=90, y=53)

submitterLabel = Label(root, text="Full Name:*", width=20, anchor="e", justify=LEFT, font=("bold", 10))
submitterLabel.place(x=28, y=130)
submitterName = Entry(root)
submitterName.place(x=200, y=130, width=200)

streetLabel = Label(root, text="Street Address:*", width=20, anchor="e", justify=LEFT, font=("bold", 10))
streetLabel.place(x=28, y=180)
streetAddress = Entry(root)
streetAddress.place(x=200, y=180, width=200)

stateLabel = Label(root, text="City:*", width=20, anchor="e", justify=LEFT, font=("bold", 10))
stateLabel.place(x=28, y=230)
cityAddress = Entry(root)
cityAddress.place(x=200, y=230, width=150)

stateLabel = Label(root, text="State:*", width=10, font=("bold", 10))
stateLabel.place(x=300, y=230)
stateAddress = Entry(root)
stateAddress.place(x=370, y=230, width=29)

emailLabel = Label(root, text="Email:*", width=20, anchor="e", justify=LEFT, font=("bold", 10))
emailLabel.place(x=28, y=280)
submitterEmail = Entry(root)
submitterEmail.place(x=200, y=280, width=200)

issueLabel = Label(root, text="Description of Road Issue:*", width=20, anchor="e", justify=LEFT, font=("bold", 10))
issueLabel.place(x=28, y=320)
submittedIssue = Entry(root)
submittedIssue.place(x=200, y=320, width=200)


Button(root, text='Submit', command=lambda: (openNewWindow()), width=20, bg='brown', fg='white').place(x=180, y=375)
Button(root, text='Admin Portal', command=lambda: (openAdminWindow()), width=20, bg='red', fg='white').place(x=180, y=425)

#The above Submit button directs the program here. 
def submit():
    #Pulling the data in the entry boxes
    fullName = submitterName.get()
    street = streetAddress.get()
    city = cityAddress.get()
    state = stateAddress.get()
    emailAddress = submitterEmail.get()
    issueDescription = submittedIssue.get()
    #Verify that all of the fields have data, program shuts you down unless its filled
    if(fullName == "" or street == "" or city == "" or state == "" or emailAddress == "" or issueDescription == ""):
        #messagebox.showerror('Error', 'All fields are required')
        testFunction = False
    #If you are good, YOU SHALL PASS!
    else:
        #Attempt to send it to the database, shut it all down if it fails
        if(databaseFunctions.createIssue(fullName, street, city, state, emailAddress, issueDescription)):
            print("Database Success.")
            #Attempt to send it to the supplied email
            if(confirmationEmail(fullName, street, city, state, emailAddress, issueDescription)):
                print("Email Success.")
                testFunction = True
            else:
                print("Email Fail.")
                testFunction = False
        else:
            print("Database Fail.")
            testFunction = False

    #If there was a failure anywhere, an error is thrown and then it is returned to the function that originally called this function "openNewWindow()"
    return(testFunction)

#Take in the field data and then 
def confirmationEmail(fullName, street, city, state, emailAddress, issueDescription):
    mail_subject = "Road Tech Repair Submission"
    mail_message = "Thank you, " + fullName + ", the issue at " + street + " in " + city + ", " + state + " has been submitted." + issueDescription

    my_mailer = mailer.Mailer("py_mailer@clond.net","ZAhJDErU3QK8","smtp.gmail.com")
    return my_mailer.send_mail(emailAddress, mail_subject, mail_message)


def openNewWindow():
    #If everything went well, enjoy a box of "toast message" 
    if(submit()):
        text="Your Issue has been submitted ... \n\n" + str(submitterName.get()) + "\n" + str(submitterEmail.get()) +"\n" + str(streetAddress.get()) + "\n" + str(submittedIssue.get())
        messagebox.showinfo("Success", text)
    #If there was a failure along the way, it sorts out what it was(ish) and lets you know the error
    else:        
        fullName = submitterName.get()
        street = streetAddress.get()
        city = cityAddress.get()
        state = stateAddress.get()
        emailAddress = submitterEmail.get()
        issueDescription = submittedIssue.get()
        #Better have submitted something is all of the those fields
        if(fullName == "" or street == "" or city == "" or state == "" or emailAddress == "" or issueDescription == ""):
            messagebox.showerror('Error', 'All fields are required')
        #It wasn't the missing fields that caused it so it's generic message for you.
        else:
            messagebox.showerror('Error', 'Something went wrong')

    
    
#The admin window to review the item submitted
def openAdminWindow():

    window = tk.Tk()
    window.title("Issues Submitted")
    
    #ScrollView window was chosen to accomidate how many issues are to be submitted since Indiana roads are salty garbage
    scrollViewBox = tk.Text(window, height=50, width=175)
    scroll = tk.Scrollbar(window)
    scrollViewBox.configure(yscrollcommand=scroll.set)
    scrollViewBox.pack(side=tk.LEFT)
    scroll.config(command=scrollViewBox.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    #Pull all of the issues from the database
    submittedIssueList = databaseFunctions.getAllIssues()
    d = submittedIssueList
    #Using Panda's Dataframe to manage the data and then spell out the metadata for the column names
    df=pd.DataFrame(d, columns=['#', 'Name:', 'Street:', 'City:', 'State:', 'Email:', 'Issue:', 'Repaired:', 'Mystery:'])
    #Dropping one of the unused fields, added mostly for example purposes
    df=df.drop(df.columns[[8]], axis=1)

    scrollViewBox.insert(tk.END, df)
        
root.mainloop()



#git pull

#git add .
#git commit -m "some sort of message"
#git push