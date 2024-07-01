import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from subprocess import call
 
  
# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 
  
app = ctk.CTk() 
app.geometry("400x400") 
app.title("INSTITUTE MANAGEMENT SYSTEM") 

def mainform():
    call(["python", "INSTITUTE MANAGEMENT SYSTEM/final.py"])
    
  
def login(): 
  
    username = "admin"
    password = "12345"
    
    if user_entry.get() == username and user_pass.get() == password: 
        mainform()
    else: 
        tkmb.showerror(title="Login Failed",message="Invalid Username and password") 
  
  
  
label = ctk.CTkLabel(app,text="LOGIN") 
  
label.pack(pady=20) 
  
  
frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 
  
label = ctk.CTkLabel(master=frame,text='INSTITUTE MANAGEMENT SYSTEM') 
label.pack(pady=12,padx=10) 
  
  
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 
  
  
button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 
  
  
app.mainloop()
