from tkinter import *
from cryptography.fernet import Fernet
import mysql.connector as connector
import main_passwords
from tkinter import messagebox
import random
import datetime
import pytz
from datetime import date, timedelta


def login():
    global login_window
    login_window = Tk()
    login_window.geometry('1000x800')
    login_window.title('Login')

    welcome = Label(login_window, text="                     Welcome to Online Bank                     ",
                    font=('sans-serif', 40))
    welcome.grid(column=0, row=0, columnspan=6)

    spaces = Label(login_window, text="           ", font=('sans-serif', 40))
    spaces.grid(column=0, row=1)

    welcome = Label(login_window, text="   Login   ", font=('sans-serif', 40))
    welcome.grid(column=1, row=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=1)

    userid_label = Label(login_window, text="   User ID   ", font=('sans-serif', 30))
    userid_label.grid(column=1, row=3)

    userid_e = Entry(login_window, borderwidth=5, font=('sans-serif', 20))
    userid_e.grid(column=2, row=3)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=4)

    pass_label = Label(login_window, text="Password   ", font=('sans-serif', 30))
    pass_label.grid(column=1, row=4)

    pass_e_login = Entry(login_window, borderwidth=5, font=('sans-serif', 20), show='*')
    pass_e_login.grid(column=2, row=4)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=5)
    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=1, row=5)

    login_button = Button(login_window, text='Login', font=('sans-serif', 24), bg='light blue', fg='white',
                          command=login_message)
    login_button.grid(row=5, column=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40))
    spaces.grid(column=0, row=6)

    frame_admin = LabelFrame(login_window, text='Administrator', font=('sans-serif', 20))
    frame_admin.grid(column=1, row=6)

    login_button_admin = Button(frame_admin, text='Login', font=('sans-serif', 24), bg='#FF7F50', fg='white',
                                command=pass_)
    login_button_admin.grid(row=0, column=0, )

    frame_new = LabelFrame(login_window, text='New Account', font=('sans-serif', 20), padx=5, pady=5)
    frame_new.grid(column=2, row=6, columnspan=2)

    create_btn = Button(frame_new, text='Create new account', font=('sans-serif', 24), bg='#00008B', fg='white', padx=7,
                        pady=3, command=pass_)
    create_btn.grid(row=5, column=0)

    login_window.mainloop()
    userid = int(userid_e.get())
    password = pass_e_login.get()
    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    current_user_temp_list = list(current_user_temp_tuple)
    current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
    if current_user_temp_list[2] == password:
        print('successfully logined to the account')

    else:
        print('entered password is incorrect\n please try again')
        login()
    return current_user_temp_list

def login_message():
    a = messagebox.showinfo(title='Login', message='successfully logged in')
    if a == 'ok':
        login_window.destroy()
        logined_window()


def logined_window():
    logined_window = Tk()
    logined_window.geometry('1000x800')
    logined_window.title('Welcome to BANK')

    spaces = Label(logined_window, text="   ", font=('sans-serif', 40))
    spaces.grid(column=0, row=0)

    welcome = Label(logined_window, text="What do you want to do?", font=('sans-serif', 50))
    welcome.grid(column=1, row=0, columnspan=4)

    trans_button = Button(logined_window, text='Transaction', font=('sans-serif', 42), bg='light blue', fg='white',
                          command=pass_)  #
    trans_button.grid(row=2, column=1, columnspan=3)
    deposit_button = Button(logined_window, text='Deposit', font=('sans-serif', 42), bg='light blue', fg='white',
                            command=pass_)  #
    deposit_button.grid(row=3, column=1, columnspan=3)
    withdrawal_button = Button(logined_window, text='Withdrawal', font=('sans-serif', 42), bg='light blue', fg='white',
                               command=pass_)  #
    withdrawal_button.grid(row=4, column=1, columnspan=3)
    show_trans_button = Button(logined_window, text='Show transaction', font=('sans-serif', 42), bg='light blue',
                               fg='white', command=pass_)  #
    show_trans_button.grid(row=5, column=1, columnspan=3)
    loan_button = Button(logined_window, text='Loan', font=('sans-serif', 42), bg='light blue', fg='white',
                         command=login)  #
    loan_button.grid(row=6, column=1, columnspan=3)
    exit_button = Button(logined_window, text='Exit', font=('sans-serif', 42), bg='light blue', fg='white',
                         command=pass_)  #
    exit_button.grid(row=7, column=1, columnspan=3)
    logined_window.mainloop()


def pass_():
    pass


def encodeStr(text):
    global fernet, key
    encryptedText = fernet.encrypt(text.encode()).decode()
    return encryptedText


def decodeStr(text):
    global fernet, key
    decryptedText = fernet.decrypt(text.encode()).decode()
    return decryptedText

try:
    database = connector.connect(host=main_passwords.hosts, database=main_passwords.name,
                                 user=main_passwords.users, password=main_passwords.database_password)

    print('successfully connected to database')
except:
    print('database not connected')

cursor = database.cursor()
key = main_passwords.frenet_key.encode()
fernet = Fernet(key)

'''print("___________WELCOME TO THE BANK__________")
print("What Would You Like to Do ?")
print("1)Login")
print("2)Create Account")
print("3)admin account")
ask_login_signup = int(input("Enter an Option : "))'''
login()