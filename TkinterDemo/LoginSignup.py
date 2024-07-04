from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import subprocess
##DATABASE

def login():
    if usr.get() == "" or passw.get()=="":
        messagebox.showerror("Error!", "Please fill all the fields")
    else:
        username = usr.get()
        password = passw.get()
        if(password=="admin"):
            messagebox.showinfo("Succesfull Login","You have been login successfully")
            launch_welcome_script()
        else:
            messagebox.showerror("Error","Wrong password entered")

def launch_welcome_script():
    try:
        subprocess.Popen(['python', 'Sinew.py'])  # Adjust the command as per your environment
    except FileNotFoundError:
        messagebox.showerror("Error", "Failed to launch welcome.py")


def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)

win = Tk()
win.geometry("1450x700")
win.resizable(False, False)
win.title("WELLNESS-WAY NETWORK")

submit_btn_style = {"font": ("Arial", 15), "bd": 5, "bg": "#008080", "fg": "white"}

#Top image
top_photo = resize_image("../Projct/img_2.png", 1450, 150)
top = Label(image=top_photo)
top.pack(side=TOP, fill='x')

#Top title
mytitle = Label(win, text="WELLNESS WAY-NETWORK", font=("Arial", 25, "bold"), bg="#008080", fg="white")
mytitle.pack(side=TOP, fill='x', padx=0, pady=0)

#Hero image
hero_photo = resize_image("../Projct/img_3.png", 750, 400)  # Adjust width and height as needed
hero = Label(image=hero_photo)
hero.place(x=20, y=230, height=450, width=800)

#hero right frame
rightfr = Frame(win,border =12,bg="lightgrey",relief=SUNKEN)
rightfr.place(x=840,y=310,height=310,width=550)

#content in hero right fraeme
loginlabel = Label(rightfr,text="Login",border=12, bg="lightgrey",font=("Arial",16,"bold"))
loginlabel.place(x=175,y=30,height=30,width=150)

#usernamelabel
usernamelabel =  Label(rightfr,text="Username : ",border=12, bg="lightgrey",font=("Arial",16,"bold"))
usernamelabel.place(x=30,y=80,height=30,width=150)

#username entry
usr = StringVar()
userentry = Entry(rightfr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=usr)
userentry.place(x=200,y=80,height=30,width=180)

#passwordlabel
passlabel =Label(rightfr,text="Password : ",border=12, bg="lightgrey",font=("Arial",16,"bold"))
passlabel.place(x=30,y=140,height=30,width=150)

#password entry
passw =StringVar()
passentry = Entry(rightfr, font=("Arial", 15), bg="lightgrey", bd=3, textvariable=passw)
passentry.place(x=200,y=140,height=30,width=180)

#admin or not
admin = StringVar()
adminbox = Checkbutton(rightfr, text="Admin", font=("ARIAL", 16), bg="lightgrey",variable=admin)
adminbox.place(x=160,y=180,height=30,width=160)

#submitbutton
subbutt = Button(rightfr,text="Click to Login",**submit_btn_style,command=login)
subbutt.place(x=160,y=230,height=50,width=200)

win.mainloop()
