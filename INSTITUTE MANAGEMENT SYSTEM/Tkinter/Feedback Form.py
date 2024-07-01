import tkinter as tk
from tkinter import messagebox


#Create the main window
parent=tk.Tk()
parent.title("Feedback Form")

#Create and place the date label and entry
date_label=tk.Label(parent, text="Enter Date:")
date_label.pack()

date_entry = tk.Entry(parent)
date_entry.pack()

#Create and place the fullname label and entry
fullname_label=tk.Label(parent, text="Enter your Fullname:")
fullname_label.pack()

fullname_entry = tk.Entry(parent)
fullname_entry.pack()

#Create and place the mobileno label and entry
mobileno_label=tk.Label(parent, text="Enter your Mobile Number:")
mobileno_label.pack()

mobileno_entry = tk.Entry(parent)
mobileno_entry.pack()

#Create and place the enquiry label and entry
enquiry_label=tk.Label(parent, text="Enter your Enquires:")
enquiry_label.pack()

enquiry_entry = tk.Entry(parent)
enquiry_entry.pack()

#Create and place the feedback label and entry
feedback_label=tk.Label(parent, text="Enter your Feedback:")
feedback_label.pack()

feedback_entry = tk.Entry(parent)
feedback_entry.pack()

#Create and place the staff label and entry
staff_label=tk.Label(parent, text="Provide name of the Staff:")
staff_label.pack()

staff_entry = tk.Entry(parent)
staff_entry.pack()

#Create and place the submit button
submit_button=tk.Button(parent, text="Submit")
submit_button.pack()

#Start the Tkinter event loop
parent.mainloop()
