from tkinter import *
from tkinter import messagebox
import mysql.connector as connector
import random
from cryptography.fernet import Fernet
import datetime
import pytz
import sys
from datetime import date, timedelta
import main_passwords
def pass_():
    pass


def login(x,y):
    userid = int(x)
    password = y

    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    current_user_temp_list = list(current_user_temp_tuple)
    current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
    if current_user_temp_list[2] == password:
        print('successfully logged to the account')
        messagebox.showinfo("login","successfully logged in")
        login_window.destroy()
        logged_screen()

    else:
        print('entered password is incorrect\n please try again')
        response = messagebox.askquestion('login','password is incorrect...try again')
        if response == 'yes':
            login_window.destroy()
            login_screen()
        else:
            sys.exit('user closed')

    return current_user_temp_list

def logged_screen():
    print('GOOD')


def login_screen():
    global login_window
    login_window = Tk()
    login_window.geometry('800x524')
    login_window.title('Login')

    welcome = Label(login_window, text="                          Welcome to Online Bank                     ",
                    font=('Arial Bold', 25))
    welcome.grid(column=0, row=0, columnspan=6)

    spaces = Label(login_window, text="           ", font=('Arial Bold', 22))
    spaces.grid(column=0, row=1)

    welcome = Label(login_window, text="   Login   ", font=('Arial Bold', 20))
    welcome.grid(column=1, row=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 20))
    spaces.grid(column=0, row=1)

    userid_label = Label(login_window, text="   User ID   ", font=('Arial Bold', 15))
    userid_label.grid(column=1, row=3)

    userid_e = Entry(login_window, borderwidth=10, font=('Arial Bold', 10))
    userid_e.grid(column=2, row=3)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 20))
    spaces.grid(column=0, row=4)

    pass_label = Label(login_window, text="Password   ", font=('Arial Bold', 15))
    pass_label.grid(column=1, row=4)

    pass_e = Entry(login_window, borderwidth=10, font=('Arial Bold', 10))
    pass_e.grid(column=2, row=4)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 20))
    spaces.grid(column=0, row=5)
    spaces = Label(login_window, text="             ", font=('Arial Bold', 20))
    spaces.grid(column=1, row=5)

    login_button = Button(login_window, text='Login', font=('Arial Bold', 12), bg='light blue', fg='white',
                          command=lambda: login(userid_e.get(),pass_e.get()))
    login_button.grid(row=5, column=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 20))
    spaces.grid(column=0, row=6)

    frame_admin = LabelFrame(login_window, text='Administrator', font=('Arial Bold', 10))
    frame_admin.grid(column=1, row=6)

    login_button_admin = Button(frame_admin, text='Login', font=('Arial Bold', 12), bg='#FF7F50', fg='white',
                                command=pass_e)
    login_button_admin.grid(row=0, column=0, )

    frame_new = LabelFrame(login_window, text='New Account', font=('Arial Bold', 10), padx=5, pady=5)
    frame_new.grid(column=2, row=6, columnspan=2)

    create_btn = Button(frame_new, text='Create new account', font=('Arial Bold', 12), bg='#00008B', fg='white', padx=7,
                        pady=3, command=pass_e)
    create_btn.grid(row=5, column=0)

    login_window.mainloop()


def currenttime():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

    d_string = current_time.strftime("20%y-%m-%d")
    t_string = current_time.strftime("%H:%M:%S")
    time = [d_string, t_string]
    return time


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

login_screen()