import tkinter as tk
import databaseFunctions
import string

window = tk.Tk()
window.title("Text Widget with Scrollbar")
  
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

print(chunked_list[1])

#submittedList = submittedIssueList.split('), (')
i = 0
paragraphStyle = ""
for i in range(0, len(chunked_list)):
    paragraphStyle = paragraphStyle + "\n" + str(chunked_list[i])

paragraphStyle = paragraphStyle.translate({ord(i):None for i in '[]()'})
  
text.insert(tk.END, paragraphStyle)
tk.mainloop()