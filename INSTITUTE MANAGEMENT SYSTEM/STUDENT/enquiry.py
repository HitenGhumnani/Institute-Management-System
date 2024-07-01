import customtkinter as ctk
import tkinter.messagebox as tkmb
import mysql.connector

#Selecting GUI theme - dark, light, system(for system default)
ctk.set_appearance_mode("dark")

#Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("400*400")
app.title("Enquiry Form")

def logic():
    try:
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="institute")
        dt = date_entry.get()
        fn = fullname_entry.get()
        mn = mobileno_entry.get()
        eq = enquiry_entry.get()
        stf = staff_entry.get()

        sql = "insert into ef values('" + dt + "','" + fn + "','" + mn + "','" + eq + "','" + stf + "')"
        mycursor = mydb.cursor()
        mycursor.execute(sql)

        mydb.commit()
        tkmb.showinfo(title="Submit Successful",message="Record Saved")

    except Exception as e:
        tkmb.showinfo(title="Error",message=e)

label=ctk.CTkLabel(app,text="Institute")
label.pack(pady=20)

frame=ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label=ctk.CTkLabel(master=frame,text='Please the fill the given form')
label.pack(pady=12,padx=10)

date_entry=ctk.CTkEntry(master=frame,placeholder_text="Date:")
date_entry.pack(pady=12,padx=10)

fullname_entry=ctk.CTkEntry(master=frame,placeholder_text="Fullname:")
fullname_entry.pack(pady=12,padx=10)

mobileno_entry=ctk.CTkEntry(master=frame,placeholder_text="Mobile Number:")
mobileno_entry.pack(pady=12,padx=10)

enquiry_entry=ctk.CTkEntry(master=frame,placeholder_text="Enquires:")
enquiry_entry.pack(pady=12,padx=10)

staff_entry=ctk.CTkEntry(master=frame,placeholder_text="Staff Name:")
staff_entry.pack(pady=12,padx=10)

button=ctk.CTkButton(master=frame,text='Submit',command=logic)
button.pack(pady=12,padx=10)

app.mainloop()
