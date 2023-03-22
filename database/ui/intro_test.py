from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pandas as pd

#Overall declaration of global variables that the program uses
address = ""
city = ""
state = ""
notes = ""
date = ""
testFunction = False
lines = ""

#Create the initial project submittal screen with titles, labels, entry fields, and buttons
rootLogOn = Tk()
rootLogOn.geometry('500x300')
rootLogOn.title("Morel Mushrooms")

titleLabel = Label(rootLogOn, text="Morel Mushrooms Logon", width=20, font=("bold", 20))
titleLabel.place(x=90, y=53)

submitterLabel = Label(rootLogOn, text="User Name:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
submitterLabel.place(x=28, y=130)
submitterName = Entry(rootLogOn)
submitterName.place(x=200, y=130, width=200)

streetLabel = Label(rootLogOn, text="Password:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
streetLabel.place(x=28, y=180)
streetAddress = Entry(rootLogOn)
streetAddress.place(x=200, y=180, width=200)

Button(rootLogOn, text='Submit', command=lambda: (openSubmissionWindow()), width=20, bg='brown', fg='white').place(x=180, y=230)

##########################################################



def openSubmissionWindow():

    #with open('readme.txt') as f:
    #lines = f.readlines()
    
    rootSubmission = Tk()
    rootSubmission.geometry('500x500')
    rootSubmission.title("Morel Mushrooms")

    titleLabel = Label(rootSubmission, text="Morel Mushrooms Logon", width=20, font=("bold", 20))
    titleLabel.place(x=90, y=53)

    addressLabel = Label(rootSubmission, text="Address:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
    addressLabel.place(x=28, y=130)
    addressField = Entry(rootSubmission)
    addressField.place(x=200, y=130, width=200)

    cityLabel = Label(rootSubmission, text="City:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
    cityLabel.place(x=28, y=180)
    cityField = Entry(rootSubmission)
    cityField.place(x=200, y=180, width=200)

    stateLabel = Label(rootSubmission, text="State:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
    stateLabel.place(x=28, y=230)
    stateField = Entry(rootSubmission)
    stateField.place(x=200, y=230, width=200)

    noteLabel = Label(rootSubmission, text="Notes:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
    noteLabel.place(x=28, y=280)
    noteField = Entry(rootSubmission)
    noteField.place(x=200, y=280, width=200)

    dateLabel = Label(rootSubmission, text="Date:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
    dateLabel.place(x=28, y=330)
    dateField = Entry(rootSubmission)
    dateField.place(x=200, y=330, width=200)
    
    Button(rootSubmission, text='Submit', command=lambda: (submit()), width=20, bg='brown', fg='white').place(x=180, y=380)

#The above Submit button directs the program here. 
def submit():
    #Pulling the data in the entry boxes
    address = addressField.get()
    city = cityField.get()
    state = stateField.get()
    note = noteField.get()
    date = dateField.get()

    if(address == "" or city == "" or state == "" or note == "" or date == ""):
        messagebox.showerror('Error', 'All fields are required')
    else:
        openSubmittedConfirmWindow()

    #Verify that all of the fields have data, program shuts you down unless its filled
    #if(fullName == "" or street == "" or city == "" or state == "" or emailAddress == "" or issueDescription == ""):
        #messagebox.showerror('Error', 'All fields are required')
    #    testFunction = False
    #If you are good, YOU SHALL PASS!
    #else:
        #Attempt to send it to the database, shut it all down if it fails
        #if(databaseFunctions.createIssue(fullName, street, city, state, emailAddress, issueDescription)):
        #    print("Database Success.")
        #    #Attempt to send it to the supplied email
        #    if(confirmationEmail(fullName, street, city, state, emailAddress, issueDescription)):
        #        print("Email Success.")
        #        testFunction = True
        #    else:
        #        print("Email Fail.")
        #        testFunction = False
        #else:
        #    print("Database Fail.")
        #    testFunction = False

    #If there was a failure anywhere, an error is thrown and then it is returned to the function that originally called this function "openNewWindow()"
    #return(testFunction)

#Take in the field data and then 
def openSubmittedConfirmWindow():
    mail_subject = "Road Tech Repair Submission"
    mail_message = "Thank you, " + fullName + ", the issue at " + street + " in " + city + ", " + state + " has been submitted." + issueDescription

    #my_mailer = mailer.Mailer("py_mailer@clond.net","ZAhJDErU3QK8","smtp.gmail.com")
    #return my_mailer.send_mail(emailAddress, mail_subject, mail_message)


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
    #submittedIssueList = databaseFunctions.getAllIssues()
    #d = submittedIssueList
    #Using Panda's Dataframe to manage the data and then spell out the metadata for the column names
    #df=pd.DataFrame(d, columns=['#', 'Name:', 'Street:', 'City:', 'State:', 'Email:', 'Issue:', 'Repaired:', 'Mystery:'])
    #Dropping one of the unused fields, added mostly for example purposes
    #df=df.drop(df.columns[[8]], axis=1)

    scrollViewBox.insert(tk.END, df)
        
rootLogOn.mainloop()



#git pull

#git add .
#git commit -m "some sort of message"
#git push