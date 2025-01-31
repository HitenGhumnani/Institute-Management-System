from tkinter import *
from subprocess import call
import sys

def enquiry():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/enquiry.py"])

def feedback():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/feedback.py"])

def admission():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/admission.py"])

def fees():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/fees.py"])

def attendance():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/attendance.py"])

def examination():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/examination.py"])

def examfees():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/examfees.py"])

def registration():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/registration.py"])

def attendace2():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/attendace[staff].py"])

def salary():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/salary.py"])

def batch_allocation():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/batch_allocation.py"])

def payments():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/TRANSACTIONS/payments.py"])

def other_income():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/TRANSACTIONS/other_income.py"])

def misce_expenses():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/TRANSACTIONS/misce_expenses.py"])

def enquiry_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/enquiry_table.py"])

def feedback_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/feedback_table.py"])

def admission_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/admission_table.py"])

def fees_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/fees_table.py"])

def attendance_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/attendance_table.py"])

def examination_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/examination_table.py"])

def examfees_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STUDENT/examfees_table.py"])

def registration_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/registration_table.py"])

def attendace2_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/attendace[staff]_table.py"])

def salary_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/salary_table.py"])

def batch_allocation_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/batch_allocation_table.py"])

def payments_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/TRANSACTIONS/payments_table.py"])

def other_income_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/TRANSACTIONS/other_income_table.py"])

def misce_expenses_table():
    call(["python", b"INSTITUTE MANAGEMENT SYSTEM/STAFF/misce_expenses_table.py"])

def close():
    sys.exit()
    
root = Tk()
root.attributes('-fullscreen',True)

menubar = Menu(root)

student = Menu(menubar,tearoff=0)
student.add_command(label="Enquiry",command=enquiry)
student.add_command(label="Feedback",command=feedback)
student.add_command(label="Admission",command=admission)
student.add_command(label="Fees",command=fees)
student.add_command(label="Attendance",command=attendance)
student.add_command(label="Examination",command=examination)
student.add_command(label="Exam Fees",command=examfees)

student.add_separator()
student.add_command(label="Exit",command=close)
menubar.add_cascade(label="STUDENT",menu=student)


staff = Menu(menubar,tearoff=0)
staff.add_command(label="Registration",command=registration)
staff.add_command(label="Staff Attendance",command=attendace2)
staff.add_command(label="Salary",command=salary)
staff.add_command(label="Batch Allocation",command=batch_allocation)

staff.add_separator()
staff.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="STAFF",menu=staff)


transaction = Menu(menubar,tearoff=0)
transaction.add_command(label="Payments",command=payments)
transaction.add_command(label="Other Income",command=other_income)
transaction.add_command(label="Miscellaneous Expenses",command=misce_expenses)

transaction.add_separator()
transaction.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="TRANSACTIONS",menu=transaction)


admin = Menu(menubar,tearoff=0)
admin.add_command(label="Enquiry Table",command=enquiry_table)
admin.add_command(label="Feedback Table",command=feedback_table)
admin.add_command(label="Admission Table",command=admission_table)
admin.add_command(label="Fees Table",command=fees_table)
admin.add_command(label="Attendance Table",command=attendance_table)
admin.add_command(label="Examination Table",command=examination_table)
admin.add_command(label="Exam Fees Table",command=examfees_table)
admin.add_command(label="Registration Table",command=registration_table)
admin.add_command(label="Staff Attendance Table",command=attendace2_table)
admin.add_command(label="Salary Table",command=salary_table)
admin.add_command(label="Batch Allocation Table",command=batch_allocation_table)
admin.add_command(label="Payments Table",command=payments_table)
admin.add_command(label="Other Income Table",command=other_income_table)
admin.add_command(label="Miscellaneous Expenses Table",command=misce_expenses_table)

admin.add_separator()
admin.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="ADMIN",menu=admin)

root.config(menu=menubar)
root.mainloop()
