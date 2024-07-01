import customtkinter as ctk
import tkinter.messagebox as tkmb
import mysql.connector

#Selecting GUI theme - dark, light, system(for system default)
ctk.set_appearance_mode("dark")

#Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("400*400")
app.title("Examination Form")

def logic():
    try:
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="institute")
        dt = date_entry.get()
        fn = fullname_entry.get()
        ad = address_entry.get()
        ct = city_entry.get()
        mn = mobileno_entry.get()
        eid = email_id_entry.get()
        ex = exam_entry.get()
        ses = session_entry.get()
        exf = exam_fees_entry.get()

        sql = "insert into exf values('" + dt + "','" + fn + "','" + ad + "','" + ct + "','" + mn + "','" + eid + "','" + ex + "','" + ses + "','" + exf + "')"
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

address_entry=ctk.CTkEntry(master=frame,placeholder_text="Address:")
address_entry.pack(pady=12,padx=10)

city_entry=ctk.CTkEntry(master=frame,placeholder_text="City:")
city_entry.pack(pady=12,padx=10)

mobileno_entry=ctk.CTkEntry(master=frame,placeholder_text="Mobile Number:")
mobileno_entry.pack(pady=12,padx=10)

email_id_entry=ctk.CTkEntry(master=frame,placeholder_text="Email Id:")
email_id_entry.pack(pady=12,padx=10)

exam_entry=ctk.CTkEntry(master=frame,placeholder_text="Name of Examination:")
exam_entry.pack(pady=12,padx=10)

session_entry=ctk.CTkEntry(master=frame,placeholder_text="Session[WINTER/SUMMER]:")
session_entry.pack(pady=12,padx=10)

exam_fees_entry=ctk.CTkEntry(master=frame,placeholder_text="Examination Fees:")
exam_fees_entry.pack(pady=12,padx=10)

button=ctk.CTkButton(master=frame,text='Submit',command=logic)
button.pack(pady=12,padx=10)

app.mainloop()
