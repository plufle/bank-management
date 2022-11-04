# modules
from tkinter import *
from cryptography.fernet import Fernet
import mysql.connector as connector
import main_passwords
import random

# functions

def login():
    userid = int(userid_e.get())
    password = pass_e.get()

    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    if current_user_temp_tuple == None:
        print('account not found\nplease try again')
        login_screen()
    else:
        current_user_temp_list = list(current_user_temp_tuple)
        current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
        if current_user_temp_list[2] == password:
            print('successfully logined to the account')
        else:
            print('entered password is incorrect\n please try again')
            login()
        return current_user_temp_list

def createaccount():
    name = input("enter your name      : ")
    userid = random.randint(10002, 100000)
    pin = input("enter you password    :  ")
    pin2 = input("confirm your password : ")
    if pin != pin2:
        print("pin dose not match\nplease try again")
        createaccount()
    else:
        balance = 0
        pin_encoded = str(encodeStr(pin))
        print(type(pin_encoded))
        insertstr = "insert into users values('{0}','{1}','{2}','{3}')".format(userid, name, pin_encoded, balance)
        cursor.execute(insertstr)
        database.commit()
        print("account sucessfully created :-")
        print("name    = {}".format(name))
        print("userid  = {}".format(userid))
        print("pin     = {}".format(pin))
        print("balance = 0")

def login_admin():
    pass


def encodeStr(text):
    global fernet, key
    encryptedText = fernet.encrypt(text.encode()).decode()
    return encryptedText


def decodeStr(text):
    global fernet, key
    decryptedText = fernet.decrypt(text.encode()).decode()
    return decryptedText


def login_screen():
    global userid_e,pass_e
    login_window = Tk()
    login_window.geometry('1000x800')
    login_window.title('Login')

    welcome = Label(login_window, text="                     Welcome to Online Bank                     ",
                    font=('Arial Bold', 40))
    welcome.grid(column=0, row=0, columnspan=6)

    spaces = Label(login_window, text="           ", font=('sans-serif', 40))
    spaces.grid(column=0, row=1)

    welcome = Label(login_window, text="   Login   ", font=('sans-serif', 40))
    welcome.grid(column=1, row=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=1)

    userid_label = Label(login_window, text="   User ID   ", font=('sans-serif', 30))
    userid_label.grid(column=1, row=3)

    userid_e = Entry(login_window, borderwidth=10)
    userid_e.grid(column=2, row=3)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=4)

    pass_label = Label(login_window, text="Password   ", font=('sans-serif', 30))
    pass_label.grid(column=1, row=4)

    pass_e = Entry(login_window, borderwidth=10)
    pass_e.grid(column=2, row=4)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=5)
    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=1, row=5)

    login_button = Button(login_window, text='Login', font=('sans-serif', 24), bg='light blue', fg='white',
                          command=login)
    login_button.grid(row=5, column=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=6)

    frame_admin = LabelFrame(login_window, text='Administrator', font=('sans-serif', 20),)
    frame_admin.grid(column=1, row=6)

    login_button_admin = Button(frame_admin, text='Login', font=('sans-serif', 24), bg='#FF7F50', fg='white',
                                command=login_admin)
    login_button_admin.grid(row=0, column=0, )

    frame_new = LabelFrame(login_window, text='New Account', font=('sans-serif', 20), padx=5, pady=5)
    frame_new.grid(column=2, row=6, columnspan=2)

    create_btn = Button(frame_new, text='Create new account', font=('sans-serif', 24), bg='#00008B', fg='white', padx=7,
                        pady=3, command=createaccount)
    create_btn.grid(row=5, column=0)

    login_window.mainloop()



# main

try:
    database = connector.connect(host=main_passwords.hosts, database=main_passwords.name,
                                 user=main_passwords.users, password=main_passwords.database_password)

    print('successfully connected to database')
except:
    print('database not connected')

cursor = database.cursor()

key = main_passwords.frenet_key.encode()
fernet = Fernet(key)




login_screen()

