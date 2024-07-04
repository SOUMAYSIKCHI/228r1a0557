from tkinter import *
from tkinter import ttk
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tkinter import messagebox

engine = create_engine('sqlite:///pyppt.db')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    rollno = Column(String, unique=True)
    name = Column(String)
    ppt_title = Column(String)
    submitted = Column(Boolean)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

def search_student():
    session = Session()
    if search_by.get() == "Name":
        students = session.query(Student).filter_by(name=search_in.get()).all()
    elif search_by.get() == "Roll No":
        students = session.query(Student).filter_by(rollno=search_in.get()).all()
    elif search_by.get() == "PPT Title":
        students = session.query(Student).filter_by(ppt_title=search_in.get()).all()
    elif search_by.get() == "Submitted":
        students = session.query(Student).filter_by(submitted=search_in.get()=="Yes").all()
    session.close()
    student_table.delete(*student_table.get_children())
    for student in students:
        student_table.insert('', 'end', values=(student.rollno, student.name, student.ppt_title, "Yes" if student.submitted else "No"))

def submit_student():
    session = Session()
    student = Student(rollno=Roll_No.get(), name=name.get(), ppt_title=PPT_title.get(), submitted=Submitted.get()=="Yes")
    session.add(student)
    session.commit()
    session.close()
    student_table.insert('', 'end', values=(Roll_No.get(), name.get(), PPT_title.get(), Submitted.get()))


def update_student():
    session = Session()
    student = session.query(Student).filter_by(rollno=Roll_No.get()).first()
    if student:
        student.name = name.get()
        student.ppt_title = PPT_title.get()
        student.submitted = Submitted.get()=="Yes"
        session.commit()
        messagebox.showinfo("Success","Data updated succesfull")
    else:
        messagebox.showinfo("Error","Data not updated")

    session.close()

def show_all_students():
    session = Session()
    students = session.query(Student).all()
    session.close()
    student_table.delete(*student_table.get_children())
    for student in students:
        student_table.insert('', 'end', values=(student.rollno, student.name, student.ppt_title, "Yes" if student.submitted else "No"))

#-----------------------------------------TTKINTER CODE---------------------------------------------------------------------------------
root = Tk()
root.geometry("1370x700+0+0")
root.title("PPT Submission System")

# Title of whole window
title = Label(root, text="PPT Submission System", bg="skyblue", fg="black", padx=25, pady=25,
              font=("Arial 40 bold"), border=12, relief=RAISED)
title.pack(side=TOP, fill='x')

# Left side frame
detail_frame = LabelFrame(root, text="Enter Details", font=("Arial 25 bold"), bg="alice blue", fg="red", border=12,
                          relief=SUNKEN)
detail_frame.place(x=40, y=150, width=600, height=600)

# Right frame
data_frame = Frame(root, bg="lightgrey", border=12, relief=GROOVE)
data_frame.place(x=660, y=150, width=800, height=600)

# Variables
name = StringVar()
Roll_No = StringVar()
PPT_title = StringVar()
Submitted = StringVar()
search_by = StringVar()

# Left side ->>>
# Name
name_lbl = Label(detail_frame, text="Name : ", font=('Arial', 20), bd=5, bg="alice blue")
name_lbl.grid(row=0, column=0, padx=2, pady=2)
name_ent = Entry(detail_frame, font=('arial', 17), relief=GROOVE, border=12, bd=5, textvariable=name)
name_ent.grid(row=0, column=1, padx=2, pady=2)

# Roll No
rollno_lbl = Label(detail_frame, text="Roll No : ", font=('Arial', 20), bd=5, bg="alice blue")
rollno_lbl.grid(row=1, column=0, padx=2, pady=2)
rollno_ent = Entry(detail_frame, font=('arial', 17), relief=GROOVE, border=12, bd=5, textvariable=Roll_No)
rollno_ent.grid(row=1, column=1, padx=2, pady=2)

# PPT Title
ppt_title_lbl = Label(detail_frame, text="PPT Title : ", font=('Arial', 20), bd=5, bg="alice blue")
ppt_title_lbl.grid(row=2, column=0, padx=2, pady=2)
ppt_title_ent = Entry(detail_frame, font=('arial', 17), relief=GROOVE, border=12, bd=5, textvariable=PPT_title)
ppt_title_ent.grid(row=2, column=1, padx=2, pady=2)

# Submitted
submitted_lbl = Label(detail_frame, text="Submitted : ", font=('Arial', 20), bd=5, bg="alice blue")
submitted_lbl.grid(row=3, column=0, padx=2, pady=2)
yes_radio = Radiobutton(detail_frame, text="Yes", variable=Submitted, value="Yes",bg="alice blue")
yes_radio.grid(row=3, column=1, padx=2, pady=2)
no_radio = Radiobutton(detail_frame, text="No", variable=Submitted, value="No",bg="alice blue")
no_radio.grid(row=3, column=2, padx=2, pady=2)

# Button
submit_button = Button(detail_frame, text="Submit", bg="dark turquoise", bd=7, font=('Arial', 13), width=352, height=100, command=submit_student)
submit_button.place(x=20, y=450, width=202, height=50)

# Button

update_button = Button(detail_frame, text="Update", bg="dark turquoise", bd=7, font=('Arial', 13), width=352, height=100, command=update_student)
update_button.place(x=280, y=450, width=202, height=50)

# Right side ->>>
search_frame = Frame(data_frame, bg="medium spring green", bd=12, relief=GROOVE)
search_frame.pack(side=TOP, fill='x')

# Search label
Search_label = Label(search_frame, text="Search By ", bg="medium spring green", font=('Arial', 14))
Search_label.grid(row=0, column=0, padx=12, pady=2)

# Search combobox
search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly", textvariable=search_by)
search_in['values'] = ("Name", "Roll No", "PPT Title", "Submitted")
search_in.grid(row=0, column=1, padx=7, pady=2)

# Search button
search_btn = Button(search_frame, text="Search", font=("Arial", 13), bd=4, width=14, bg="whitesmoke", command=search_student)
search_btn.grid(row=0, column=3, padx=12, pady=2)
# Show all button
show_all = Button(search_frame, text="Show All", font=("Arial", 13), bd=4, width=14, bg="whitesmoke", command=show_all_students)
show_all.grid(row=0, column=2, padx=14, pady=2)

#database frame
main_frame = Frame(data_frame,bg="lightgrey",bd=11,relief=GROOVE)
main_frame.pack(fill=BOTH,expand=True)

#scroll bar in database frame
y_scroll = Scrollbar(main_frame,orient=VERTICAL)
x_scroll = Scrollbar(main_frame,orient=HORIZONTAL)

#creating table using Treeview
student_table = ttk.Treeview(main_frame,columns=("Roll_No","Name","PPT_title","Submitted"),
                                                  yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
y_scroll.pack(side=RIGHT,fill="y")
x_scroll.config(command=student_table.xview)
x_scroll.pack(side=BOTTOM,fill="x")

student_table.heading("Roll_No",text="Roll_No")
student_table.heading("Name",text="Name")
student_table.heading("PPT_title",text="PPT_title")
student_table.heading("Submitted",text="Submitted")


student_table['show'] = 'headings'
student_table.column("Roll_No",width=80)
student_table.column("Name",width=80)
student_table.column("PPT_title",width=50)
student_table.column("Submitted",width=50)
student_table.pack(fill=BOTH,expand=True)

root.mainloop()