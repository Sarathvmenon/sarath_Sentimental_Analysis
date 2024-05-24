import mysql.connector
from tkinter import *
from tkinter import messagebox
from Admin import AdminHome
#creating the application main window.
top = Tk()
top.geometry("600x400")
u_name = StringVar()
u_pass = StringVar()
large_font = ('Verdana', 15)
top.title("Login")
def checkuser():
    get_name = u_name.get().strip()
    get_pass = u_pass.get().strip()
    print("Name:", get_name, ",", "Password:", get_pass)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="speech"
    )
    if get_name=="" and get_pass=="":
        messagebox.showinfo("Entry","username and pass missing")
    elif get_name=="":
        messagebox.showinfo("Entry","username is blank")
    elif get_pass=="":
        messagebox.showinfo("Entry","password is blank")
    else:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM login WHERE userid = %s and password=%s"
        adr = (get_name,get_pass)

        mycursor.execute(sql, adr)

        print("I am here...")
        myresult = mycursor.fetchall()
        print("Count:",mycursor.rowcount)
        if mycursor.rowcount:
            top.withdraw()
            cp=Toplevel()
            print("I am here...")
            w=AdminHome(cp)
            #adminhome()
        else:
            messagebox.showinfo("Entry","no such user")
        print("done....")
def login():

    uname = Label(top, text = "Username",font=large_font).place(x = 30,y = 50)
    e1 = Entry(top,width = 20,textvariable=u_name,font=large_font).place(x = 140, y = 50)


    password = Label(top, text = "Password",font=large_font).place(x = 30, y = 90)
    e2 = Entry(top, width = 20,textvariable=u_pass,font=large_font,show="*").place(x = 140, y = 90)
    sbmitbtn = Button(top, text="Cancel", activebackground="pink", font=large_font, activeforeground="blue", command=top.destroy).place(x=300, y=130)

    sbmitbtn = Button(top, text = "Submit",activebackground = "pink",font=large_font, activeforeground = "blue",command=checkuser).place(x = 200, y = 130)

    top.mainloop()

login()