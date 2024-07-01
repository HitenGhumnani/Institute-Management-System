import customtkinter as ctk
import tkinter.messagebox as tkmb
import mysql.connector

#Selecting GUI theme - dark, light, system(for system default)
ctk.set_appearance_mode("dark")

#Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("400*400")
app.title("Exam Fees Form")

def logic():
    try:
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="institute")
        dt = date_entry.get()
        fn = fullname_entry.get()
        ex = exam_entry.get()
        exf = exam_fees_entry.get()
        pt = particular_entry.get()
        md = mop_entry.get()
        
        sql = "insert into exff values('" + dt + "','" + fn + "','" + ex + "','" + exf + "','" + pt + "','" + md + "')"
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

exam_entry=ctk.CTkEntry(master=frame,placeholder_text="Name of Examination:")
exam_entry.pack(pady=12,padx=10)

exam_fees_entry=ctk.CTkEntry(master=frame,placeholder_text="Examination Fees:")
exam_fees_entry.pack(pady=12,padx=10)

particular_entry=ctk.CTkEntry(master=frame,placeholder_text="Particulars [if any]:")
particular_entry.pack(pady=12,padx=10)

mop_entry=ctk.CTkEntry(master=frame,placeholder_text="Mode of Payment:")
mop_entry.pack(pady=12,padx=10)

button=ctk.CTkButton(master=frame,text='Submit',command=logic)
button.pack(pady=12,padx=10)

app.mainloop()
