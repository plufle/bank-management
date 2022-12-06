from tkinter import *
from tkinter import messagebox
import mysql.connector as connector
import random
from cryptography.fernet import Fernet
import datetime
import pytz
import sys
import customtkinter
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
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    global login_window
    login_window = customtkinter.CTk()
    login_window.geometry('800x524')
    login_window.title('Login')

    welcome = customtkinter.CTkLabel(login_window, text="                             Welcome to Online Bank"
                    , text_font=('sans-serif',25))
    welcome.grid(column=0, row=0, columnspan=6)

    spaces = customtkinter.CTkLabel(login_window, text="           " )
    spaces.grid(column=0, row=1)

    welcome = customtkinter.CTkLabel(login_window, text="                Login   " ,text_font=('sans-serif',21))
    welcome.grid(column=1, row=1, columnspan=2)

    spaces = customtkinter.CTkLabel(login_window, text="             ")
    spaces.grid(column=0, row=1)

    userid_label = customtkinter.CTkLabel(login_window, text="   User ID   ",text_font=('sans-serif',20))
    userid_label.grid(column=1, row=3)

    userid_e = Entry(login_window, borderwidth=10)
    userid_e.grid(column=2, row=3)

    spaces = customtkinter.CTkLabel(login_window, text="             ")
    spaces.grid(column=0, row=4)

    pass_label = customtkinter.CTkLabel(login_window, text="Password   ",text_font=('sans-serif',20))
    pass_label.grid(column=1, row=4)

    pass_e = Entry(login_window, borderwidth=10)
    pass_e.grid(column=2, row=4)

    spaces = customtkinter.CTkLabel(login_window, text="             ")
    spaces.grid(column=0, row=5)
    spaces = customtkinter.CTkLabel(login_window, text="             " )
    spaces.grid(column=1, row=5)

    login_button = customtkinter.CTkButton(login_window, text='Login',
                          command=lambda: login(userid_e.get(),pass_e.get()))
    login_button.grid(row=5, column=1, columnspan=2)

    spaces = customtkinter.CTkLabel(login_window, text="             ")
    spaces.grid(column=0, row=6)

    frame_admin = customtkinter.CTkFrame(login_window)
    frame_admin.grid(column=1, row=6)

    login_button_admin = customtkinter.CTkButton(frame_admin, text='Login',
                                command=pass_e)
    login_button_admin.grid(row=0, column=0,)

    frame_new = customtkinter.CTkFrame(login_window)
    frame_new.grid(column=2, row=6, columnspan=2)

    create_btn = customtkinter.CTkButton(frame_new, text='Create new account',
                         command=pass_e)
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