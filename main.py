from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Login Page")
root.config(bg="blue")


def check_table():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Login')
    for i in mycursor:
        print(i)


def enter():
    check_table()


def register():
    user = ent1.get()
    password = ent2.get()
    if ent1 == "" or ent2 == "":
        messagebox.showerror("ERROR", "Please fill in username and password")
    elif user.isdigit():
        messagebox.showerror("Error", "Name does not contain letters")
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO Login  VALUES (%s, %s)"
        val = (ent1.get(), ent2.get())
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        mycursor.execute('Select * from Login')
        messagebox.showinfo("SUCCESS", "New user and password added")

        # text file
        w = open("Login_details.txt", "a+")
        w.write("Username: " + ent1.get() + "\n")
        w.write("Password: " + ent2.get() + "\n")
        w.write("\n")
        w.close()


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)


def exit_btn():
    msg_box = messagebox.askquestion("Heading Out?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        root.destroy()


# LABELS
lbl1 = Label(root, text="Please enter Username:", bg="blue", font=('Arial', 10))
lbl1.place(x=10, y=10)
lbl2 = Label(root, text="Please enter Password:", bg="blue", font=('Arial', 10))
lbl2.place(x=10, y=50)


# Entries
ent1 = Entry(root, width=30)
ent1.place(x=250, y=10)
ent2 = Entry(root, width=30, show="*")
ent2.place(x=250, y=50)

# Buttons
btn = Button(root, text="Login", width=10, bg="blue", command=enter, borderwidth=5)
btn.place(x=200, y=200)
btn2 = Button(root, text="Register", width=10, bg="blue", command=register, borderwidth=5)
btn2.place(x=350, y=200)
clrbtn = Button(root, text="Clear", width=10, bg="blue", command=clear, borderwidth=5)
clrbtn.place(x=100, y=350)
extbtn = Button(root, text="Exit", width=10, bg="blue", command=exit_btn, borderwidth=5)
extbtn.place(x=500, y=350)


# Run mainloop
root.mainloop()
