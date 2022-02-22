import re


def login():
    print("WELCOME TO LOGIN PAGE")

    file = open("user.txt", "r")
    maills = []
    passls = []
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        maills.append(a)
        passls.append(b)
    data = dict(zip(maills, passls))
    file.close()

    email = input("enter your mail: ")

    if email not in maills:
        print("userid not found \n")
        print("no mail id found please register ")
        print("type 'login' to go to login page")
        print("or type 'register' to go to register page\n\n")
        while True:
            lorr = input()
            if lorr == 'login':
                login()
            elif lorr == "register":
                register()
            else:
                print("choose between 'login' or 'register'")

    elif email in maills:
        password = input("enter your password: ")
        if password!=data[email]:
            print("wrong password")
            print("type 'forget' to know your password")
            print("or type 'signup' to go to signup page\n\n")

            while True:
                forget = input()
                if forget == 'forget':
                    print(f"your password for the {email} id is {data[email]}")
                if forget == "signup":
                    signup()
                else:
                    print("choose between 'forget' or 'signup'")
        else:
            print("welcome to website page")
            exit(0)



def mail(email,maills):
    mail_val = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    if re.search(mail_val, email):
        if email in maills:
            print("mail id already exist")
            register()
        else:
            password(email)
    else:
        print("please enter valid mailid")
        register()


def password(email):
    password = input("enter your password: ")
    password2 = input("enter your password again: ")
    if password == password2:
        if len(password) < 5:
            print("password is too short")
            register()
        elif len(password) >16:
            print("password is too long")
            register()
        elif not re.search("[a-z]", password):
            print("password must have atleast one lower-case")
            register()
        elif not re.search("[A-Z]", password):
            print("password must have atleast one upper")
            register()
        elif not re.search("[0-9]", password):
            print("password must have atleast one number")
            register()
        elif not re.search("[\._]", password):
            print("password must have atleast one special character")
            register()
        else:
            file = open("user.txt", "a")
            file.write(email + "," + password+"\n")
            file.close()
            print("account registered,please sign in\n\n")
            login()
    else:
        print("passwords are not matching")
        register()

def register():
    print("WELCOME TO REGISTER PAGE")

    file = open("user.txt", "r")
    maills = []
    passls = []
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        maills.append(a)
        passls.append(b)

    data = dict(zip(maills,passls))
    file.close()

    email = input("enter your mail: ")
    mail(email,maills)


def signup():
    print("welcome to login page \n")
    choose = input("login or signup: ")
    if choose == "login":
        login()
    elif choose == "signup":
        register()
    else:
        print("please enter a valid input\n\n")
        signup()

signup()

