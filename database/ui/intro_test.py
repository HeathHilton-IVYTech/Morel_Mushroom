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
root = Tk()
root.geometry('500x600')
root.title("Morel Mushrooms")


titleLabel = Label(root, text="Morel Mushrooms Submitter", width=35, font=("bold", 20))
titleLabel.place(x=-30, y=53)

userLabel = Label(root, text="User Name:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
userLabel.place(x=28, y=130)
userName = Entry(root)
userName.place(x=200, y=130, width=200)

passLabel = Label(root, text="Password:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
passLabel.place(x=28, y=180)
passWord = Entry(root)
passWord.place(x=200, y=180, width=200)

lineLabel = Label(root, text="------------------------------------------------------------------------", width=30, anchor="e", fg='gray', justify=LEFT, font=("bold", 10))
lineLabel.place(x=150, y=210)

addressLabel = Label(root, text="Address:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
addressLabel.place(x=28, y=250)
addressField = Entry(root)
addressField.place(x=200, y=250, width=200)

cityLabel = Label(root, text="City:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
cityLabel.place(x=28, y=300)
cityField = Entry(root)
cityField.place(x=200, y=300, width=200)

stateLabel = Label(root, text="State:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
stateLabel.place(x=28, y=350)
stateField = Entry(root)
stateField.place(x=200, y=350, width=200)

noteLabel = Label(root, text="Notes:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
noteLabel.place(x=28, y=400)
noteField = Entry(root)
noteField.place(x=200, y=400, width=200)

dateLabel = Label(root, text="Date:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
dateLabel.place(x=28, y=450)
dateField = Entry(root)
dateField.place(x=200, y=450, width=200)


Button(root, text='Submit', command=lambda: (submit()), width=20, bg='brown', fg='white').place(x=180, y=525)

##########################################################



def openSubmissionWindow():
    root.destroy()
    #with open('readme.txt') as f:
    #lines = f.readlines()
    
    #rootSubmission = Tk()
    #rootSubmission.geometry('500x500')
    #rootSubmission.title("Morel Mushrooms")

    #titleLabel = Label(rootSubmission, text="Morel Mushrooms Logon", width=20, font=("bold", 20))
    #titleLabel.place(x=90, y=53)

    
    #Button(rootSubmission, text='Submit', command=lambda: (submit()), width=20, bg='brown', fg='white').place(x=180, y=380)



#The above Submit button directs the program here. 
def submit():
    #Pulling the data in the entry boxes
    #global rootSubmission
    #rootSubmission = Tk()
    #addressField = Entry(rootSubmission)

    address = addressField.get()
    city = cityField.get()
    state = stateField.get()
    note = noteField.get()
    date = dateField.get()

    if(address == "" or city == "" or state == "" or note == "" or date == ""):
        messagebox.showerror('Error', 'All fields are required')
    else:
        print(address + "\n" + city + "\n" + state + "\n" + note + "\n" + date)
        f = open('submissions.csv', 'r')
        content = f.read()
        print(content)
        f.close()
        
        openAdminWindow()
        #openSubmittedConfirmWindow()

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
    #mail_subject = "Road Tech Repair Submission"
    #mail_message = "Thank you, " + fullName + ", the issue at " + street + " in " + city + ", " + state + " has been submitted." + issueDescription
    print("Shut Up, YOU!")

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

    f = open('submissions.csv', 'r')
    content = f.read()
    print(content)
    f.close()
    submittedIssueList = content #databaseFunctions.getAllIssues()
    d = submittedIssueList
    #Using Panda's Dataframe to manage the data and then spell out the metadata for the column names
    #df=pd.DataFrame(df, columns=['#', 'Name:', 'Address:', 'City:', 'State:', 'Notes:', 'Date:'])
    df = pd.read_csv('submissions.csv', sep=",")#index_col=0)
    #df = pd.DataFrame(data=data).T
    #Dropping one of the unused fields, added mostly for example purposes
    #df=df.drop(df.columns[[8]], axis=1)

    scrollViewBox.insert(tk.END, df)
    scrollViewBox(df)
        
root.mainloop()



#git pull

#git add .
#git commit -m "some sort of message"
#git push