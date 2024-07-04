from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
# databasw functions ::::->>>>>>>>>>>>>>>>>>>>>>>>>>>
def add_func():
    if rollno.get() == "" or name.get() =="":
        messagebox.showerror("Error ! ","Please fill the fields")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="S4soum@y", database="student_record")
        curr = conn.cursor()
        curr.execute("INSERT INTO studentdata VALUES(%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),
                                                        unit_test_1.get(),unit_test_2.get(),unit_test_3.get(),
                                                                      unit_test_4.get(),unit_test_5.get()))
        try:
            conn.commit()
            messagebox.showinfo("Success", "Data entered successfully")
            fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            conn.close()

def fetch_data():
    conn = mysql.connector.connect(host="localhost", user="root", password="S4soum@y", database="student_record")
    curr = conn.cursor()
    curr.execute("SELECT * FROM studentdata")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',END,values=row)
        conn.commit()
    conn.close()


root = Tk()
root.geometry("1370x700+0+0")
root.title("Student Information System")

#Tile of whole window
title = Label(root,text = "Student Information System",bg="orange red",fg="black",padx=25,pady=25,
                font=("Arial 40 bold"),border=12,relief= RAISED
                )
title.pack(side=TOP,fill='x')

#left side frame
detail_frame = LabelFrame(root,text="Enter Details",font=("Arial,25,bold"),bg="lightgrey",fg="red",border=12,relief=GROOVE)
detail_frame.place(x=40,y=150,width=600,height=600)
#right frame
data_frame = Frame(root,bg = "lightgrey",border=12,relief=GROOVE)
data_frame.place(x=660,y=150,width=800,height=600)

#----------------varianbles------------#
rollno = StringVar()
name = StringVar()
unit_test_1 = StringVar()
unit_test_2 = StringVar()
unit_test_3 = StringVar()
unit_test_4 = StringVar()
unit_test_5 = StringVar()

search_by = StringVar()

#->>>>>>>>>>>>>>>>>>>>>>


#left side ->>>>

#rollno
rollno_lbl = Label(detail_frame,text="Roll No : ",font=('Arial',20),bd=5,bg="lightgrey")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)
rollno_ent = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)
#name
name_lbl = Label(detail_frame,text="Name : ",font=('Arial',20),bd=16,bg="lightgrey")
name_lbl.grid(row=1,column=0,padx=2,pady=2)
name_ent = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)
#unit test1
unit_test_1 = Label(detail_frame,text="Unit Test 1 : ",font=('Arial',20),bd=12,bg="lightgrey")
unit_test_1.grid(row=2,column=0,padx=2,pady=2)
unit_test_1 = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=unit_test_1)
unit_test_1.grid(row=2,column=1,padx=2,pady=2)
#unit_test2
unit_test_2 = Label(detail_frame,text="Unit Test 2 : ",font=('Arial',20),bd=12,bg="lightgrey")
unit_test_2.grid(row=3,column=0,padx=2,pady=2)
unit_test_2 = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=unit_test_2)
unit_test_2.grid(row=3,column=1,padx=2,pady=2)
#unit_test3
unit_test_3lbl = Label(detail_frame,text="Unit Test 3 : ",font=('Arial',20),bd=12,bg="lightgrey")
unit_test_3lbl.grid(row=4,column=0,padx=2,pady=2)
unit_test3ent = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=unit_test_3)
unit_test3ent.grid(row=4,column=1,padx=2,pady=2)
#unit_test4
unit_test4lbl = Label(detail_frame,text="Unit Test 4 : ",font=('Arial',20),bd=12,bg="lightgrey")
unit_test4lbl.grid(row=5,column=0,padx=2,pady=2)
unit_test4ent = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=unit_test_4)
unit_test4ent.grid(row=5,column=1,padx=2,pady=2)
#unit_test5
unit_test5lbl = Label(detail_frame,text="Unit Test 5 : ",font=('Arial',20),bd=12,bg="lightgrey")
unit_test5lbl.grid(row=6,column=0,padx=2,pady=2)
unit_test5ent = Entry(detail_frame,font=('arial',17),relief=GROOVE,border=12,bd=5,textvariable=unit_test_5)
unit_test5ent.grid(row=6,column=1,padx=2,pady=2)
#Button
submit_button = Button(detail_frame,text="Submit",bg="lightgrey",bd=7,font=('Arial',13),width=352,height=100,command=add_func)
submit_button.place(x=100,y=450,width=202,height=50)
update_button = Button(detail_frame,text="Update",bg="lightgrey",bd=7,font=('Arial',13),width=352,height=100)
update_button.place(x=100,y=510,width=202,height=50)


#right side ->>>>>>
search_frame = Frame(data_frame,bg="lightgrey",bd=12,relief=GROOVE)
search_frame.pack(side=TOP,fill='x')
#search label
Search_label = Label(search_frame,text="Search By ",bg="lightgrey",font=('Arial',14))
Search_label.grid(row=0,column=0,padx=12,pady=2)
#search combobox
search_in = ttk.Combobox(search_frame,font=("Arial",14),state="readonly",textvariable=search_by)
search_in['values'] =("Name","Roll No")
search_in.grid(row=0,column=1,padx=12,pady=2)
#seacrh button
search_btn= Button(search_frame,text="Search",font=("Arial",13),bd=4,width=14,bg="lightgrey")
search_btn.grid(row=0,column=2,padx=12,pady=2)
#show all button
show_btn= Button(search_frame,text="Show All",font=("Arial",13),bd=4,width=14,bg="lightgrey")
show_btn.grid(row=0,column=3,padx=12,pady=2)

#database frame
main_frame = Frame(data_frame,bg="lightgrey",bd=11,relief=GROOVE)
main_frame.pack(fill=BOTH,expand=True)

#scroll bar in database frame
y_scroll = Scrollbar(main_frame,orient=VERTICAL)
x_scroll = Scrollbar(main_frame,orient=HORIZONTAL)

#creating table using Treeview
student_table = ttk.Treeview(main_frame,columns=("Roll No","Name","Unit-Test-1","Unit-Test-2"
                                                 ,"Unit-Test-3","Unit-Test-4","Unit-Test-5"),
                                                  yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
y_scroll.pack(side=RIGHT,fill="y")
x_scroll.config(command=student_table.xview)
x_scroll.pack(side=BOTTOM,fill="x")

student_table.heading("Roll No",text="Roll No")
student_table.heading("Name",text="Name")
student_table.heading("Unit-Test-1",text="Unit-Test-1")
student_table.heading("Unit-Test-2",text="Unit-Test-2")
student_table.heading("Unit-Test-3",text="Unit-Test-3")
student_table.heading("Unit-Test-4",text="Unit-Test-4")
student_table.heading("Unit-Test-5",text="Unit-Test-5")

student_table['show'] = 'headings'
student_table.column("Roll No",width=80)
student_table.column("Name",width=80)
student_table.column("Unit-Test-1",width=50)
student_table.column("Unit-Test-2",width=50)
student_table.column("Unit-Test-3",width=50)
student_table.column("Unit-Test-4",width=50)
student_table.column("Unit-Test-5",width=50)
student_table.pack(fill=BOTH,expand=True)





root.mainloop()