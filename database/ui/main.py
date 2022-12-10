from tkinter import*
import databaseFunctions

fullName = ""

street = ""
city = ""
state = ""
zip = ""

root = Tk()
root.geometry('500x500')
root.title("Road Tech")
titleLabel = Label(root, text="Road Issue Form",width=20,font=("bold", 20))
titleLabel.place(x=90,y=53)
submitterLabel = Label(root, text="Email",width=20,font=("bold", 10))
submitterLabel.place(x=80,y=130)
submitterEmail = Entry(root)
submitterEmail.place(x=240,y=130)
addressLabel = Label(root, text="Address",width=20,font=("bold", 10))
addressLabel.place(x=68,y=180)
submitterAddress = Entry(root)
submitterAddress.place(x=240,y=180)
directionLabel = Label(root, text="Direction:",width=20,font=("bold", 10))
directionLabel.place(x=70,y=230)

var = IntVar()

#Radiobutton(root, text="N",padx = 5, variable=var, value=1).place(x=235,y=230)
#Radiobutton(root, text="S",padx = 5, variable=var, value=2).place(x=280,y=230)
#Radiobutton(root, text="E",padx = 5, variable=var, value=3).place(x=325,y=230)
#Radiobutton(root, text="W",padx = 5, variable=var, value=4).place(x=370,y=230)

def getValues(street, city, state, zip):
    street = submitterAddress.get()
    print(street)
    #street = "1234 Mint Ave"
    city = "Indy"
    state = "IN"
    zip = "12345"
    return(street, city, state, zip)

def Submit():
    street = submitterAddress.get()
    city = "Indy"
    state = "IN"
    zip = "56789"
    #getValues(street, city, state, zip)
    databaseFunctions.createIssue(street, city, state, zip)
    print("added to database")
    print(street, city, state, zip)

emailLabel = Label(root, text="Email:",width=20,font=("bold", 10))
emailLabel.place(x=70,y=280)
submitterEmail = Entry(root)
submitterEmail.place(x=240,y=280)
Button(root, text='Submit',width=20,bg='brown',fg='white',command=Submit).place(x=180,y=380)

# it is use for display the registration form on the window

root.mainloop()

print("Your Issue has been submitted ...")
print(submitterName)
print(submitterEmail)
print(directionLabel)
print(submitterEmail)