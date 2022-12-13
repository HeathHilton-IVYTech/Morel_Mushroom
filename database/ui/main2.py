from tkinter import *
import tkinter as tk
import databaseFunctions
import mailer

fullName = ""
street = ""
city = ""
state = ""
emailAddress = ""
issueDescription = ""
blank = ""

root = Tk()
root.geometry('500x500')
root.title("Road Issue")

titleLabel = Label(root, text="Road Issue Form", width=20, font=("bold", 20))
titleLabel.place(x=90, y=53)

submitterLabel = Label(root, text="Full Name:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
submitterLabel.place(x=28, y=130)
submitterName = Entry(root)
submitterName.place(x=200, y=130, width=200)

streetLabel = Label(root, text="Street Address:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
streetLabel.place(x=28, y=180)
streetAddress = Entry(root)
streetAddress.place(x=200, y=180, width=200)

stateLabel = Label(root, text="City:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
stateLabel.place(x=28, y=230)
cityAddress = Entry(root)
cityAddress.place(x=200, y=230, width=150)

stateLabel = Label(root, text="State:", width=10, font=("bold", 10))
stateLabel.place(x=300, y=230)
stateAddress = Entry(root)
stateAddress.place(x=370, y=230, width=29)

emailLabel = Label(root, text="Email:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
emailLabel.place(x=28, y=280)
submitterEmail = Entry(root)
submitterEmail.place(x=200, y=280, width=200)

issueLabel = Label(root, text="Description of Road Issue:", width=20, anchor="e", justify=LEFT, font=("bold", 10))
issueLabel.place(x=28, y=320)
submittedIssue = Entry(root)
submittedIssue.place(x=200, y=320, width=200)


Button(root, text='Submit', command=lambda: (openNewWindow()), width=20, bg='brown', fg='white').place(x=180, y=375)
Button(root, text='Admin Portal', command=lambda: (openAdminWindow()), width=20, bg='red', fg='white').place(x=180, y=425)


def submit():
    fullName = submitterName.get()
    street = streetAddress.get()
    city = cityAddress.get()
    state = stateAddress.get()
    emailAddress = submitterEmail.get()
    issueDescription = submittedIssue.get()
    databaseFunctions.createIssue(fullName, street, city, state, emailAddress, issueDescription)
    print("added to database")
    if(confirmationEmail(fullName, street, city, state, emailAddress, issueDescription)):
        print("Message successfully delivered to " + emailAddress + ".")
    else:
        print("Sorry, the confirmation email could not be delivered.")
    #print(fullName, street, city, state, emailAddress, issueDescription)


def confirmationEmail(fullName, street, city, state, emailAddress, issueDescription):
    mail_subject = "Road Tech Repair Submission"
    mail_message = "Thank you, " + fullName + ", the issue at " + street + " in " + city + ", " + state + " has been submitted." + issueDescription
    #mail_message = "Test Submission"
    #my_mailer = mailer.Mailer("py_mailer@email.com","secretpassword","smtp.email.com",587,True,True,False)
    #my_mailer.send_mail(emailAddress, mail_subject, mail_message)

    my_mailer = mailer.Mailer("py_mailer@clond.net","ZAhJDErU3QK8","smtp.gmail.com")
    return my_mailer.send_mail(emailAddress, mail_subject, mail_message)

    #mailer.Mailer.send_mail(blank, emailAddress, mail_subject, mail_message)


def openNewWindow():
    submit()
    newWindow = Toplevel(root)
    newWindow.title("Issue Submitted")

    # define window geometry

    newWindow.geometry("250x250")

    Label(newWindow,
          text="Your Issue has been submitted ... \n" + str(submitterName.get()) + "\n" + str(submitterEmail.get()) +"\n" + str(streetAddress.get()) + "\n" + str(submittedIssue.get())).place(x=25, y=25)
    Button(newWindow, text="Exit", command=newWindow.destroy).place(x=100, y=100)
    

def openAdminWindow():

    window = tk.Tk()
    window.title("Issues Submitted")
    
    text = tk.Text(window, height=50, width=150)
    scroll = tk.Scrollbar(window)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=tk.LEFT)
    
    scroll.config(command=text.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    submittedIssueList = databaseFunctions.getAllIssues()


    chunked_list = list()
    chunk_size = 1
    for i in range(0, len(submittedIssueList), chunk_size):
        chunked_list.append(submittedIssueList[i:i+chunk_size])


    i = 0
    paragraphString = "Submitted Data: \n#  Name:    Address:      City:  ST:    Email:    Issue:   Repaired:  Mystery:"
    for i in range(0, len(chunked_list)):
        paragraphString = paragraphString + "\n" + str(chunked_list[i])
    paragraphString = paragraphString.translate({ord(i):None for i in '[]()\''})
    
    text.insert(tk.END, paragraphString)


root.mainloop()
