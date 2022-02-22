from tkinter import *
import re

def welcome():

    welcome=Tk()
    welcome.geometry("500x450")
    welcome.title("Welcome")

    label1 = Label(welcome, text="welcome to the home page you are log in successfully",font='Helvetica 14 bold',fg="orange").pack()
    button2 = Button(welcome, text="sign up", command=signup).pack()



def forgetpass():
    if email2.get() not in maills:
        label22 = Label(Login,text="userid not found \n",fg="red")
        label22.pack()
    elif email2.get() in maills:
        label1 = Label(Login, text=f"your password for the {email2.get()} id is {data[email2.get()]}")
        label1.pack()
        button1 = Button(Login, text="sign up", command=signup)
        button1.pack()
def malvar2():
    if email2.get() not in maills:
        label22 = Label(Login,text="userid not found \n",fg="red")
        label22.pack()


    elif email2.get() in maills:
        if str(password3.get())!=data[email2.get()]:
            label3 = Label(Login,text="wrong passsword  \n",fg="red").pack()
        else:
            welcome()



def login():

    global Login
    Login=Tk()
    Login.geometry("500x450")
    Login.title("login")

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
    global password3

    label1=Label(Login,text="login",font=12,bg="red").pack(padx=6,pady=4)
    label2 = Label(Login, text="Email",font=8).pack()
    email2 = Entry(Login)
    email2.pack()
    label3 = Label(Login, text="password",font=8).pack()
    password3 = Entry(Login)
    password3.pack()
    button1 = Button(Login, text="login", command=malvar2,width=12,height=1,bg="grey")
    button1.pack(padx=3,pady=12)
    button2 = Button(Login, text="forget password", command=forgetpass,width=12,height=1,bg="grey")
    button2.pack(padx=3,pady=4)



def mailver():
    mail_val = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(mail_val, email.get()):
        if email.get() in maills:
            label1 = Label(Register, text="mail already exists",fg="red").pack()
        else:
            if password.get() == password2.get():
                if len(password.get()) <= 5:
                    label1 = Label(Register, text="password is too short",fg="red").pack()
                elif len(password.get()) > 15:
                    label1 = Label(Register, text="password is too long",fg="red").pack()
                elif not re.search("[@_!#$%^&*()<>?/\|=}+{~:]", password.get()):
                    label2 = Label(Register, text="password must have atleast one special character",fg="red").pack()
                elif not re.search("[a-z]", password.get()):
                    label1 = Label(Register, text="password must have atleast one lower-case",fg="red").pack()
                elif not re.search("[A-Z]", password.get()):
                    label1 = Label(Register, text="password must have atleast one upper",fg="red").pack()
                elif not re.search("[0-9]", password.get()):
                    label1 = Label(Register, text="password must have atleast one number",fg="red").pack()
                else:
                    file = open("user.txt", "a")
                    file.write(str(email.get())+","+str(password.get())+"\n")
                    file.close()
                    # print("account registered,please sign in\n\n")
                    login()
            else:
                label1 = Label(Register, text="passwords are not matching",fg="red")
                label1.pack()
    else:
        label1 = Label(Register, text="please enter valid Email-id",fg="red")
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
    global Register
    Register = Tk()
    Register.geometry("500x450")
    Register.title("Register")

    global email
    global password
    global password2
    label1 = Label(Register, text="Register",font=12,bg="red").pack(padx=3,pady=4)
    label2 = Label(Register, text="Email",font=8).pack()
    email=Entry(Register)
    email.pack()
    label3 = Label(Register, text="password",font=8).pack()
    password = Entry(Register)
    password.pack()
    label4 = Label(Register, text="confirm password",font=8).pack()
    password2 = Entry(Register)
    password2.pack()
    button1 = Button(Register, text="register", command=mailver,width=12,height=1,bg="grey")
    button1.pack(padx=3,pady=8)


def signup():
    signup = Tk()
    signup.geometry("500x450")
    signup.title("Sign up")
    label1=Label(signup,text="welcome to Sign up",font=12,bg="red").pack(padx=3,pady=4)
    button1=Button(signup,text="login",command=login,width=12,height=1).pack(padx=3,pady=4)
    button2=Button(signup,text="register",command=register,width=12,height=1).pack(padx=3,pady=4)
    button3=Button(signup,text="exit",command=quit,width=12,height=1).pack(padx=3,pady=4)
    signup.mainloop()

signup()
