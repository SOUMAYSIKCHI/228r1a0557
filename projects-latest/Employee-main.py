import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import Employeedatabase

app = customtkinter.CTk()
app.title("Employee Management System")
app.geometry('900x420')
app.config(bg='#161c25')
app.resizable(False ,False)
font1 = ('Arial',20,'bold')
font2 = ('Arial,12,bold')


def add_to_treeview():
    employees = Employeedatabase.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)
    print("Treeview refreshed with employees:", employees)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        id_entry.delete(0,END)
        name_entry.delete(0,END)
        role_entry.delete(0,END)
        variable1.set('Male')
        status_entry.delete(0,END)

def disply_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        role_entry.insert(0,row[2])
        variable1.set(row[3])
        status_entry.insert(0,row[4])
    else:
        pass
def insert():
    id = id_entry.get()
    name = name_entry.get()
    role = role_entry.get()
    gender = variable1.get()
    status = status_entry.get()
    if not(id and name and role and gender and status):
        messagebox.showerror('Error','Enter all fields')
    elif Employeedatabase.id_exists(id):
        messagebox.showerror('Error','ID already exists.')
    else:
        Employeedatabase.insert_employee(id,name,role,gender,status)
        add_to_treeview()
        messagebox.showinfo('Success','Data has been inserted')

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose an employee to delete')
    else:
        id= id_entry.get()
        Employeedatabase.delete_employee(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been deleted')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an employee to delete')
    else:
        id = id_entry.get()
        name = name_entry.get()
        role = role_entry.get()
        gender = variable1.get()
        status = status_entry.get()
        Employeedatabase.update_employee(name,role,gender,status,id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been updated')

id_label = customtkinter.CTkLabel(app,font=font1,text='ID:',text_color='#fff',bg_color='#161c25')
id_label.place(x=20,y=20)

id_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color="#fff",border_width=2,width=100,border_color='#0c9295')
id_entry.place(x=120,y=20)

name_label = customtkinter.CTkLabel(app,font=font1,text='NAME:',text_color='#fff',bg_color='#161c25')
name_label.place(x=20,y=80)

name_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color="#fff",border_width=2,width=100,border_color='#0c9295')
name_entry.place(x=120,y=80)

role_label = customtkinter.CTkLabel(app,font=font1,text='ROLE:',text_color='#fff',bg_color='#161c25')
role_label.place(x=20,y=140)

role_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color="#fff",border_width=2,width=100,border_color='#0c9295')
role_entry.place(x=120,y=140)

gender_label = customtkinter.CTkLabel(app,font=font1,text='GENDER:',text_color='#fff',bg_color='#161c25')
gender_label.place(x=20,y=200)

options = ['Male','Female']
variable1= StringVar()

gender_options = customtkinter.CTkComboBox(app,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#0C9295',button_color='#0C9295',border_color='#0C9295',width=180,variable=variable1,values=options)
gender_options.set('Male')
gender_options.place(x=120,y=200)

status_label = customtkinter.CTkLabel(app,font=font1,text='STATUS:',text_color='#fff',bg_color='#161c25')
status_label.place(x=20,y=260)
status_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color="#fff",border_width=2,width=100,border_color='#0c9295')
status_entry.place(x=120,y=260)

add_button = customtkinter.CTkButton(app,command=insert,font=font1,text_color='#fff',text='Add Employee',fg_color='#05A312',hover_color='#00850B',bg_color='#161C25',cursor ='hand2',corner_radius=15,width=260)
add_button.place(x=20,y=310)

clear_button = customtkinter.CTkButton(app,command=lambda:clear(True),font=font1,text_color='#fff',text='New Employee',fg_color='#161C25',hover_color='#FF5002',bg_color='#161C25',cursor ='hand2',corner_radius=15,width=260)
clear_button.place(x=20,y=360)

update_button = customtkinter.CTkButton(app,command=update,font=font1,text_color='#fff',text='Update Employee',fg_color='#161C25',hover_color='#FF5002',bg_color='#161C25',cursor ='hand2',corner_radius=15,width=260)
update_button.place(x=300,y=360)

delete_button = customtkinter.CTkButton(app,command=delete,font=font1,text_color='#fff',text='Delete Employee',fg_color='#E40404',hover_color='#AE0000',bg_color='#161C25',cursor ='hand2',corner_radius=15,width=260)
delete_button.place(x=580,y=360)

style = ttk.Style(app)
style.configure('Treeview',font=font2,foreground='#000',background='#fff',fieldbackground='#313837')
style.map('Treeview',background=[('selected','#1A8F2D')])
tree = ttk.Treeview(app,height=15)

tree['columns'] = ('ID','Name','Role','Gender','Status')
tree.column('#0',width=0,stretch=tk.NO)
tree.column('ID',anchor=tk.CENTER,width=120)
tree.column('Name',anchor=tk.CENTER,width=120)
tree.column('Role',anchor=tk.CENTER,width=120)
tree.column('Gender',anchor=tk.CENTER,width=120)
tree.column('Status',anchor=tk.CENTER,width=120)

tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Status',text='Status')
tree.place(x=400,y=20)

tree.bind('<ButtonRelease>',disply_data)

add_to_treeview()

app.mainloop()
