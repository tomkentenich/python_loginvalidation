from tkinter import *
import re

def welcome():
    welcome=Tk()
    welcome.geometry("500x450")
    label1 = Label(welcome, text="welcome to the home page you are log in successfully").pack()
    button2 = Button(welcome, text="sign up", command=signup).pack()



def forgetpass():
    if email2.get() not in maills:
        label22 = Label(Login,text="userid not found \n")
        label22.pack()
    elif email2.get() in maills:
        label1 = Label(Login, text=f"your password for the {email2.get()} id is {data[email2.get()]}")
        label1.pack()
        button1 = Button(Login, text="sign up", command=signup)
        button1.pack()
def malvar2():
    if email2.get() not in maills:
        label22 = Label(Login,text="userid not found \n")
        label22.pack()


    elif email2.get() in maills:
        if str(password.get())!=data[email2.get()]:
            label3 = Label(Login,text="wrong passsword \n").pack()
        else:
            welcome()



def login():
    global Login
    Login=Tk()
    Login.geometry("500x450")

    file = open("user.txt", "r")
    global maills
    maills = []
    passls = []
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        maills.append(a)
        passls.append(b)
    global data
    data = dict(zip(maills, passls))
    file.close()


    global email2
    global password

    label1=Label(Login,text="login").pack()
    label2 = Label(Login, text="username").pack()
    email2 = Entry(Login)
    email2.pack()
    label3 = Label(Login, text="password").pack()
    password = Entry(Login)
    password.pack()
    button1 = Button(Login, text="login", command=malvar2)
    button1.pack()
    button2 = Button(Login, text="forget password", command=forgetpass)
    button2.pack()



def mailver():
    mail_val = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(mail_val, email.get()):
        if email in maills:
            label1 = Label(register, text="mail already exists").pack()
        else:
            if password.get() == password2.get():
                if len(password.get()) <= 5:
                    label1 = Label(register, text="password is too short").pack()
                elif len(password.get()) > 15:
                    label1 = Label(register, text="password is too long").pack()
                elif not re.search("[a-z]", password.get()):
                    label1 = Label(register, text="password must have atleast one lower-case").pack()
                elif not re.search("[A-Z]", password.get()):
                    label1 = Label(register, text="password must have atleast one upper").pack()
                elif not re.search("[0-9]", password.get()):
                    label1 = Label(register, text="password must have atleast one number").pack()
                elif not re.search("[$&+,:;=?@#|'<>.-^*()%!]", password.get()):
                    label1 = Label(register, text="password must have atleast one special character").pack()
                else:
                    file = open("user.txt", "a")
                    file.write(str(email.get())+","+str(password.get())+"\n")
                    file.close()
                    # print("account registered,please sign in\n\n")
                    login()
            else:
                label1 = Label(register, text="passwords are not matching")
                label1.pack()
    else:
        label1 = Label(register, text="please enter valid mailid")
        label1.pack()

def register():
    file = open("user.txt", "r")
    global maills
    maills = []
    passls = []
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        maills.append(a)
        passls.append(b)
    data = dict(zip(maills, passls))
    file.close()
    global register
    register = Tk()
    register.geometry("500x450")
    global email
    global password
    global password2
    label1 = Label(register, text="register").pack()
    label2 = Label(register, text="username").pack()
    email=Entry(register)
    email.pack()
    label3 = Label(register, text="password").pack()
    password = Entry(register)
    password.pack()
    label4 = Label(register, text="confirm password").pack()
    password2 = Entry(register)
    password2.pack()
    button1 = Button(register, text="register", command=mailver)
    button1.pack()


def signup():
    signup = Tk()
    signup.geometry("500x450")
    label1=Label(signup,text="welcome to home page",font=10,).pack()
    button1=Button(signup,text="login",command=login,width=8,height=1).pack()
    button2=Button(signup,text="register",command=register,width=8,height=1).pack()
    button3=Button(signup,text="exit",command=quit,width=8,height=1).pack()
    signup.mainloop()

signup()

