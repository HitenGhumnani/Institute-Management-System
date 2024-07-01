import tkinter as tk
from tkinter import messagebox


#Create the main window
parent=tk.Tk()
parent.title("Admission Form")

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

#Create and place the address label and entry
address_label=tk.Label(parent, text="Enter your Address:")
address_label.pack()

address_entry = tk.Entry(parent)
address_entry.pack()

#Create and place the city label and entry
city_label=tk.Label(parent, text="Enter your City:")
city_label.pack()

city_entry = tk.Entry(parent)
city_entry.pack()

#Create and place the mobileno label and entry
mobileno_label=tk.Label(parent, text="Enter your Mobile Number:")
mobileno_label.pack()

mobileno_entry = tk.Entry(parent)
mobileno_entry.pack()

#Create and place the email_id label and entry
email_id_label=tk.Label(parent, text="Enter your Email Id:")
email_id_label.pack()

email_id_entry = tk.Entry(parent)
email_id_entry.pack()

#Create and place the batch_time label and entry
batch_time_label=tk.Label(parent, text="Enter preferred Batch Time:")
batch_time_label.pack()

batch_time_entry = tk.Entry(parent)
batch_time_entry.pack()

#Create and place the staff label and entry
staff_label=tk.Label(parent, text="Provide name of the Staff:")
staff_label.pack()

staff_entry = tk.Entry(parent)
staff_entry.pack()

#Create and place the fees label and entry
fess_label=tk.Label(parent, text="Enter your Total Fess:")
fess_label.pack()

fees_entry = tk.Entry(parent)
fees_entry.pack()

#Create and place the duration label and entry
duration_label=tk.Label(parent, text="Total Duration of your Course:")
duration_label.pack()

duration_entry = tk.Entry(parent)
duration_entry.pack()

#Create and place the submit button
submit_button=tk.Button(parent, text="Submit")
submit_button.pack()

#Start the Tkinter event loop
parent.mainloop()
