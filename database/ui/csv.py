import mysql.connector
from tkinter import * 
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
import tkinter as tk
import tkinter.filedialog as filedialog


db = mysql.connector.connect(
    host = "34.72.16.255",
    user="root",
    password="iamlegend",
    db = "pothole1"
)

cursor= db.cursor()
cursor.execute("SELECT * FROM issue")

for row in cursor:

    f = open('issue.csv', 'w')
    s = str(row)
    f.write(s)
    f.close()

def save_file():
  # Use the filedialog module to ask the user to select a file to save
  filepath = filedialog.asksaveasfilename()

  # Open the file for writing
  with open(filepath, 'w') as outfile:
    # Write the contents of the file
    outfile.write(s)
    
# Create a root window
root = tk.Tk()

# Create a button to trigger the save function
button = tk.Button(root, text='Save', command=save_file)
button.pack()

# Run the Tkinter event loop
root.mainloop()