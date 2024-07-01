import tkinter as tk
from customtkinter import CTkEntry
import mysql.connector



data = []
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="institute"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM srf")
myresult = mycursor.fetchall()


for x in myresult:
  data.append(x)



root = tk.Tk()
root.title("Institute Management System")

label = tk.Label(root, text="STAFF REGISTRATION", font=("Arial", 14, "bold"))
label.grid(row=0, column=0, padx=10, pady=5)

headers = ["Date", "Fullname", "Address", "City", "Mobile Number", "Email ID", "Qualifications", "Designation", "Duty Time"]
for col, header in enumerate(headers):
    label = tk.Label(root, text=header, font=("Arial", 12, "bold"))
    label.grid(row=1, column=col, padx=10, pady=5)





 
widths = [100,100,200,100,100,200,200,100,100]
for row, row_data in enumerate(data, start=2):
    for col, value in enumerate(row_data):
        entry = CTkEntry(root, width=widths[col])
        entry.insert(tk.END, value)
        entry.grid(row=row,column=col,padx=10,pady=5)

root.mainloop()
